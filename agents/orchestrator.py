from agents.rag_agent import run_rag
from agents.log_agent import run_log_analysis
from agents.risk_agent import run_risk_assessment

def orchestrate(user_input: str):

    if "log" in user_input.lower():
        log_result = run_log_analysis(user_input)
        policy_result = run_rag(user_input)

        final = run_risk_assessment(
            policy=policy_result,
            log_analysis=log_result
        )

        return final

    return run_rag(user_input)
