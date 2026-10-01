
from crewai import Agent
from llm_config import get_llm


def create_marketing_agent():

    agent = Agent(
        role="Marketing Strategist",

        goal=(
            "Develop a marketing strategy to attract customers, "
            "improve brand awareness, and support business growth."
        ),

        backstory=(
            "You are a digital marketing consultant specializing "
            "in customer acquisition, branding, social media, "
            "marketing channels, and growth strategies."
        ),

        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
        max_iter=3
    )

    return agent
