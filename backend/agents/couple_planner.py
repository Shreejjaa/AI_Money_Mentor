
from agents.advisor import client


def couple_finance_advice(income1, income2, expenses):

    total_income = income1 + income2

    prompt = f"""
You are a financial planner helping a couple manage money.

Partner 1 Income: ₹{income1}
Partner 2 Income: ₹{income2}
Combined Monthly Expenses: ₹{expenses}

Combined Income: ₹{total_income}

Give 5 financial suggestions for the couple.
Focus on savings, investment, and tax optimization.
Use simple bullet points.
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        advice = response.text.replace("*", "")

        lines = advice.split("\n")
        clean = []

        for line in lines:
            line = line.strip()
            if line:
                clean.append("• " + line)

        return "<br>".join(clean)

    except Exception:
        return "AI advice unavailable."

