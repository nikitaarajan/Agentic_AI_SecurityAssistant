from langchain_core.prompts import ChatPromptTemplate
from config import get_llm

risk_prompt = ChatPromptTemplate.from_template(
    """You are a security risk assessor.

    Policy context:
    {policy}

    Log findings:
    {log_analysis}

    Output JSON with:
    - incident_type
    - severity
    - recommended_actions
    """
)

risk_chain = risk_prompt | get_llm()

def run_risk_assessment(policy: str, log_analysis: str):
    return risk_chain.invoke({
        "policy": policy,
        "log_analysis": log_analysis
    }).content
