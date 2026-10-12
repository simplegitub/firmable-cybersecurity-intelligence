
import json
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "firmable_eval_labeled.csv"

RESULTS_FILE = BASE_DIR / "firmable_eval_results.csv"
SUMMARY_FILE = BASE_DIR / "firmable_eval_summary.csv"
REPORT_FILE = BASE_DIR / "firmable_eval_report.json"

REQUIRED_COLUMNS = [
    "organization_name",
    "prospecting_research_score",
    "human_label",
]


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Evaluation dataset not found: {INPUT_FILE}\n"
            "Place firmable_eval_labeled.csv inside the evals/ folder."
        )

    df = pd.read_csv(INPUT_FILE)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["human_label"] = (
        df["human_label"]
        .fillna("")
        .astype(str)
        .str.strip()
        .str.upper()
        .str.replace(" ", "_", regex=False)
    )

    df["prospecting_research_score"] = pd.to_numeric(
        df["prospecting_research_score"], errors="coerce"
    )

    df = df[df["human_label"] != ""].copy()

    if df.empty:
        raise ValueError("No labelled evaluation examples were found.")

    summary = (
        df.groupby("human_label")["prospecting_research_score"]
        .agg(["count", "mean", "min", "max"])
        .reset_index()
        .rename(
            columns={
                "human_label": "label",
                "count": "example_count",
                "mean": "mean_score",
                "min": "min_score",
                "max": "max_score",
            }
        )
        .round(2)
    )

    df.to_csv(RESULTS_FILE, index=False)
    summary.to_csv(SUMMARY_FILE, index=False)

    label_counts = {
        str(label): int(count)
        for label, count in df["human_label"].value_counts().items()
    }

    report = {
        "evaluation_version": "1.0.0",
        "evaluation_examples": int(len(df)),
        "label_counts": label_counts,
        "mean_score_by_label": {
            str(row["label"]): (
                float(row["mean_score"])
                if pd.notna(row["mean_score"])
                else None
            )
            for _, row in summary.iterrows()
        },
        "interpretation": (
            "Descriptive comparison only. Similar group scores do not "
            "demonstrate that the heuristic distinguishes the labels."
        ),
        "limitations": [
            "Small, manually labelled evaluation sample.",
            "Initial sample has no RESEARCH-labelled examples.",
            "Manual labels are not confirmed sales outcomes.",
            "Scores are heuristics, not probabilities of buying intent.",
        ],
    }

    REPORT_FILE.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"Evaluation examples: {len(df)}")
    print("\nScore summary:")
    print(summary.to_string(index=False))
    print(f"\nSaved: {RESULTS_FILE.name}")
    print(f"Saved: {SUMMARY_FILE.name}")
    print(f"Saved: {REPORT_FILE.name}")


if __name__ == "__main__":
    main()
