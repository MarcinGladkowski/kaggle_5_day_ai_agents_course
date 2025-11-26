from research_agent.agent import root_agent
from research_agent.libraries import *

runner = InMemoryRunner(
    agent=root_agent,
    plugins=[
        LoggingPlugin()
    ],  # <---- 2. Add the plugin. Handles standard Observability logging across ALL agents
)


print("✅ Runner configured")

print("🚀 Running agent with LoggingPlugin...")
print("📊 Watch the comprehensive logging output below:\n")

response = asyncio.run(runner.run_debug("Find recent papers on quantum computing"))