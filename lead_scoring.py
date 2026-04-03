import pandas as pd

df = pd.read_csv("data/leads.csv")

def score_lead(row):
    score = 0

    # Numerical
    score += row['website_visits'] * 2
    score += row['engagement_score'] * 5

    # Intent signal
    if row['pricing_page'] == 1:
        score += 30

    return min(score, 100)

df['score'] = df.apply(score_lead, axis=1)

# Categorize
df['category'] = df['score'].apply(lambda x: "High" if x>70 else "Medium" if x>40 else "Low")

print(df)

print(df.to_json(orient="records", indent=2))