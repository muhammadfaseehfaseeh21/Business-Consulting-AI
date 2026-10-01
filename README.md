
# Business Consulting AI

A Multi-Agent Business Consulting System powered by CrewAI, Groq, and Streamlit.

## Features

- Six specialized AI agents
- Market research
- Business analysis
- SWOT analysis
- Marketing strategy
- Financial planning
- Operations strategy
- Final business strategy report
- Download report as Markdown
- Streamlit interface

## Technology Stack

- Python
- CrewAI
- Groq API
- openai/gpt-oss-120b
- Streamlit

## Project Structure

All Python files are stored in the main repository.

No agents or tasks folders are required.

## API Key Setup

Add your Groq API key in Streamlit Secrets:

GROQ_API_KEY = "your_actual_api_key"

Never upload your actual API key to GitHub.

## Deployment

1. Upload all files to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your repository.
4. Select app.py as the main file.
5. Add GROQ_API_KEY in Secrets.
6. Deploy the application.

## Agent Workflow

User Input
    ↓
Market Research Agent
    ↓
Business Analyst Agent
    ↓
Marketing Strategist
    ↓
Financial Analyst
    ↓
Operations Strategist
    ↓
Chief Strategy Consultant
    ↓
Business Strategy Report
