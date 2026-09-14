import json
from enum import Enum
from pydantic import BaseModel, ConfigDict, Field, ValidationError

class Output(str, Enum):
    VALID = """
    {
        "intent": "refund",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    MALFORMED = """
    {
        "intent": "refund",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 0.95
    """
    MISSING_FIELD = """
    {
        "intent": "refund",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "confidence": 0.95
    }
    """
    INVALID_ENUM = """
    {
        "intent": "invalid_intent",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    WRONG_FIELD_TYPE = """
    {
        "intent": 42,
        "department": true,
        "requires_human_review": 1,
        "reason": 12345,
        "customer_reference": 67890,
        "confidence": "high"
    }
    """
    HUMAN_REVIEW_REQUIRED = """
    {
        "intent": "refund",
        "department": "support",
        "requires_human_review": true,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    EXTRA_FIELD = """
    {
        "intent": "refund",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 0.95,
        "extra_field": "unexpected"
    }
    """
    SEMANTICALLY_INVALID = """
    {
        "intent": "refund",
        "department": "marketing",
        "requires_human_review": true,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    LOW_CONFIDENCE = """
    {
        "intent": "refund",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 0.65
    }
    """
    CONFIDENCE_BOUNDARY = """
    {
        "intent": "refund",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 0.7
    }
    """
    CONFIDENCE_OUT_OF_RANGE = """
    {
        "intent": "refund",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 1.5
    }
    """
    VERY_LONG_REASON = """
    {
        "intent": "refund",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product. The product was found to be faulty and did not meet the quality standards expected by the customer, leading to dissatisfaction and a request for a full refund.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    INVALID_CUSTOMER_REFERENCE = """
    {
        "intent": "refund",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "InvalidReference",
        "confidence": 0.95
    }
    """
    DUPLICATE_FIELDS = """
    {
        "intent": "refund",
        "intent": "address_update",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    REFUND_FINANCE = """
    {
        "intent": "refund",
        "department": "finance",
        "requires_human_review": false,
        "reason": "Customer requests a refund for a defective product.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    ADDRESS_UPDATE_WRONG_DEPARTMENT = """
    {
        "intent": "address_update",
        "department": "sales",
        "requires_human_review": false,
        "reason": "Customer requests an address update.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    PLAN_CHANGE_WRONG_DEPARTMENT = """
    {
        "intent": "plan_change",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests a plan change.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    ACCOUNT_DELETION_WRONG_DEPARTMENT = """
    {
        "intent": "account_deletion",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests account deletion.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    AUTOMATIC_MARKETING = """
    {
        "intent": "refund",
        "department": "marketing",
        "requires_human_review": false,
        "reason": "Customer requests a marketing follow-up.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    AUTOMATIC_ADDRESS_UPDATE = """
    {
        "intent": "address_update",
        "department": "support",
        "requires_human_review": false,
        "reason": "Customer requests an address update.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    AUTOMATIC_PLAN_CHANGE = """
    {
        "intent": "plan_change",
        "department": "sales",
        "requires_human_review": false,
        "reason": "Customer requests a plan change.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """
    AUTOMATIC_ACCOUNT_DELETION = """
    {
        "intent": "account_deletion",
        "department": "technical",
        "requires_human_review": false,
        "reason": "Customer requests account deletion.",
        "customer_reference": "C123456",
        "confidence": 0.95
    }
    """

class WorkflowDecision(BaseModel):
    model_config = ConfigDict(extra="forbid")

    class Intent(str, Enum):
        ACCOUNT_DELETION = "account_deletion"
        REFUND = "refund"
        ADDRESS_UPDATE = "address_update"
        PLAN_CHANGE = "plan_change"

    class Department(str, Enum):
        MARKETING = "marketing"
        SUPPORT = "support"
        SALES = "sales"
        TECHNICAL = "technical"
        FINANCE = "finance"

    intent: Intent
    department: Department
    requires_human_review: bool
    reason: str = Field(max_length=200)
    confidence: float = Field(ge=0.0, le=1.0)
    customer_reference: str = Field(pattern=r"^C[0-9]{6}$")

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
    return WorkflowDecision.model_validate(data)

def validate_business_rules(decision: WorkflowDecision):
    if decision.requires_human_review and decision.department == WorkflowDecision.Department.MARKETING:
        raise ValueError("Business rule violation: Marketing department cannot require human review.")
    if decision.intent == WorkflowDecision.Intent.REFUND and decision.department == WorkflowDecision.Department.FINANCE:
        raise ValueError("Business rule violation: Finance department cannot process refund requests.")
    if decision.confidence < 0.7:
        raise ValueError("Business rule violation: confidence must be greater than or equal to 0.7.")
    if decision.intent == WorkflowDecision.Intent.ADDRESS_UPDATE and decision.department != WorkflowDecision.Department.SUPPORT:
        raise ValueError("Business rule violation: Address update requests must be handled by the support department.")
    if decision.intent == WorkflowDecision.Intent.PLAN_CHANGE and decision.department != WorkflowDecision.Department.SALES:
        raise ValueError("Business rule violation: Plan change requests must be handled by the sales department.")
    if decision.intent == WorkflowDecision.Intent.ACCOUNT_DELETION and decision.department != WorkflowDecision.Department.TECHNICAL:
        raise ValueError("Business rule violation: Account deletion requests must be handled by the technical department.")

def validate_output(output: str) -> WorkflowDecision:
    data = parse_model_output(output)
    decision = validate_schema(data)
    validate_business_rules(decision)
    return decision

def route_workflow(decision: WorkflowDecision) -> str:
    if decision.requires_human_review:
        print(
            f"Routing {decision.customer_reference} to human review "
            f"because: {decision.reason}"
        )
        return "human_review"

    department_actions = {
        WorkflowDecision.Department.MARKETING: "creating a marketing follow-up",
        WorkflowDecision.Department.SUPPORT: "creating a support ticket",
        WorkflowDecision.Department.SALES: "creating a sales task",
        WorkflowDecision.Department.TECHNICAL: "creating a technical task",
        WorkflowDecision.Department.FINANCE: "creating a finance task",
    }
    action = department_actions[decision.department]
    print(
        f"Routing {decision.customer_reference} to the "
        f"{decision.department.value} department: {action}."
    )
    return "automatic_action"

if __name__ == "__main__":
    try:
        decision = validate_output(Output.VALID.value)
    except json.JSONDecodeError as e:
        print(f"Error parsing model output: {e}")
    except ValidationError as e:
        print(f"Schema validation error: {e}")
    except ValueError as e:
        print(f"Business rule validation error: {e}")
    else:
        route_workflow(decision)