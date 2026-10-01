
from crewai import Agent
from llm_config import get_llm


def create_market_research_agent():

    agent = Agent(
        role="Market Research Specialist",

        goal=(
            "Analyze market demand, customer needs, "
            "industry trends, competitors, and opportunities."
        ),

        backstory=(
            "You are an experienced market research consultant. "
            "You specialize in customer behavior, industry "
            "analysis, competitive research, and market demand."
        ),

        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
        max_iter=3
    )

    return agent
