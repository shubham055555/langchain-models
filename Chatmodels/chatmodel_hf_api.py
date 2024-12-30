from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()
token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token=token,
)

print(llm.invoke("Explain LangChain in simple words"))
