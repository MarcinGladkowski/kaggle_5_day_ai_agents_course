import asyncio
from google.adk.runners import InMemoryRunner

from image_agent.agent import root_agent

runner = InMemoryRunner(agent=root_agent)

print("✅ Runner created.")

response = asyncio.run(runner.run_debug("Provide a sample tiny image", verbose=True))

print("✅ Response received:")

for event in response:
    if event.content and event.content.parts:
        for part in event.content.parts:
            if hasattr(part, "function_response") and part.function_response:
                for item in part.function_response.response.get("content", []):
                    if item.get("type") == "image":
                        print("Image URL:", item) # use package to display image