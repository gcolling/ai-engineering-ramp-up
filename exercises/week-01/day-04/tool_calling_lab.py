import re
from mock_llm import call_llm

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_order_status",
            "description": "Get the status of a customer's order.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_reference": {
                        "type": "string",
                        "description": "Customer reference such as C123456.",
                    },
                    "order_id": {
                        "type": "string",
                        "description": "Order ID such as O987654.",
                    },
                },
                "required": [
                    "customer_reference",
                    "order_id",
                ],
            },
        },
    }
]


def get_order_status(customer_reference: str, order_id: str) -> dict | str:
    orders = {
        "C123456": {
            "O987654": {
                "status": "shipped",
                "tracking_number": "TRK001",
            },
            "O987655": {
                "status": "processing",
                "tracking_number": None,
            },
        },
        "C654321": {
            "O123456": {
                "status": "delivered",
                "tracking_number": "TRK002",
            },
            "O123457": {
                "status": "cancelled",
                "tracking_number": None,
            },
        },
        "C789012": {
            "O345678": {
                "status": "shipped",
                "tracking_number": "TRK003",
            },
        }
    }

    try:
        order = orders[customer_reference][order_id]
    except KeyError:
        return f"Order {order_id} not found for the customer reference {customer_reference}"

    return order


TOOL_FUNCTIONS = {
    "get_order_status": get_order_status,
}


def validate_arguments(arguments: dict):
    try:
        customer_reference = arguments['customer_reference']
        order_id = arguments['order_id']
    except KeyError:
        raise ValueError(f"Missing tool arguments.")

    if (
        not isinstance(customer_reference, str)
        or not isinstance(order_id, str)
        or not re.fullmatch(r"^C[0-9]{6}$", customer_reference)
        or not re.fullmatch(r"^O[0-9]{6}$", order_id)
    ):
        raise ValueError(f"Invalid tool arguments received.")
    

def call_tool(tool_name: str, arguments: dict | None = None) -> dict | str:
    available_tool_names = {
        tool["function"]["name"]
        for tool in TOOLS
    }
    if tool_name not in available_tool_names:
        raise ValueError(f"Tool '{tool_name}' not found.")

    tool_function = TOOL_FUNCTIONS.get(tool_name)
    if tool_function is None:
        raise ValueError(f"Tool '{tool_name}' has no implementation.")

    arguments = arguments or {}
    validate_arguments(arguments)
    
    return tool_function(**arguments)


def process_llm_response(response: dict):
    response_type = response.get("type")

    if response_type == "final_answer":
        if "content" not in response:
            raise ValueError("Missing final answer content.")
        return response["content"]

    if response_type == "tool_call":
        if "name" not in response or "arguments" not in response:
            raise ValueError("Missing tool call fields.")
        return call_tool(response["name"], response["arguments"])

    raise ValueError("Unknown LLM response type.")