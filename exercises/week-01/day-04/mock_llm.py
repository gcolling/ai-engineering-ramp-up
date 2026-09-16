def call_llm(response_type: str):
    if response_type == "tool_call":
        return {
            "type": "tool_call",
            "name": "get_order_status",
            "arguments": {
                "customer_reference": "C123456",
                "order_id": "O987654"
            }
        }
    if response_type == "final_answer":
        return {
            "type": "final_answer",
            "content": "I don't need to call a tool."
        }

    raise ValueError(f"Unknown mock LLM response type: {response_type}")