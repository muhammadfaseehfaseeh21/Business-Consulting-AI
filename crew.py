
from crewai import Crew, Process

from market_research_agent import create_market_research_agent
from business_analyst_agent import create_business_analyst_agent
from marketing_agent import create_marketing_agent
from financial_agent import create_financial_agent
from operations_agent import create_operations_agent
from strategy_consultant_agent import create_strategy_consultant_agent

from consulting_tasks import create_consulting_tasks


def run_business_consulting(business_info):

    # Create six agents

    market_agent = create_market_research_agent()
    business_agent = create_business_analyst_agent()
    marketing_agent = create_marketing_agent()
    financial_agent = create_financial_agent()
    operations_agent = create_operations_agent()
    consultant_agent = create_strategy_consultant_agent()

    agents = [
        market_agent,
        business_agent,
        marketing_agent,
        financial_agent,
        operations_agent,
        consultant_agent
    ]

    # Create tasks

    tasks = create_consulting_tasks(
        market_agent,
        business_agent,
        marketing_agent,
        financial_agent,
        operations_agent,
        consultant_agent,
        business_info
    )

    # Create Crew

    consulting_crew = Crew(
        agents=agents,
        tasks=tasks,
        process=Process.sequential,
        verbose=False
    )

    # Execute

    result = consulting_crew.kickoff()

    return str(result)
