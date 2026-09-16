from enum import Enum

import pytest
from mock_llm import call_llm
from tool_calling_lab import call_tool, process_llm_response

class TOOLS(str, Enum):
    GET_ORDER_STATUS = "get_order_status"
    UNKNOWN_TOOL = "unknown_tool"


def test_unknown_tool_name():
    with pytest.raises(ValueError, match="not found"):
        call_tool(tool_name=TOOLS.UNKNOWN_TOOL)


def test_missing_arguments():
    with pytest.raises(ValueError, match="Missing tool arguments"):
        call_tool(tool_name=TOOLS.GET_ORDER_STATUS)


def test_invalid_customer_reference():
    arguments = {
        "customer_reference": "DROP TABLE customers",
        "order_id": "O123435"
    }

    with pytest.raises(ValueError, match="Invalid tool arguments"):
        call_tool(tool_name=TOOLS.GET_ORDER_STATUS, arguments=arguments)


def test_invalid_order_id():
    arguments = {
        "customer_reference": "C123456",
        "order_id": "DROP DATABASE"
    }

    with pytest.raises(ValueError, match="Invalid tool arguments"):
        call_tool(tool_name=TOOLS.GET_ORDER_STATUS, arguments=arguments)


def test_wrong_argument_type():
    arguments = {
        "customer_reference": 1234561,
        "order_id": "O123435"
    }

    with pytest.raises(ValueError, match="Invalid tool arguments"):
        call_tool(tool_name=TOOLS.GET_ORDER_STATUS, arguments=arguments)


def test_valid_tool_call():
    arguments = {
        "customer_reference": "C123456",
        "order_id": "O987654"
    }

    order = call_tool(tool_name=TOOLS.GET_ORDER_STATUS, arguments=arguments)
    assert order['status'] == "shipped"
    assert order['tracking_number'] == "TRK001"


def test_process_llm_tool_call():
    response = call_llm("tool_call")

    result = process_llm_response(response)

    assert result["status"] == "shipped"
    assert result["tracking_number"] == "TRK001"


def test_process_llm_final_answer():
    response = call_llm("final_answer")

    result = process_llm_response(response)

    assert result == "I don't need to call a tool."


def test_unknown_llm_response_type():
    response = {
        "type": "something_unknown"
    }

    with pytest.raises(ValueError, match="Unknown LLM response type"):
        process_llm_response(response)


def test_unknown_mock_llm_scenario():
    with pytest.raises(ValueError, match="Unknown mock LLM response type"):
        call_llm("unexpected")


def test_tool_call_with_missing_arguments():
    response = {
        "type": "tool_call",
        "name": "get_order_status",
    }

    with pytest.raises(ValueError, match="Missing tool call fields"):
        process_llm_response(response)


def test_final_answer_with_missing_content():
    with pytest.raises(ValueError, match="Missing final answer content"):
        process_llm_response({"type": "final_answer"})