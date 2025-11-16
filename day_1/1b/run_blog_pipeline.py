import asyncio
from google.adk.runners import InMemoryRunner

from blog_pipeline.agent import root_agent

runner = InMemoryRunner(agent=root_agent)

print("✅ Runner created.")

asyncio.run(runner.run_debug(
    "Write a blog post about the benefits of multi-agent systems for software developers"
))

print("✅ Response received:")