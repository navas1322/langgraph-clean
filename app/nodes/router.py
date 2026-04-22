def router_node(state):
    q = state["question"].lower()

    if "weather" in q:
        route = "weather"
    elif "btc" in q or "stock" in q or "finance" in q:
        route = "finance"
    else:
        route = "general"

    state["route"] = route
    return state