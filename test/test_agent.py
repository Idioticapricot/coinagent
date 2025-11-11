import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini

# Load environment variables
load_dotenv()

# Initialize Gemini agent
agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    markdown=True,
)

# Test the agent
response = agent.run("Say hello in pirate speak")
print(response.content if hasattr(response, 'content') else str(response))