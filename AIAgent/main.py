import os
import argparse
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("API Key was not found")

from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Charbot")
parser.add_argument("user_prompt", type=str, help="What would you like to ask AI Agent?")
args = parser.parse_args()

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ],
)

if response.usage == None:
    raise RuntimeError("No usage data, likely a failed API request")
else:
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

print(response.choices[0].message.content)