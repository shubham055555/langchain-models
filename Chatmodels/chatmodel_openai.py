from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

# .env load
load_dotenv()

# Chat Model (OpenRouter through LangChain)
chat = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7,
    max_completion_tokens=100
)

# Simple chat
response = chat.invoke("who is the prime minister of india")

print(response.content)
