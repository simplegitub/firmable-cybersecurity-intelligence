# Firmable Cybersecurity Sales Intelligence Platform

## Overview

This project is a cybersecurity sales intelligence prototype designed to help prioritize organizations for further prospecting research using internet-exposure metadata.

It processes organization-level signals from a dataset and presents a searchable prospecting research score through a Streamlit application.

**Important:** The score is an exploratory prioritization heuristic. It does not represent confirmed buying intent, prove that an organization is vulnerable, or establish that it is a suitable sales prospect.

## Application

The Streamlit application provides:

- Organization-level prospecting research scores
- Searchable organization records
- Infrastructure-provider flags for additional review
- Summary metrics and a downloadable CSV
- A simple interface for exploring results

**Live application:** Add your deployed Streamlit URL here.

## Project Workflow

1. **Data ingestion:** Read internet-exposure metadata from the source dataset.
2. **Data preparation:** Normalize organization names and aggregate records.
3. **Feature engineering:** Calculate signals such as unique IP addresses, unique ports, expired-certificate observations, vulnerability-metadata observations, and country coverage.
4. **Scoring:** Combine the signals into a heuristic research-prioritization score.
5. **Exploration:** Display the resulting CSV in a Streamlit application.
6. **Evaluation:** Compare scores against a small manually labelled evaluation sample and document limitations.

## Technology Stack

- Python
- Pandas
- Streamlit
- CSV-based data processing
- GitHub
- Streamlit Community Cloud

## Scoring and Limitations

The prototype uses weighted signals to help identify organizations for further research. The resulting score is not a calibrated probability or a validated measure of sales readiness.

Infrastructure providers and hosting companies may receive high scores because of their scale and network characteristics. These organizations may require additional review rather than automatic prioritization.

The evaluation sample contains 25 manually labelled examples: 22 labelled `LOW PRIORITY` and 3 labelled `REVIEW`. The initial evaluation showed similar mean scores for these groups, indicating that the current heuristic does not clearly separate them. The sample is small and does not establish predictive accuracy.

See [Evaluation Results](evals/RESULTS.md) for details.

## Repository Structure

```text
.
├── app.py
├── requirements.txt
├── firmable_prospect_scores.csv
├── skills/
│   └── prospecting-research/
│       └── SKILL.md
├── prompts/
│   └── prospecting_analysis/
│       └── v1.md
├── evals/
│   ├── README.md
│   ├── evaluate.py
│   ├── firmable_eval_labeled.csv
│   └── RESULTS.md
└── docs/
    ├── PLANNING.md
    ├── ARCHITECTURE.md
    ├── HOW_YOU_BUILD.md
    └── OBSERVABILITY.md
```

## Run Locally

1. Install Python.
2. Clone this repository.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the application:

```bash
streamlit run app.py
```

The application uses the prospect scores CSV included in the repository. The original large source dataset is not included in GitHub.

## Evaluation

The evaluation harness is available at `evals/evaluate.py`. It validates the evaluation input and generates descriptive results and summary files.

Run it from the repository root:

```bash
python evals/evaluate.py
```

The evaluation is intended to support transparency and reproducibility, not to claim model accuracy.

## Documentation

- [Project Planning](docs/PLANNING.md)
- [Architecture](docs/ARCHITECTURE.md)
- [How the Project Was Built](docs/HOW_YOU_BUILD.md)
- [Observability and Cost Monitoring](docs/OBSERVABILITY.md)
- [Prospecting Research Skill](skills/prospecting-research/SKILL.md)
- [Versioned Analysis Prompt](prompts/prospecting_analysis/v1.md)
- [Evaluation Framework](evals/README.md)
- [Evaluation Results](evals/RESULTS.md)

## Responsible Use

Use these scores only as preliminary research signals. Verify findings with reliable sources before contacting an organization or making business decisions. Do not treat metadata observations as confirmation of an active vulnerability or a company's purchasing intent.
