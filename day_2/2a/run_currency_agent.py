import asyncio
from google.adk.runners import InMemoryRunner

from currency_agent.agent import root_agent

runner = InMemoryRunner(agent=root_agent)

print("✅ Runner created.")

asyncio.run(runner.run_debug(
    "I want to convert 500 US Dollars to Euros using my Platinum Credit Card. How much will I receive?"
))

print("✅ Response received:")