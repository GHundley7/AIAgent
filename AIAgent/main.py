import os
import argparse
from dotenv import load_dotenv
from prompts import system_prompt
from call_function import available_functions
import json

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
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
    tools=available_functions,
    temperature=0
)

message = response.choices[0].message

if response.usage == None:
    raise RuntimeError("No usage data, likely a failed API request")
elif args.verbose == True:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")

if message.tool_calls:
    for tool_call in message.tool_calls:
        function_args = json.loads(tool_call.function.arguments or "{}")
        print(f"Calling function: {tool_call.function.name}({function_args})")
else: 
    print(response.choices[0].message.content)

