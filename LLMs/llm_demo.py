from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI

load_dotenv()

print("KEY:", os.getenv("OPENROUTER_API_KEY"))  # check

llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

print(llm.invoke("What is LangChain?").content)
