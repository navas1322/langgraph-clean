memory_store = {}

def get_history(user_id: str):
    return memory_store.get(user_id, [])

def save_history(user_id: str, question: str, answer: str):
    if user_id not in memory_store:
        memory_store[user_id] = []

    memory_store[user_id].append(f"User: {question}")
    memory_store[user_id].append(f"AI: {answer}")