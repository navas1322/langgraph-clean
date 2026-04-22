from typing import TypedDict, List

class State(TypedDict):
    user_id: str
    question: str
    route: str
    history: List[str]
    response: str