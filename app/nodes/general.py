import os
from openai import OpenAI
from app.memory import save_history

client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL", "http://localhost:1234/v1"),
    api_key=os.getenv("OPENAI_API_KEY", "lm-studio")
)

MODEL = os.getenv("MODEL_NAME", "local-model")

def general_node(state):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": state["question"]}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7
    )

    answer = response.choices[0].message.content

    save_history(state["user_id"], state["question"], answer)

    return {**state, "response": answer}