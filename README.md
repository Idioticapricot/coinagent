# Pirate Agent Template

A pirate-themed AI agent built with Orca Agent SDK and Google's Gemini 2.0 Flash model. This agent responds to all requests in pirate speak while maintaining helpful functionality.

## Features

- 🏴‍☠️ Pirate personality with authentic pirate terminology
- 🤖 Powered by Google Gemini 2.0 Flash model
- 🐳 Docker containerized for easy deployment
- ⚓ Built on Orca Agent SDK for Algorand integration
- 🚀 GitHub Actions CI/CD pipeline

## Quick Start

### Local Development

1. **Clone and install dependencies:**
   ```bash
   git clone <repository-url>
   cd agent-template
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   # Create .env file
   echo "GOOGLE_API_KEY=your_google_api_key_here" > .env
   ```

3. **Run the agent:**
   ```bash
   python app.py
   ```

### Docker Deployment

1. **Build and run:**
   ```bash
   docker build -t pirate-agent .
   docker run -p 8000:8000 pirate-agent
   ```

2. **Or use pre-built image:**
   ```bash
   docker run -p 8000:8000 ghcr.io/yourusername/agent-template:latest
   ```

## Configuration

Update the agent configuration in `app.py`:

```python
config = AgentConfig(
    agent_id="your-agent-id",
    receiver_address="YOUR_ALGO_ADDRESS", 
    price_microalgos=1_000_000,
    agent_token="your_agent_token",
    remote_server_url="http://localhost:3000/api/agent/access"
)
```

## Testing

Run the test to verify Gemini integration:

```bash
python test/test_agent.py
```

Expected output: `Ahoy there, matey!`

## Environment Variables

- `GOOGLE_API_KEY` - Required for Gemini model access

## Tech Stack

- **AI Model**: Google Gemini 2.0 Flash
- **Agent Framework**: Orca Agent SDK
- **AI Library**: Agno
- **Runtime**: Python 3.12
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

## Deployment

The agent automatically deploys to GitHub Container Registry on push to main branch. Configure your Kubernetes deployment to pull from `ghcr.io/yourusername/agent-template:latest`.

## License

MIT License