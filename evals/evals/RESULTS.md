# Initial Evaluation Results

**Evaluation version:** 1.0.0  
**Sample size:** 25 manually labelled organization records

## Label distribution

| Human label | Examples |
|---|---:|
| LOW_PRIORITY | 22 |
| REVIEW | 3 |
| **Total** | **25** |

## Score comparison

| Human label | Mean score | Minimum | Maximum |
|---|---:|---:|---:|
| LOW_PRIORITY | 93.34 | 89.3 | 99.9 |
| REVIEW | 93.53 | 89.8 | 97.7 |

## Interpretation

The mean scores for `LOW_PRIORITY` and `REVIEW` are very similar. The current research-prioritization heuristic does not clearly distinguish these two groups in this initial evaluation sample.

This is a descriptive comparison, not a predictive-accuracy measurement.

## Limitations

- The evaluation sample is small and imbalanced.
- No examples are labelled `RESEARCH`.
- Human labels represent review judgements, not verified sales outcomes.
- Infrastructure providers and shared hosting can affect observed counts.
- A high score does not establish buying intent or confirm a vulnerability.

## Next steps

1. Collect additional examples across all intended labels.
2. Define consistent criteria for human labelling.
3. Run the evaluation script reproducibly.
4. Compare results whenever the scoring logic changes.

## Reproducibility

Run the evaluation script from the repository root:

`python evals/evaluate.py`

The script expects `evals/firmable_eval_labeled.csv` and writes the results into the same directory.

The CSV should remain the source of truth for the labelled examples.
