from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from config import get_llm, get_embeddings

# Load and split docs once
loader = TextLoader("documents/security_policy.txt")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

vectorstore = Chroma.from_documents(split_docs, get_embeddings())
retriever = vectorstore.as_retriever()

prompt = ChatPromptTemplate.from_template(
    """You are a security assistant.

    Context:
    {context}

    Question:
    {question}
    """
)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | get_llm()
)

def run_rag(question: str):
    return rag_chain.invoke(question).content
