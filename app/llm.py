from langchain_openai import ChatOpenAI
 

def get_llm():

    return ChatOpenAI(
        base_url="http://localhost:1234/v1",
        api_key="lm-studio",
        model="qwen/qwen3-4b-2507",
        temperature=0
    )

 