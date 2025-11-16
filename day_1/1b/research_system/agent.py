from google.adk.agents import SequentialAgent, ParallelAgent

from .agents.financial_research_agent import finance_researcher
from .agents.health_researcher_agent import health_researcher
from .agents.tech_researcher_agent import tech_researcher
from .agents.aggregator import aggregator_agent


# The ParallelAgent runs all its sub-agents simultaneously.
parallel_research_team = ParallelAgent(
    name="ParallelResearchTeam",
    sub_agents=[tech_researcher, health_researcher, finance_researcher],
)

# This SequentialAgent defines the high-level workflow: run the parallel team first, then run the aggregator.
root_agent = SequentialAgent(
    name="research_system",
    sub_agents=[parallel_research_team, aggregator_agent],
)

print("✅ Parallel and Sequential Agents created.")