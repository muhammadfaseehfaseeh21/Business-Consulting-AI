
from crewai import Agent
from llm_config import get_llm


def create_operations_agent():

    agent = Agent(
        role="Operations Strategist",

        goal=(
            "Develop an operational strategy covering resources, "
            "workflow, staffing, technology, and implementation."
        ),

        backstory=(
            "You are an operations management consultant "
            "specializing in business processes, resource "
            "planning, workflow optimization, and execution."
        ),

        llm=get_llm(),
        verbose=False,
        allow_delegation=False,
        max_iter=3
    )

    return agent
