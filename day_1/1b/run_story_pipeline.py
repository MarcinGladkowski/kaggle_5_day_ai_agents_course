import asyncio
from google.adk.runners import InMemoryRunner

from story_pipeline.agent import root_agent

runner = InMemoryRunner(agent=root_agent)

print("✅ Runner created.")

asyncio.run(runner.run_debug(
    "Write a short story about a lighthouse keeper who discovers a mysterious, glowing map"
))

print("✅ Response received:")