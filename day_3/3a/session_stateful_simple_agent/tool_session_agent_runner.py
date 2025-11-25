from tool_session_agent.agent import root_agent #, APP_NAME, USER_ID, session_service
from run_session import run_session
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
import asyncio

# Configuration
APP_NAME = "default"
USER_ID = "default"
MODEL_NAME = "gemini-2.5-flash-lite"

# Set up session service and runner
session_service = InMemorySessionService()
runner = Runner(agent=root_agent, session_service=session_service, app_name="default")

# Test conversation demonstrating session state
asyncio.run(run_session(
    runner,
    [
        "Hi there, how are you doing today? What is my name?",  # Agent shouldn't know the name yet
        "My name is Sam. I'm from Poland.",  # Provide name - agent should save it
        "What is my name? Which country am I from?",  # Agent should recall from session state
    ],
    "state-demo-session",
    session_service=session_service,
    user_id=USER_ID,
    model_name="gemini-2.5-flash-lite",
))

session = asyncio.run(session_service.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id="state-demo-session"
))

print("Session State Contents:")
print(session.state)
print("\n🔍 Notice the 'user:name' and 'user:country' keys storing our data!")