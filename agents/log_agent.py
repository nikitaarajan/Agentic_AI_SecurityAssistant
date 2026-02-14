from langchain_core.prompts import ChatPromptTemplate
from config import get_llm

log_prompt = ChatPromptTemplate.from_template(
    """You are a cybersecurity log analysis expert.

    Analyse these logs:
    {logs}

    Identify:
    - suspicious IPs
    - anomaly patterns
    - severity
    """
)

log_chain = log_prompt | get_llm()

def run_log_analysis(logs: str):
    return log_chain.invoke({"logs": logs}).content
