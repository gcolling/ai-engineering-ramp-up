# QA on AI

Imagine someone tells you: **"We tested our AI assistant with 20 questions and all 20 worked."**

As a QA engineer, what questions would you ask? And what's their purpose?

---

1. Have you re-tested the same questions at least a couple of times? The goal is to identify how solid the behavior and knowledge base of the AI assistant actually is. Passing once can be pure luck, but isn't really a sign of consistency. If to user 1 it says ABC, but to user 2 it says XYZ instead, that is a big flaw.
2. Have you asked questions about information the assistant didn't have access to? Understand if the AI "knows" how to say "I don't know" instead of forging information simply to fill the gaps.
3. Have you tested presenting yourself with a name/role other than your own? The AI application must not simply believe what the user is saying, but be able to verify that information using guardrails for both the input and output, thus avoiding sharing information or accepting requests it should not.
4. Have you tried inputting new information as a source of truth, asking the LLM to update it's sources based on that? The AI shouldn't simply take new information from anyone just because they said so.
5. Have you asked the AI assistant to do things you know for a fact it cannot? If the application is supposed to impede things such as "web search", the agent should respect that.
6. Have you tried sending exceptionally long inputs? The idea is to test whether the AI remains consistent on its answers with long contexts or starts hallucinating more.
7. Have you confronted the AI assistant or asked it to tell you how it works? The system shouldn't be giving away it's own directives to any user. They are system-side, invisible to the users, and should remain so.
8. Have you tried asking the AI what it can or cannot do? To verify it's awareness and adherence to the system rules. It can share it's capabilities so the user knows how to use them, but cannot share confidential information or configurations.
9. Have you tried sending all the requests at the same time? Trying to identify how the system responds and how it handles concurrent requests performance-wise.
10. Have you tried asking vague/ambiguous questions? Verify if the AI "knows it isn't sure", but can share that along the multiple answer options it has found (if so intended), if any.
