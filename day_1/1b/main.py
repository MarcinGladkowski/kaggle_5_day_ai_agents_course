import asyncio
from google.adk.runners import InMemoryRunner

from research_coordinator.agent import research_agent

runner = InMemoryRunner(agent=research_agent)

print("✅ Runner created.")

asyncio.run(runner.run_debug(
    "What are the latest advancements in quantum computing and what do they mean for AI?"
))

print("✅ Response received:")