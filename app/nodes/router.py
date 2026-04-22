#def router_node(state):
#    q = state["question"].lower()
#
#    if "weather" in q:
#        route = "weather"
#    elif "btc" in q or "stock" in q or "finance" in q:
#        route = "finance"
#    else:
#        route = "general"
#
#    state["route"] = route
#    return state

from app.llm import get_llm

llm = get_llm()

def router_node(state):
    question = state["question"]

    prompt = f"""
You are a routing system.

Decide which route to use:

Options:
- general
- weather
- finance

Return ONLY one word.

Question: {question}
"""

    response = llm.invoke([
        {"role": "system", "content": "You are a strict router."},
        {"role": "user", "content": prompt}
    ])

    route = response.content.strip().lower()

    # safety guard (VERY IMPORTANT in LangGraph)
    if "weather" in route:
        route = "weather"
    elif "finance" in route:
        route = "finance"
    else:
        route = "general"

    state["route"] = route
    return state