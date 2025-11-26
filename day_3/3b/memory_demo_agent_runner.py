from memory_demo_agent.libraries import *
from memory_demo_agent.agent import user_agent, memory_service
from session import run_session
import asyncio

APP_NAME = "MemoryDemoApp"
USER_ID = "demo_user"

# Create Session Service
session_service = InMemorySessionService()  # Handles conversations

# Create runner with BOTH services
runner = Runner(
    agent=user_agent,
    app_name="MemoryDemoApp",
    session_service=session_service,
    memory_service=memory_service,  # Memory service is now available!
)

print("✅ Agent and Runner created with memory support!")


# User tells agent about their favorite color
asyncio.run(run_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_service=session_service,
    runner_instance=runner,
    user_queries="My favorite color is blue-green. Can you write a Haiku about it?",
    session_id="conversation-01",  # Session ID
))

session = asyncio.run(session_service.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id="conversation-01"
))

# Let's see what's in the session
print("📝 Session contains:")
for event in session.events:
    text = (
        event.content.parts[0].text[:60]
        if event.content and event.content.parts
        else "(empty)"
    )
    print(f"  {event.content.role}: {text}...")
    

# new session where agent should recall from memory
asyncio.run(run_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_service=session_service,
    runner_instance=runner,
    user_queries="My birthday is on March 15th.", 
    session_id="birthday-session-01"
))

# Manually save the session to memory
birthday_session = asyncio.run(session_service.get_session(
    app_name=APP_NAME, user_id=USER_ID, session_id="birthday-session-01"
))

asyncio.run(memory_service.add_session_to_memory(birthday_session))
print("✅ Birthday session saved to memory!")

# Test retrieval in a NEW session
asyncio.run(run_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_service=session_service,
    runner_instance=runner,
    user_queries="When is my birthday?",
    session_id="birthday-session-02"
))