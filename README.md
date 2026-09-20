# Asymmetric Update Governance (AUG)
## Research Question/ Objective

Can a smaller number of model interactions produce reasoning that is comparable to or better than conventional multi-agent debate?

---

## Overview

This project explores an alternative protocol for coordinating multiple large language model agents. Instead of running a longer debate loop, the protocol uses asymmetric critique and revision: one agent produces an initial answer, another agent identifies weaknesses (if there is any) in that answer, and the first agent revises its response based on the critique.

---

## AUG

Asymmetric Update Governance (AUG) uses three model calls:

```text
Agent A₁ → Agent B (critique by presenting weak points in arguments and reasoning) → Agent A₂ (final)
```
The project compares two systems:

- AUG (Asymmetric Update Governance): a three-step process

- MAD (Multi-Agent Debate): a conventional debate-style protocol in which agents continue discussing and revising their positions iteratively

The two systems are tested on a curated set of questions with varying difficulty levels. Each question is answered by both protocols, and the outputs are then evaluated by an independent judge model.

The evaluation focuses on two dimensions:

- Accuracy: how correct the final answer is based on the information available.
- Reasoning quality: how logically sound, relevant, and well-supported the explanation is.

The judge assigns scores from 0 to 10 for each metric. This allows the project to compare the quality of reasoning between AUG and MAD under the same conditions.

---

## Technologies

- Python
- OpenAI Python SDK
- Ollama / local LLM inference
- SQLite
- Prompt-based agent orchestration

---

## Repository Structure

- main.py: implements the AUG protocol
- norMAD.py: implements the conventional MAD baseline
- judge.py: evaluates the outputs produced by both systems
- database.py: stores and loads the benchmark questions
- README.md: project overview and methodology

---

## Limitations

This project is an exploratory prototype and has several limitations:

- The benchmark contains a relatively small number of questions.
- The questions may not represent all types of reasoning tasks.
- The evaluation judge is itself an LLM, so its scores may reflect model preferences as well as correctness.
- Prompt wording and formatting can significantly affect model behavior.
- The current experiment does not provide a broad production-scale benchmark.
- Additional repeated trials would be needed to determine whether observed differences are statistically reliable.
---

## Future Work

- Expand the benchmark set to include more diverse reasoning tasks.
- Compare different model families and parameter settings.
- Introduce stronger statistical comparison across multiple runs.
- Analyze the relationship between interaction count and reasoning quality.
- Improve evaluation robustness by combining LLM judging with human review or rule-based scoring.

---

## Conclusions 

AUG is a prototype protocol for studying how the structure of multi-agent interactions affects reasoning quality. This project provides a framework for comparing the two approaches and not to confidently declare whether one method is better than the other.

Through this project, I independently investigated multi-agent coordination, prompt design, evaluation methodology, and the trade-off between reasoning quality and interaction cost.
