
import pandas as pd
from agents.advisor import client


def analyze_budget(file):

    df = pd.read_csv(file)

    total_spending = df["amount"].sum()

    category_summary = df.groupby("category")["amount"].sum().to_dict()

    prompt = f"""
You are a financial advisor.

Here is the user's monthly spending data.

Total Spending: ₹{total_spending}

Category Breakdown:
{category_summary}

Analyze the spending and give 5 short suggestions to improve budgeting.
Avoid technical jargon.
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        advice = response.text

        advice = advice.replace("*", "")
        lines = advice.split("\n")

        clean = []
        for line in lines:
            line = line.strip()
            if line:
                clean.append("• " + line)

        advice = "<br>".join(clean)

    except Exception:
        advice = "AI analysis temporarily unavailable."

    return {
        "total_spending": total_spending,
        "categories": category_summary,
        "advice": advice
    }
