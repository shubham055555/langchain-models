from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

chat = ChatOpenAI(
    model="anthropic/claude-3.5-sonnet",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7,
    max_tokens=100   #  ye line add karo
)

messages = [
    SystemMessage(content="You are a helpful AI teacher."),
    HumanMessage(content="Explain LangChain in simple words.")
]

print(chat.invoke(messages).content)
