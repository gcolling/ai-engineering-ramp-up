from structured_output_lab import validate_output, TicketClassification, Response

def test_validate_output_with_valid_data():
    output = Response.VALID.value
    assert validate_output(output)

def test_validate_malformed_output():
    output = Response.MALFORMED.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for malformed output"
    except ValueError as e:
        assert "Expecting" in str(e)

def test_validate_with_missing_field():
    output = Response.MISSING_FIELD.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for missing field"
    except ValueError as e:
        assert "Field required" in str(e)

def test_validate_with_invalid_enum():
    output = Response.INVALID_ENUM.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for invalid enum"
    except ValueError as e:
        assert "Input should be" in str(e)

def test_validate_with_wrong_field_type():
    output = Response.WRONG_FIELD_TYPE.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for wrong field type"
    except ValueError as e:
        assert "valid number" in str(e)

def test_validate_with_confidence_out_of_range():
    output = Response.CONFIDENCE_OUT_OF_RANGE.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for confidence out of range"
    except ValueError as e:
        assert "less than or equal to 1" in str(e)

def test_validate_with_low_confidence():
    output = Response.LOW_CONFIDENCE.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for low confidence"
    except ValueError as e:
        assert "confidence must be greater than or equal to 0.7" in str(e)

def test_validate_with_unknown_extra_field():
    output = Response.UNKNOWN_FIELD.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for unknown extra field"
    except ValueError as e:
        assert "Extra inputs are not permitted" in str(e)

def test_validate_business_rule_violation():
    output = Response.SEMANTICALLY_INVALID.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for business rule violation"
    except ValueError as e:
        assert "Business rule violation" in str(e)

def test_validate_with_empty_response():
    output = Response.EMPTY.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for empty response"
    except ValueError as e:
        assert "Field required" in str(e)

def test_validate_with_null_response():
    output = Response.NULL.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for null response"
    except ValueError as e:
        assert "Expecting value" in str(e)

def test_validate_with_very_long_reason():
    output = Response.VERY_LONG_REASON.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for very long reason"
    except ValueError as e:
        assert "at most 100 characters" in str(e)

def test_validate_with_unexpected_unicode_characters():
    output = Response.UNEXPECTED_UNICODE.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for unexpected unicode characters"
    except ValueError as e:
        assert "String should match pattern" in str(e)

def test_validate_with_duplicate_fields():
    output = Response.DUPLICATE_FIELDS.value
    try:
        validate_output(output)
        assert False, "Expected ValueError for duplicate fields"
    except ValueError as e:
        assert "duplicate fields" in str(e)