
from agents.advisor import client


def life_event_advice(event, income, savings, debt):

    prompt = f"""
You are an expert Indian financial planner.

User Details:
Monthly Income: ₹{income}
Current Savings: ₹{savings}
Existing Debt: ₹{debt}

Life Event: {event}

Give 5 short financial suggestions for handling this event.
Keep it simple and beginner friendly.
Use bullet points.
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
        return "AI advice temporarily unavailable."

