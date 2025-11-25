from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService 
from google.genai import types
from google.adk.apps.app import App, EventsCompactionConfig
from session_agent.agent import root_agent
from run_session import run_session
import asyncio


APP_NAME = "default"  # Application
USER_ID = "default"  # User
SESSION = "default"  # Session
MODEL_NAME = "gemini-2.5-flash-lite"

db_url = "sqlite:///my_agent_data.db"  # Local SQLite file
session_service = DatabaseSessionService(db_url=db_url)


research_app_compacting = App(
    name="research_app_compacting",
    root_agent=root_agent,
    # This is the new part!
    events_compaction_config=EventsCompactionConfig(
        compaction_interval=2,  # Trigger compaction every 2 invocations
        overlap_size=1,  # Keep 1 previous turn for context
    ),
)

# Step 3: Create the Runner
runner = Runner(app=research_app_compacting, session_service=session_service)

###
#  Only invoking session with same session id allows to access previous context (get knowledge of previous interactions)
###
asyncio.run(run_session(
    runner,
    [
        "Hi, I am Sam! What is the capital of United States?",
    ],
    "stateful-agentic-session-1",
))

asyncio.run(run_session(
    runner,
    [
        "What I asked you in the previous session?",
        "Hello! What is my name?",  # This time, the agent should remember!
    ],
    "stateful-agentic-session-1",
))

# Compensation test

# Turn 1
asyncio.run(run_session(
    runner,
    "What is the latest news about AI in healthcare?",
    "compaction_demo",
))

# Turn 2
asyncio.run(run_session(
    runner,
    "Are there any new developments in drug discovery?",
    "compaction_demo",
))  
# Turn 3 - Compaction should trigger after this turn!
asyncio.run(run_session(
    runner,
    "Tell me more about the second development you found.",
    "compaction_demo",
))

# Turn 4
asyncio.run(run_session(
    runner,
    "Who are the main companies involved in that?",
    "compaction_demo",
))

# Get the final session state
final_session = asyncio.run(session_service.get_session(
    app_name=research_app_compacting.name,
    user_id=USER_ID,
    session_id="compaction_demo",
))

print("--- Searching for Compaction Summary Event ---")
found_summary = False
for event in final_session.events:
    # Compaction events have a 'compaction' attribute
    if event.actions and event.actions.compaction:
        print("\n✅ SUCCESS! Found the Compaction Event:")
        print(f"  Author: {event.author}")
        print(f"\n Compacted information: {event}")
        found_summary = True
        break

if not found_summary:
    print(
        "\n❌ No compaction event found. Try increasing the number of turns in the demo."
    )