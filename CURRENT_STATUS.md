# Current Status

## Program

Duration: 9 weeks

Expected workload: approximately 15 hours/week

Typical study session: approximately 3 hours

## Current position

Phase: 1 — AI Application Foundations

Week: 1

Day: 3

Current module: Structured Outputs and Validation

## Time

Target this week: approximately 15 hours

Completed this week: approximately 9 hours

## Completed

- CV repositioning
- LinkedIn repositioning
- GitHub training environment setup
- Local development environment setup
- ChatGPT training workspace setup
- Week 1 Day 1 — LLM application mental model
- Week 1 Day 2 — Prompt and context engineering
- Week 1 Day 3 — Structured outputs and validation

## Currently working on

- None

## Blocked

None

## Current questions

None

## Skills recently covered

### LLM application foundations

- LLM vs. LLM application
- Tokens
- Context
- Inference
- Probabilistic generation
- Prompt/context influence
- Hallucination mechanisms
- Responsibilities outside the LLM
- AI-specific testing considerations

### Prompt and context engineering

- Context construction
- Context minimization
- Context management
- Direct and indirect prompt injection
- Untrusted content
- Trust and authority boundaries
- Deterministic application controls
- Authentication and authorization outside the LLM
- Context handling for retrieved documents and tool results

### Structured outputs and validation

- Structured output contracts
- JSON parsing
- Schema validation
- Business validation
- Validation failure classes
- Cross-field business rules
- Range and threshold validation
- State-dependent validation
- Human-review routing
- Validated AI output as a workflow input

## Projects

No portfolio projects started yet.

## Next

Week 1 Day 4 — Tool and Function Calling Fundamentals

## Learning observations

Week 1 has established the core application boundary around an LLM:

context is engineered before inference, and model output must be
validated before it can influence application behavior.

Day 3 added the distinction between structural validity and business
validity, reinforcing that a structurally valid model response is not
automatically a correct or safe application decision.

## Git workflow

branch → implementation → tests → commit → push → pull request →
review → merge.
