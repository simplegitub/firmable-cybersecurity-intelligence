import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Firmable Cybersecurity Intelligence",
    page_icon="🔎",
    layout="wide"
)

DATA_PATH = "/content/firmable_working_dataset.csv"
SCORE_PATH = "/content/firmable_prospect_scores.csv"

st.title("Firmable Cybersecurity Sales Intelligence")
st.caption(
    "Explore observed internet-facing infrastructure signals "
    "to support further company research."
)

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH, low_memory=False)
    scores = pd.read_csv(SCORE_PATH, low_memory=False)
    return data, scores

if not os.path.exists(DATA_PATH) or not os.path.exists(SCORE_PATH):
    st.error("Required dataset or score file is missing.")
    st.stop()

data, scores = load_data()

# Normalize organization names for joining
data["org_key"] = (
    data["org"].fillna("").astype(str).str.lower().str.strip()
)
scores["organization_name"] = (
    scores["organization_name"].fillna("").astype(str)
)

st.metric("Network records loaded", f"{len(data):,}")
st.metric("Organizations scored", f"{len(scores):,}")

st.subheader("Organization research explorer")

search = st.text_input("Search organization name")
results = scores.copy()

if search:
    results = results[
        results["organization_name"].str.contains(
            search, case=False, na=False, regex=False
        )
    ]

sort_options = [
    "prospecting_research_score",
    "unique_ips",
    "unique_ports",
    "expired_cert_records",
    "vuln_metadata_records"
]
available_sorts = [c for c in sort_options if c in results.columns]
sort_by = st.selectbox("Sort results by", available_sorts)

if sort_by in results.columns:
    results = results.sort_values(sort_by, ascending=False)

st.dataframe(results.head(200), use_container_width=True)

st.download_button(
    "Download displayed organization results",
    data=results.to_csv(index=False).encode("utf-8"),
    file_name="firmable_organization_results.csv",
    mime="text/csv"
)

st.subheader("Inspect observed records")

if "organization_name" in scores.columns:
    selected_org = st.selectbox(
        "Select an organization",
        scores["organization_name"].dropna().sort_values().unique()
    )

    matching = data[
        data["org"].fillna("").astype(str).str.strip().str.lower()
        == selected_org.strip().lower()
    ]

    st.write(f"Observed records for **{selected_org}**: {len(matching):,}")

    detail_columns = [
        "org", "ip_str", "port", "domains", "timestamp",
        "location.country_name", "location.city",
        "ssl.cert.expired", "http.title", "http.server",
        "opts.vulns"
    ]
    detail_columns = [c for c in detail_columns if c in matching.columns]
    st.dataframe(
        matching[detail_columns].head(100),
        use_container_width=True
    )

st.info(
    "Interpretation note: these scores are exploratory research-prioritization "
    "heuristics. Network observations do not establish buying intent, "
    "confirmed vulnerability, or an organization's willingness to purchase."
)
