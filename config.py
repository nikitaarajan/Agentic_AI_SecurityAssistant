from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()

def get_llm():
    return ChatOpenAI(model="gpt-4o-mini")

def get_embeddings():
    return OpenAIEmbeddings()
