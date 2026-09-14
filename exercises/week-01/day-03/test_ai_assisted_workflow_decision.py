import pytest

from ai_assisted_workflow_decision import (
	Output,
	WorkflowDecision,
	route_workflow,
	validate_output,
)

def test_validate_output_with_valid_data():
	decision = validate_output(Output.VALID.value)

	assert isinstance(decision, WorkflowDecision)
	assert decision.intent == WorkflowDecision.Intent.REFUND
	assert decision.department == WorkflowDecision.Department.SUPPORT
	assert decision.requires_human_review is False


def test_validate_malformed_output():
	with pytest.raises(ValueError, match="Expecting"):
		validate_output(Output.MALFORMED.value)


def test_validate_with_missing_field():
	with pytest.raises(ValueError, match="Field required"):
		validate_output(Output.MISSING_FIELD.value)


def test_validate_with_invalid_enum():
	with pytest.raises(ValueError, match="Input should be"):
		validate_output(Output.INVALID_ENUM.value)


def test_validate_with_wrong_field_type():
	with pytest.raises(ValueError, match="valid number"):
		validate_output(Output.WRONG_FIELD_TYPE.value)


def test_validate_human_review_required_output():
	decision = validate_output(Output.HUMAN_REVIEW_REQUIRED.value)

	assert decision.requires_human_review is True


def test_validate_refund_finance_business_rule():
	with pytest.raises(ValueError, match="Finance department cannot process refund"):
		validate_output(Output.REFUND_FINANCE.value)


def test_validate_with_extra_field():
	with pytest.raises(ValueError, match="Extra inputs are not permitted"):
		validate_output(Output.EXTRA_FIELD.value)


def test_validate_with_confidence_out_of_range():
	with pytest.raises(ValueError, match="less than or equal to 1"):
		validate_output(Output.CONFIDENCE_OUT_OF_RANGE.value)


def test_validate_with_very_long_reason():
	with pytest.raises(ValueError, match="at most 200 characters"):
		validate_output(Output.VERY_LONG_REASON.value)


def test_validate_with_invalid_customer_reference():
	with pytest.raises(ValueError, match="String should match pattern"):
		validate_output(Output.INVALID_CUSTOMER_REFERENCE.value)


def test_validate_with_duplicate_fields():
	with pytest.raises(ValueError, match="duplicate fields"):
		validate_output(Output.DUPLICATE_FIELDS.value)


def test_validate_business_rule_for_marketing_review():
	with pytest.raises(ValueError, match="Marketing department cannot require human review"):
		validate_output(Output.SEMANTICALLY_INVALID.value)


def test_validate_business_rule_for_low_confidence():
	with pytest.raises(ValueError, match="confidence must be greater than or equal to 0.7"):
		validate_output(Output.LOW_CONFIDENCE.value)


def test_validate_business_rule_for_address_update_department():
	with pytest.raises(ValueError, match="Address update requests must be handled"):
		validate_output(Output.ADDRESS_UPDATE_WRONG_DEPARTMENT.value)


def test_validate_business_rule_for_plan_change_department():
	with pytest.raises(ValueError, match="Plan change requests must be handled"):
		validate_output(Output.PLAN_CHANGE_WRONG_DEPARTMENT.value)


def test_validate_business_rule_for_account_deletion_department():
	with pytest.raises(ValueError, match="Account deletion requests must be handled"):
		validate_output(Output.ACCOUNT_DELETION_WRONG_DEPARTMENT.value)


def test_validate_confidence_boundary():
	decision = validate_output(Output.CONFIDENCE_BOUNDARY.value)

	assert decision.confidence == 0.7


def test_route_workflow_to_automatic_action():
	decision = validate_output(Output.VALID.value)

	assert route_workflow(decision) == "automatic_action"


def test_route_workflow_prints_department_action(capsys):
	decision = validate_output(Output.VALID.value)

	route_workflow(decision)

	assert capsys.readouterr().out == (
		"Routing C123456 to the support department: creating a support ticket.\n"
	)



@pytest.mark.parametrize(
	("output", "expected_action"),
	[
		(Output.AUTOMATIC_MARKETING, "creating a marketing follow-up"),
		(Output.AUTOMATIC_ADDRESS_UPDATE, "creating a support ticket"),
		(Output.AUTOMATIC_PLAN_CHANGE, "creating a sales task"),
		(Output.AUTOMATIC_ACCOUNT_DELETION, "creating a technical task"),
	]
)
def test_route_workflow_prints_action_for_each_reachable_department(
	output, expected_action, capsys
):
	decision = validate_output(output.value)

	assert route_workflow(decision) == "automatic_action"
	assert capsys.readouterr().out == (
		f"Routing C123456 to the {decision.department.value} department: {expected_action}.\n"
	)


def test_route_workflow_to_human_review():
	decision = validate_output(Output.HUMAN_REVIEW_REQUIRED.value)

	assert route_workflow(decision) == "human_review"


def test_route_workflow_prints_human_review_details(capsys):
	decision = validate_output(Output.HUMAN_REVIEW_REQUIRED.value)

	route_workflow(decision)

	assert capsys.readouterr().out == (
		"Routing C123456 to human review because: "
		"Customer requests a refund for a defective product.\n"
	)
