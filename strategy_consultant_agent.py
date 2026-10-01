
from crewai import Agent
from llm_config import get_llm


def create_strategy_consultant_agent():

    agent = Agent(
        role="Chief Business Strategy Consultant",

        goal=(
            "Combine specialist findings into a complete, "
            "professional, practical business strategy report."
        ),

        backstory=(
            "You are a senior business consultant who integrates "
            "market research, business analysis, marketing, "
            "finance, and operations into a unified strategy."
        ),

        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
        max_iter=3
    )

    return agent
