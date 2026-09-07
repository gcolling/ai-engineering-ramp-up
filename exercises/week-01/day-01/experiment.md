# Experiment A - Same question, different context

Three prompts with different context are available, as follows:

**A**

```
What is the vacation policy?
```

**B**

```
You are an HR assistant.

What is the vacation policy?
```

**C**

```
You are an HR assistant.

Company policy:
Employees receive 25 vacation days per year.

What is the vacation policy?
```

---

Questions:

1. What information does the model have in each case?
2. Which answer is likely to be most reliable?
3. What happens if the supplied policy is wrong?
4. What happens if two conflicting policies are supplied?
5. Does adding context guarantee correctness?

---

Answers:

1. Scenario A has just the user input. Scenario B has the user input as well as the developer prompt. And scenario C has the developer prompt, which includes a policy (could be a document), and the user input.
2. Option C is supposedly the most reliable, assuming the provided data is correct, because it has a base knowledge, persona, and a direction to answer.
3. In this case, the wrong information given with no extra instructions or guardrails will be provided to the user.
4. The probabilistic model will evaluate which of the policies is more likely to be the "correct" (even if not true) answer and reply with it, or possibly it will say there are conflicting data and provide both.
5. Not necessarily. If the context itself is wrong, the information provided based on it will also be the wrong one. The AI has no way of knowing (nor is it its job) what is the truth, unless told so.
