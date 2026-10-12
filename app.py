
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Firmable Sales Intelligence",
    page_icon="🔎",
    layout="wide"
)

st.title("Firmable Cybersecurity Sales Intelligence")
st.caption("Explore organization-level infrastructure signals for further research.")

# Look for the CSV in the same directory as this app.py file
BASE_DIR = Path(__file__).resolve().parent
SCORE_PATH = BASE_DIR / "firmable_prospect_scores.csv"

# Diagnostic details help identify deployment path issues
if not SCORE_PATH.exists():
    st.error("The organization score CSV was not found.")
    st.write("Expected file location:", str(SCORE_PATH))
    st.write("App directory contents:", [p.name for p in BASE_DIR.iterdir()])
    st.stop()

@st.cache_data
def load_scores(path):
    return pd.read_csv(path, low_memory=False)

scores = load_scores(str(SCORE_PATH))

st.success("Organization scores loaded successfully.")

c1, c2 = st.columns(2)
c1.metric("Organizations scored", f"{len(scores):,}")

if "provider_review_flag" in scores.columns:
    provider_count = (
        scores["provider_review_flag"]
        .fillna(False)
        .astype(str)
        .str.lower()
        .isin(["true", "1"])
        .sum()
    )
    c2.metric("Flagged for provider review", f"{provider_count:,}")

st.subheader("Search organizations")
search = st.text_input("Search by organization name")

results = scores.copy()

if search:
    results = results[
        results["organization_name"].astype(str).str.contains(
            search, case=False, na=False, regex=False
        )
    ]

if "prospecting_research_score" in results.columns:
    results = results.sort_values(
        "prospecting_research_score", ascending=False
    )

st.dataframe(results.head(500), use_container_width=True)

st.download_button(
    "Download search results",
    data=results.to_csv(index=False).encode("utf-8"),
    file_name="firmable_search_results.csv",
    mime="text/csv"
)

st.info(
    "Scores are exploratory research-prioritization heuristics. "
    "Network observations alone do not prove buying intent or confirm a vulnerability."
)

