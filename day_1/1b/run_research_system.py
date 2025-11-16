import asyncio
from google.adk.runners import InMemoryRunner

from research_system.agent import root_agent

runner = InMemoryRunner(agent=root_agent)

print("✅ Runner created.")

asyncio.run(runner.run_debug(
    "Run the daily executive briefing on Tech, Health, and Finance"
))

print("✅ Response received:")