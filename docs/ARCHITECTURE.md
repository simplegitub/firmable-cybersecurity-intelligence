# System Architecture — Firmable Cybersecurity Sales Intelligence

## 1. Overview

The platform transforms raw internet scan observations into organization-level research-prioritization scores and presents those results through a deployed Streamlit application.

## 2. Architecture flow

```text
Supplied Internet Scan Dataset
              |
              v
     Download and Decompression
              |
              v
      Python / Pandas Processing
              |
              v
     Flatten and Normalize Data
              |
              v
     Organization-Level Aggregation
              |
              v
      Research-Prioritization Scores
              |
              v
      CSV Score Dataset
              |
              v
       Streamlit Web Application
              |
              v
     Search, Review, and CSV Export
```

## 3. Data processing

The source data contains nested internet scan observations. The processing workflow extracts relevant fields, including organization names, IP addresses, ports, timestamps, certificate metadata, and vulnerability metadata.

Organization names are normalized for aggregation. The resulting organization-level dataset contains summary signals and an exploratory research-prioritization score.

## 4. Scoring approach

The baseline heuristic combines percentile-based signals for:

- Unique IP addresses
- Unique ports
- Expired certificate observations
- Vulnerability metadata observations
- Number of observed countries

The resulting score is intended to prioritize further research. It is not a probability of purchasing intent, a security-risk rating, or proof of a vulnerability.

Infrastructure-provider indicators are used as a reason for additional review rather than as evidence of buying intent.

## 5. Application layer

The Streamlit application loads the committed organization score CSV from the repository. Users can search for organizations, review available signals and scores, inspect the results table, and download filtered results.

The application is hosted using Streamlit Community Cloud, with the source code maintained in GitHub.

## 6. Evaluation architecture

The evaluation workflow uses a manually labelled CSV and a Python script to produce grouped score summaries and a JSON report.

The initial evaluation includes 25 examples: 22 `LOW_PRIORITY` and 3 `REVIEW`. The small and imbalanced sample limits the conclusions that can be drawn.

## 7. Reliability and observability

The evaluation script checks required columns and missing labels. Application testing should cover successful file loading, organization search, displayed scores, and CSV download.

Future improvements include structured application logs, error tracking, run identifiers, data-quality metrics, and monitoring of execution time and resource use.

No LLM API is required by the current deployed application. Therefore, LLM token costs are not currently part of its runtime cost.

## 8. Security and data handling

- Do not commit API keys, passwords, or access tokens.
- Avoid uploading the large raw dataset to a public repository.
- Confirm that any published data can be shared under the applicable dataset terms.
- Treat scan metadata as observational evidence rather than confirmed security findings.

## 9. Known limitations

- Shared infrastructure may affect organization-level counts.
- Name normalization may merge distinct entities.
- The baseline score has not been validated against confirmed sales outcomes.
- The current evaluation dataset needs more representative examples.

## 10. Future architecture improvements

- Automated ingestion and repeatable data validation.
- Versioned scoring configuration.
- More balanced evaluation data.
- Structured logging and performance metrics.
- Scheduled refreshes and reproducible pipeline runs.
