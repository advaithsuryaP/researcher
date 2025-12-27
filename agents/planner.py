from pydantic import BaseModel, Field
from agents import Agent

NO_OF_SEARCHES: int = 3

INSTRUCTIONS: str = f"You are a helpful research assistant. Given a query, come up with a set of web searches to perform in order to best answer the query. \
Output {NO_OF_SEARCHES} terms to search for."

class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(desctiption="The search term to use for the web search.")

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")


planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan
)
