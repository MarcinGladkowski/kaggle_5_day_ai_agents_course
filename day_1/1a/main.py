import asyncio
from google.adk.runners import InMemoryRunner

from helpful_assistant.agent import root_agent

runner = InMemoryRunner(agent=root_agent)

print("✅ Runner created.")

asyncio.run(runner.run_debug(
    "What is Agent Development Kit from Google? What languages is the SDK available in?"
))

print("✅ Response received:")