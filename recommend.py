import pandas as pd

# Load CSV
data = pd.read_csv("data.csv")

# ---------------- CLEANING ----------------

# Remove newline from column names
data.columns = data.columns.str.replace("\n", " ", regex=False)
data.columns = data.columns.str.strip()

# Clean text columns
data["PLACE"] = data["PLACE"].astype(str).str.strip().str.upper()
data["INSTITUTE NAME"] = data["INSTITUTE NAME"].astype(str).str.strip()
data["BRANCH NAME"] = data["BRANCH NAME"].astype(str).str.strip()

# Convert numeric columns
for col in data.columns:
    if any(x in col for x in ["BOYS", "GIRLS", "EWS", "FEE"]):
        data[col] = pd.to_numeric(data[col], errors="coerce")

# ---------------- RECOMMEND FUNCTION ----------------

def recommend_colleges(rank, budget, location, category, gender):

    location = location.strip().upper()

    # Decide correct cutoff column
    if category == "EWS":
        cutoff_column = "EWS GEN OU"
    else:
        cutoff_column = f"{category} {'BOYS' if gender == 'Male' else 'GIRLS'}"

    if cutoff_column not in data.columns:
        return pd.DataFrame()

    filtered = data[
        (rank <= data[cutoff_column]) &
        (data["TUITION FEE"] <= budget)
    ]

    if location:
        filtered = filtered[
            filtered["PLACE"].str.contains(location, na=False)
        ]

    if filtered.empty:
        return filtered

    # Ranking score (closer cutoff is better)
    filtered["Score"] = filtered[cutoff_column] - rank
    filtered = filtered.sort_values("Score")

    return filtered[
        [
            "INSTITUTE NAME",
            "BRANCH NAME",
            "PLACE",
            "TUITION FEE",
            cutoff_column
        ]
    ].head(10)