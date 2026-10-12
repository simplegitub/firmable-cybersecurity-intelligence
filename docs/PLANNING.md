# Project Planning — Firmable Cybersecurity Sales Intelligence

## 1. Project objective

Build a data-driven research platform that summarizes organization-level internet infrastructure observations and helps analysts prioritize organizations for further investigation.

The platform is designed to support research, not to predict purchasing intent or confirm security vulnerabilities.

## 2. Problem statement

Raw internet scan data can contain many records for the same organization. Reviewing these records individually makes it difficult to compare organizations and identify useful signals.

This project processes scan records into organization-level summaries and presents the results through a searchable web application.

## 3. Data engineering workflow

1. Download the supplied dataset.
2. Decompress and parse the source records.
3. Flatten nested fields into a tabular structure.
4. Clean and normalize organization names.
5. Aggregate records by organization.
6. Calculate exploratory research-prioritization scores.
7. Generate evaluation outputs from manually labelled examples.
8. Display the results in a Streamlit application.

## 4. Technology stack

- **Python:** Data processing and evaluation.
- **Pandas:** Data transformation, aggregation, and CSV handling.
- **Streamlit:** Interactive web application.
- **GitHub:** Source control, versioned assets, and documentation.
- **Streamlit Community Cloud:** Application hosting.

## 5. Deliverables

- Deployed Streamlit application.
- Organization-level prospecting score dataset.
- Reusable research skill documentation.
- Versioned analysis prompt.
- Labelled evaluation dataset and evaluation script.
- Evaluation results and limitations.
- Architecture documentation and build reflection.

## 6. Risks and limitations

- Shared infrastructure can make organization-level signals difficult to interpret.
- Organization-name normalization may merge distinct entities.
- The initial labelled evaluation sample is small and imbalanced.
- The current heuristic has not been validated against confirmed sales outcomes.
- Scan observations alone cannot establish buying intent or prove an exploitable vulnerability.

## 7. Completion criteria

The project is ready for review when the hosted application works, the source files are available in GitHub, the evaluation script can be run using the committed labelled dataset, and the documentation explains the system and its limitations.

## 8. Future work

- Expand the evaluation dataset and improve label consistency.
- Add automated data-quality checks.
- Track score changes between versions.
- Introduce structured application logging and execution metrics.
- Evaluate alternative scoring methods against a more representative labelled dataset.
