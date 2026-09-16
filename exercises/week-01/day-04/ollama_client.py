import requests
from tool_calling_lab import TOOLS

OLLAMA_URL = "http://localhost:11434/api/chat"

def call_llm(user_message: str) -> dict:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen3:8b",
            "messages": [
                {
                    "role":"user",
                    "content": user_message
                }
            ],
            "tools": TOOLS,
            "stream": False
        },
        timeout=30
    )

    response.raise_for_status()

    return response.json()

def extract_tool_call(response: dict) -> dict | None:
    tool_calls = response.get("message", {}).get("tool_calls", [])
    
    if not tool_calls:
        return None
    
    tool_call = tool_calls[0]
    
    return {
        "type": "tool_call",
        "name": tool_call["function"]["name"],
        "arguments": tool_call["function"]["arguments"]
    }