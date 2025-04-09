import requests
from dotenv import load_dotenv
import os

load_dotenv()

access_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')

modelo = "deepseek-ai/DeepSeek-R1"

url = f"https://api-inference.huggingface.co/models/{modelo}"
json = {
    "inputs": "Hello, what is your name?"
}


headers = {"Authorization": f"Bearer {access_token}"}

response = requests.post(url, json=json)

print(response)
print(response.json())
