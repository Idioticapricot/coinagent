import os
from dotenv import load_dotenv
from orca_agent_sdk import AgentConfig, AgentServer
from agno.agent import Agent
from agno.models.google import Gemini

# Load environment variables
load_dotenv()

# Initialize Gemini agent
agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    markdown=True,
    instructions="You are a pirate agent. Respond to all requests in pirate speak with 'Ahoy!' and use pirate terminology like 'matey', 'ye', 'aye', and 'arrr'. Be helpful but maintain your pirate persona at all times."
)

def handle_task(job_input: str) -> str:
    """Use Gemini agent to process the job input"""
    try:
        response = agent.run(job_input)
        return response.content if hasattr(response, 'content') else str(response)
    except Exception as e:
        return f"Error processing request: {str(e)}"

if __name__ == "__main__":
    config = AgentConfig(
        agent_id="5bbf48cf-62a2-4ab3-bd96-1d29ba0fc1f3",
        receiver_address="2IEECJADZ3J55PFOHKFQBJAGMMMU2NARSQ3H2VXY2ECXFBKSZVP24GQSYY",
        price_microalgos=1_000_000,
        agent_token="b8c8103f9fb07a46b21f1eaa278bc96cd973647ea844404a6e53ca61e88e611e",
        remote_server_url="http://localhost:3000/api/agent/access",
        app_id=749663128,
    )

    AgentServer(config=config, handler=handle_task).run()