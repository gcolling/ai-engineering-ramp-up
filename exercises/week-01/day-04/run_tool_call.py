from ollama_client import call_llm, extract_tool_call
from tool_calling_lab import call_tool


response = call_llm(
    "What is the status of order O987654 for customer C123456?"
)

tool_call = extract_tool_call(response)

if tool_call is None:
    print("Model did not request a tool.")
else:
    result = call_tool(
        tool_call["name"],
        tool_call["arguments"]
    )
    
    print(f"Tool result: {result}")

