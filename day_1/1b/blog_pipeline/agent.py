from google.adk.agents import SequentialAgent

from .agents.outline_agent import outline_agent
from .agents.writer_agent import writer_agent
from .agents.editor_agent import editor_agent

root_agent = SequentialAgent(
    name="blog_pipeline",
    sub_agents=[outline_agent, writer_agent, editor_agent],
)

print("✅ Sequential Agent created.")