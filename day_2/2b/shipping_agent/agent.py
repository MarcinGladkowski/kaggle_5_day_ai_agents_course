from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.function_tool import FunctionTool
from google.adk.tools.function_tool import FunctionTool

from google.adk.apps.app import App, ResumabilityConfig


from .tools.place_shipping_order import place_shipping_order

# Create shipping agent with pausable tool
shipping_agent = LlmAgent(
    name="shipping_agent",
    model="gemini-2.5-flash-lite",
    instruction="""You are a shipping coordinator assistant.
  
  When users request to ship containers:
   1. Use the place_shipping_order tool with the number of containers and destination
   2. If the order status is 'pending', inform the user that approval is required
   3. After receiving the final result, provide a clear summary including:
      - Order status (approved/rejected)
      - Order ID (if available)
      - Number of containers and destination
   4. Keep responses concise but informative
  """,
    tools=[FunctionTool(func=place_shipping_order)],
)

print("✅ Shipping Agent created!")

# Wrap the agent in a resumable app - THIS IS THE KEY FOR LONG-RUNNING OPERATIONS!
shipping_app = App(
    name="shipping_coordinator",
    root_agent=shipping_agent,
    resumability_config=ResumabilityConfig(is_resumable=True),
)

print("✅ Resumable app created!")