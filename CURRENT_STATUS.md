# Current Status

## Program

Duration: 9 weeks

Expected workload: approximately 15 hours/week

Typical study session: approximately 3 hours

## Current position

Phase: 1 — AI Application Foundations

Week: 1

Day: 4

Current module: Tool and Function Calling Fundamentals

## Time

Target this week: approximately 15 hours

Completed this week: approximately 11 hours

## Completed

- CV repositioning
- LinkedIn repositioning
- GitHub training environment setup
- Local development environment setup
- ChatGPT training workspace setup
- Week 1 Day 1 — LLM application mental model
- Week 1 Day 2 — Prompt and context engineering
- Week 1 Day 3 — Structured outputs and validation
- Week 1 Day 4 — Tool and function calling fundamentals

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

### Tool and function calling

- Tool definitions
- Tool schemas
- Tool selection
- Tool-call request validation
- Tool authorization boundaries
- Deterministic tool execution
- Read-only vs. side-effecting tools
- Tool descriptions
- Mock LLM tool calls
- Local LLM tool calling with Ollama
- Separating provider-specific responses from the application tool layer

## Projects

No portfolio projects started yet.

## Next

Week 1 Day 5 — LLM Foundations Review and Reliability Exercise

## Learning observations

Week 1 has established the core application boundary around an LLM:

context is engineered before inference, model output must be validated
before it can influence application behavior, and tool requests must
pass through deterministic application controls before execution.

Day 4 added the tool boundary: the LLM proposes a tool call, while the
application remains responsible for validation, authorization and
execution.

## Git workflow

branch → implementation → tests → commit → push → pull request → review → merge.
