
from agents.advisor import client


def tax_advice(salary, deductions):

    prompt = f"""
You are an Indian tax advisor.

User Salary: ₹{salary}
Existing Deductions: ₹{deductions}

Explain:

1. Which tax regime may be better (Old vs New)
2. Tax saving options under 80C
3. Suggestions to reduce tax

Give 5 simple bullet points.
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
        return "Tax AI service unavailable."

