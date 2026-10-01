
from crewai import Task


def create_consulting_tasks(
    market_agent,
    business_agent,
    marketing_agent,
    financial_agent,
    operations_agent,
    consultant_agent,
    business_info
):

    # TASK 1: MARKET RESEARCH

    market_task = Task(
        description=f"""
        Analyze this business:

        {business_info}

        Research:
        1. Target market
        2. Customer needs
        3. Industry trends
        4. Competitors
        5. Market opportunities
        6. Market challenges

        Clearly identify assumptions.
        Do not invent verified statistics.
        """,

        expected_output=(
            "A structured market research report."
        ),

        agent=market_agent
    )


    # TASK 2: BUSINESS ANALYSIS

    business_task = Task(
        description="""
        Evaluate the business using the provided information
        and market research findings.

        Include:
        1. Business model
        2. Value proposition
        3. SWOT analysis
        4. Strengths and weaknesses
        5. Opportunities and threats
        6. Business risks
        """,

        expected_output=(
            "A detailed business analysis and SWOT report."
        ),

        agent=business_agent,
        context=[market_task]
    )


    # TASK 3: MARKETING STRATEGY

    marketing_task = Task(
        description="""
        Develop a practical marketing strategy.

        Include:
        1. Target customer profile
        2. Brand positioning
        3. Marketing channels
        4. Customer acquisition
        5. Digital marketing strategy
        6. Marketing KPIs
        """,

        expected_output=(
            "A practical marketing and growth strategy."
        ),

        agent=marketing_agent,
        context=[market_task, business_task]
    )


    # TASK 4: FINANCIAL PLANNING

    financial_task = Task(
        description="""
        Prepare a financial planning framework.

        Include:
        1. Startup cost categories
        2. Budget allocation
        3. Revenue model
        4. Monthly expenses
        5. Break-even considerations
        6. Financial risks

        Label numerical estimates as assumptions.
        Do not present estimates as verified figures.
        """,

        expected_output=(
            "A structured financial planning report."
        ),

        agent=financial_agent,
        context=[market_task, business_task]
    )


    # TASK 5: OPERATIONS STRATEGY

    operations_task = Task(
        description="""
        Prepare an operational implementation plan.

        Include:
        1. Required resources
        2. Team roles
        3. Business workflow
        4. Technology requirements
        5. Daily operations
        6. 30/60/90-day implementation milestones
        """,

        expected_output=(
            "A practical operations strategy."
        ),

        agent=operations_agent,
        context=[
            market_task,
            business_task,
            marketing_task,
            financial_task
        ]
    )


    # TASK 6: FINAL BUSINESS STRATEGY REPORT

    final_task = Task(
        description=f"""
        Create a complete professional Business Strategy Report.

        Business Information:
        {business_info}

        Combine all five specialist reports.

        Include:

        1. Executive Summary
        2. Business Overview
        3. Market Research
        4. Competitor Analysis
        5. SWOT Analysis
        6. Business Model
        7. Marketing Strategy
        8. Financial Planning
        9. Operations Strategy
        10. Risk Assessment
        11. 30/60/90-Day Action Plan
        12. Final Strategic Recommendations

        Make the report detailed, clear, and actionable.

        Separate assumptions from verified facts.
        """,

        expected_output=(
            "A comprehensive business strategy report "
            "formatted in Markdown."
        ),

        agent=consultant_agent,

        context=[
            market_task,
            business_task,
            marketing_task,
            financial_task,
            operations_task
        ]
    )


    return [
        market_task,
        business_task,
        marketing_task,
        financial_task,
        operations_task,
        final_task
    ]
