from agents.advisor import client

def couple_finance_advice(income1, income2, expenses):

    total_income = income1 + income2
    surplus = total_income - expenses

    # Avoid division error
    if total_income == 0:
        ratio1 = ratio2 = 0
    else:
        ratio1 = income1 / total_income
        ratio2 = income2 / total_income

    contrib1 = surplus * ratio1
    contrib2 = surplus * ratio2

    # AI Prompt
    prompt = f"""
You are an expert Indian financial planner advising couples.

Partner 1 Income: ₹{income1}
Partner 2 Income: ₹{income2}
Expenses: ₹{expenses}
Surplus: ₹{surplus}

Give EXACTLY 5 bullet points:
- Include emergency fund, SIP, tax saving (NPS/ELSS), insurance
- Keep simple and practical
- No headings, only bullets
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        advice_text = response.text.replace("*", "")

        lines = [f"• {line.strip()}" for line in advice_text.split("\n") if line.strip()]
        final_advice = "<br>".join(lines)

    except Exception:
        final_advice = "• AI advice unavailable."

    return {
        "total_income": int(total_income),
        "expenses": int(expenses),
        "surplus": int(surplus),

        "contrib1": int(contrib1),
        "contrib2": int(contrib2),

        "ratio1": round(ratio1 * 100),
        "ratio2": round(ratio2 * 100),

        "advice": final_advice
    }