
from crewai import Agent
from llm_config import get_llm


def create_business_analyst_agent():

    agent = Agent(
        role="Business Analyst",

        goal=(
            "Evaluate business models, strengths, weaknesses, "
            "opportunities, threats, and business risks."
        ),

        backstory=(
            "You are a professional business analyst skilled "
            "in SWOT analysis, business models, strategic "
            "planning, and business evaluation."
        ),

        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
        max_iter=3
    )

    return agent
