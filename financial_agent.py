
from crewai import Agent
from llm_config import get_llm


def create_financial_agent():

    agent = Agent(
        role="Financial Analyst",

        goal=(
            "Prepare financial planning covering startup costs, "
            "budget allocation, revenue assumptions, expenses, "
            "and break-even considerations."
        ),

        backstory=(
            "You are a financial consultant experienced in "
            "business budgeting, revenue models, financial "
            "planning, and risk assessment."
        ),

        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
        max_iter=3
    )

    return agent
