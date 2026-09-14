import json
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field, ValidationError

class Response(str, Enum):
    VALID = """
    {
        "category": "billing",
        "priority": "high",
        "confidence": 0.91,
        "reason": "Customer reports an incorrect invoice."
    }
    """
    MALFORMED = """
    {
        "category": "billing",
        "priority": "high",
        "confidence": 0.91,
        "reason": "Customer reports an incorrect invoice."
    """
    MISSING_FIELD = """
    {
        "category": "billing",
        "confidence": 0.91,
        "reason": "Customer reports an incorrect invoice."
    }
    """
    INVALID_ENUM = """
    {
        "category": "banana",
        "priority": "high",
        "confidence": 0.91,
        "reason": "Customer reports an incorrect invoice."
    }
    """
    SEMANTICALLY_INVALID = """
    {
        "category": "security",
        "priority": "low",
        "confidence": 0.95,
        "reason": "Customer reports unauthorized account access."
    }
    """
    LOW_CONFIDENCE = """
    {
        "category": "security",
        "priority": "low",
        "confidence": 0.65,
        "reason": "Customer reports unauthorized account access."
    }
    """
    UNKNOWN_FIELD = """
    {
        "category": "billing",
        "priority": "high",
        "confidence": 0.91,
        "reason": "Customer reports an incorrect invoice.",
        "extra_field": "unexpected"
    }
    """
    CONFIDENCE_OUT_OF_RANGE = """
    {
        "category": "billing",
        "priority": "high",
        "confidence": 1.5,
        "reason": "Customer reports an incorrect invoice."
    }
    """
    WRONG_FIELD_TYPE = """
    {
    
        "category": "billing",
        "priority": "high",
        "confidence": "not a float",
        "reason": "Customer reports an incorrect invoice."
    }
    """
    EMPTY = "{}"
    NULL = None
    VERY_LONG_REASON = """
    {
        "category": "billing",
        "priority": "high",
        "confidence": 0.91,
        "reason": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    }
    """
    UNEXPECTED_UNICODE = """
    {
        "category": "billing",
        "priority": "high",
        "confidence": 0.91,
        "reason": "Customer reports an incorrect invoice. \u2603 \u2764"
    }
    """
    DUPLICATE_FIELDS = """
    {
        "category": "billing",
        "category": "security",
        "priority": "high",
        "confidence": 0.91,
        "reason": "Customer reports an incorrect invoice."
    }
    """

class TicketClassification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    class Category(str, Enum):
        BILLING = "billing"
        ACCOUNT = "account"
        SECURITY = "security"
        TECHNICAL = "technical"
        OTHER = "other"

    class Application(str, Enum):
        APP1 = "App1"
        APP2 = "App2"
        APP3 = "App3"

    class Priority(str, Enum):
        LOW = "low"
        MEDIUM = "medium"
        HIGH = "high"
        URGENT = "urgent"

    category: Category
    application: Application | None = None
    priority: Priority
    confidence: float = Field(ge=0, le=1)
    reason: str = Field(max_length=100)

def parse_model_output(output: str):
    def reject_duplicate_fields(pairs):
        data = {}
        for key, value in pairs:
            if key in data:
                raise ValueError(f"duplicate fields: {key}")
            data[key] = value
        return data

    return json.loads(output, object_pairs_hook=reject_duplicate_fields)

def validate_schema(data: dict):
    return TicketClassification.model_validate(data)

def validate_business_rules(ticket: TicketClassification):
    if ticket.confidence < 0.7:
        raise ValueError(
            "Business rule violation: confidence must be greater than or equal to 0.7."
        )
    if ticket.category == TicketClassification.Category.SECURITY and ticket.priority != TicketClassification.Priority.URGENT:
        raise ValueError(
            "Business rule violation: Security tickets must have an Urgent priority."
        )

    return True

def validate_output(output: str) -> TicketClassification:
    data = parse_model_output(output)
    ticket = validate_schema(data)
    validate_business_rules(ticket)
    return ticket
    
if __name__ == "__main__":
    try:
        ticket = validate_output(Response.VALID.value)
    except json.JSONDecodeError as e:
        print(f"Error parsing model output: {e}")
    except ValidationError as e:
        print(f"Schema validation error: {e}")
    except ValueError as e:
        print(f"Business rule validation error: {e}")
    else:
        print("Ticket classification is valid and meets all business rules.")