from langgraph.graph import StateGraph
from app.state import State

from app.nodes.router import router_node
from app.nodes.general import general_node
from app.nodes.weather import weather_node
from app.nodes.finance import finance_node

builder = StateGraph(State)

builder.add_node("router", router_node)
builder.add_node("general", general_node)
builder.add_node("weather", weather_node)
builder.add_node("finance", finance_node)

builder.set_entry_point("router")

def route_selector(state):
    return state["route"]

builder.add_conditional_edges("router", route_selector)

builder.add_edge("general", "__end__")
builder.add_edge("weather", "__end__")
builder.add_edge("finance", "__end__")

graph = builder.compile()