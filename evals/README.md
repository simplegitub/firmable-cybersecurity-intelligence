# Evaluation Framework

## Purpose

This evaluation framework checks whether the organization's research-prioritization heuristic produces useful and interpretable results.

## Evaluation dataset

The initial evaluation set contains 25 manually reviewed organization-level examples.

The labels include:
- `LOW_PRIORITY`
- `REVIEW`

The current sample contains 22 `LOW_PRIORITY` examples and 3 `REVIEW` examples. It does not yet contain examples labelled `RESEARCH`.

## Evaluation approach

The initial evaluation compares research-prioritization scores across the manually assigned labels.

The evaluation outputs include:
- `firmable_eval_labeled.csv` — manually labelled examples.
- `firmable_eval_results.csv` — evaluation records.
- `firmable_eval_summary.csv` — grouped score summary.
- `firmable_eval_report.json` — machine-readable evaluation report.

## Initial findings

The mean score for the `LOW_PRIORITY` group was approximately 93.34, while the mean score for the `REVIEW` group was approximately 93.53.

These similar averages indicate that the current heuristic does not clearly distinguish these groups in the initial sample.

This comparison is descriptive, not a measure of predictive accuracy.

## Limitations

- The evaluation sample is small and imbalanced.
- There are no `RESEARCH` examples in the initial labelled set.
- Labels represent manual review judgements, not confirmed sales outcomes.
- The score is a research-prioritization heuristic, not a buying-intent probability.
- Further examples and clearer labelling criteria are needed before drawing stronger conclusions.

## Next steps

1. Add more examples across all intended labels.
2. Define consistent criteria for each label.
3. Run a reproducible evaluation script.
4. Compare results after changes to the scoring logic.
5. Record evaluation results and limitations for each version.

## Version history

- **1.0.0:** Initial evaluation documentation for the 25-example review set.
