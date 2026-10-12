# Prospecting Research Skill

**Version:** 1.0.0  
**Purpose:** Organize organization-level internet infrastructure observations into a transparent research-prioritization workflow.

## When to use this skill

Use this workflow when reviewing organization-level records derived from internet scan data and deciding which organizations may need further manual research.

## Inputs

The workflow may use:

- Organization name
- Record count
- Unique IP addresses and ports
- Expired certificate observations
- Vulnerability metadata observations
- Country and infrastructure-provider indicators

## Workflow

1. Inspect and validate the input data.
2. Normalize organization names while preserving the original names.
3. Aggregate infrastructure observations by normalized organization.
4. Identify possible infrastructure providers for manual review.
5. Calculate a research-prioritization score using the documented heuristic.
6. Display scores and supporting signals in the Streamlit application.
7. Record evaluation results and known limitations.

## Interpretation rules

- A higher score indicates higher priority for further research under the current heuristic.
- A score is not a probability of buying intent.
- An expired certificate observation does not independently establish a security vulnerability.
- Vulnerability metadata must not be treated as proof of an exploitable vulnerability.
- Infrastructure providers and shared hosting can affect organization-level counts.
- Organization normalization can incorrectly merge distinct entities.

## Quality checks

- Check for missing organization names and invalid numeric values.
- Confirm that aggregate counts are non-negative.
- Review provider flags before interpreting high scores.
- Test organization search and CSV export.
- Record evaluation limitations and investigate unexpected results.

## Output

Produce an organization-level score table with supporting signals, review notes, and a clear warning that the scores are exploratory research heuristics.

## Version history

- **1.0.0:** Initial documented research-prioritization workflow.
