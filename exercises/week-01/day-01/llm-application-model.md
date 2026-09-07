# LLM Recap

## Exercises

### 1. Model vs application

Explain the difference between

```
LLM
```

and

```
LLM application
```

---

### 2. Determinism

Why can a traditional function behave approximately like:

```
same input → same output
```

while an LLM application may behave more like:

```
same input → different plausible outputs
```

### 3. Context

List at least five different things an application might place into an LLM's context.

### 4. Hallucination

Explain why an LLM can produce a convincing answer that is factually wrong.

### 5. Engineering responsibility

Imagine you're building:

```
SAP HR Assistant
```

A user asks:

```
"How many vacation days do I have?"
```

Explain why simply sending the question to an LLM is insufficient.
Think about:

- identity
- data
- retrieval
- authorization
- LLM
- validation
- security

---

## Answers

### 1. Model vs application

| LLM                                                                                                                                                                                                                                                                                                                                                    | LLM application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LLM is the AI itself, the model, the brain. It has been trained based on a huge amount of data so it could receive input information and provide answers based on [tokens](../../../lessons/week-01/day-01.md#tokens) and finding the sequence of them with the highest probability, one-by-one. It "processes" the tokens and outpus a sequence back. | The LLM application, however, is built around the LLM model, providing essencial extra information for it to "understand" things in a certain way and provide more appropriate answers. LLM applications can be compared to backend systems. While the backend has: a client, REST API, processing logic, database, validation and response; the LLM application has: user input, developer/system prompts, context, model, output, validation, business logic, and the final output/response. |

### 2. Determinism

The answer lies on the way both engines work. With regular code, given it stays the same between runs and has the same inputs as well, the deterministic engine will always process the same information in the same way; you input A, the code gives you B. The behavior is consistent.
LLMs are probabilistic engines, meaning that each time they receive a input XYZ, the engine will break it down into tokens, analyze them, and compute weights and probabilities for **each** output token at a time, which then forms the final answer. And that's the catch: probability is a chance, not a guarantee. Even if the input remains the same throughout the tries, both input and output tokens will depend on the probability assigned by the engine, so there's room here for different answers if from one run to another the engine weighs tokens differently.

### 3. Context

1. User input
2. System/Developer prompts
3. Files/documents
4. Tools usage results
5. Conversation history

### 4. Hallucination

The probabilistic engine of the LLM will always analyze the input tokens (context) and try to predict a correct output token-by-token. This means that even if most part of the output is correct, some tokens in it can be just "fillers" added by the AI because they are plausible continuations. LLMs know probabilities and calculations, not necessarily the truth. The hallucinations therefore are the cases in which it would make "probabilistic" sense to group certain tokens together, but they aren't necessarily correct content-wise, be it because the AI doesn't know and is trying to fill in, be it because it was given the wrong information as being true.

### 5. Engineering responsibility

From the user's perspective, that's all they want to know, and that's perfectly fine. However, a proper LLM application should be handling much more than that behind the scenes. Even before touching the LLM layer, the application must identify the user: do we enforce log in for questions? if not, is the user logged in? This is important to determine which kind of data can be processed and which questions can be actually answered in this context, because it touches authorization - a random logged out user cannot be accessing such data.
And moving forward, assuming the user is indeed authenticated and authorized to access vacation data of their own (the app needs scope check for different scenarios such as managers checking employee vacation alowance for example), the system prompt would be something like:

```
You are an HR assistant. You answer in a calm neutral tone. Only ever answer the specific questions you are asked. <+ guardrails>
```

Meanwhile, the developer prompt could include data already processed by the app's logic, like the user ID the request is for, their role, etc., and instruct the LLM to restrict itself to only that information.
Finally, the system prompt could be passed like:

```
The user asks:
"How many vacation days do I have?"
```

The composite instructions for the agent would then be:

```
System prompt.

Developer prompt.

The user asks:
"How many vacation days do I have?"
```

Any system connections and/or policies can also be specified. For this example, the developer prompt could also include **"Use the 'SAP Connector' to retrieve the data"**.
Guardrails and validations on both final input and the AI's output can help catch misbehaviors or malicious intent, and prevent sharing such output to the user.
