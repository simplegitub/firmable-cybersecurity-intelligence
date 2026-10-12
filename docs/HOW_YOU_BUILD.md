# How I Built the Firmable Cybersecurity Sales Intelligence Platform

## Approach

I approached the assignment as a data engineering and research-prioritization problem. The supplied internet scan dataset contained nested records, so I used Python and Pandas to flatten the data, normalize organization names, aggregate infrastructure observations, and generate organization-level scores.

I then built a Streamlit application to make the summarized data searchable and downloadable. I deployed the application using Streamlit Community Cloud and maintained the application source and supporting documentation in GitHub.

## AI-assisted development

I used AI assistance to break the work into manageable tasks, draft documentation, troubleshoot deployment issues, and create a reproducible evaluation script. I reviewed the generated outputs and used the observed results to identify limitations rather than treating the first scoring approach as proven.

The research skill and analysis prompt are versioned in the repository. The prompt is documented as a reusable asset; it is not represented as a live LLM integration in the deployed application.

## Evaluation and learning

I prepared an initial manually labelled set of 25 organizations: 22 labelled `LOW_PRIORITY` and 3 labelled `REVIEW`.

The average scores of the two groups were very similar. This showed that the current heuristic does not clearly distinguish these labels in the initial sample. The result helped identify the need for more representative evaluation data, consistent labelling criteria, and further scoring experiments.

## Engineering practices

I organized the code, evaluation assets, prompts, and documentation in GitHub. I also documented the workflow, reproducibility instructions, known limitations, and proposed improvements.

The next engineering priorities are to strengthen data-quality checks, expand evaluation coverage, add structured execution logging, and track performance and resource usage.

## Key takeaway

The main lesson was that building a working data application is only part of the task. A dependable data product also needs reproducible processing, transparent scoring, meaningful evaluation, clear documentation, and honest communication about what the data can and cannot establish.
