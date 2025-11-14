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
        receiver_address="ZXFGWY3SGYOTFH5BDEI2EPMV5SGLMBUEFCCHNB544JGGE7L4BQ6UDVCGRY",
        price_microalgos=1_000_000,
        agent_token="fff1c4310634031b6cd0b8277a28534f1a231382275de4281ac6334a408a5254",
        remote_server_url="http://localhost:3000/api/agent/access",
        app_id=749660886,
    )

    AgentServer(config=config, handler=handle_task).run()