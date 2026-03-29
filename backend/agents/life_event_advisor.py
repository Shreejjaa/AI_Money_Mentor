
from agents.advisor import client

def life_event_advice(event, income, savings, debt):

    prompt = f"""
You are an expert Indian financial planner.

Analyze the user's financial situation and provide clear, actionable advice for a specific life event.

-------------------------
USER FINANCIAL DETAILS
-------------------------
• Monthly Income: ₹{income}
• Current Savings: ₹{savings}
• Existing Debt: ₹{debt}

-------------------------
LIFE EVENT
-------------------------
• Event: {event}
"""
    # ===== BASIC CALCULATIONS (SMART TOUCH) =====
    emergency_fund = income * 3
    savings_ratio = (savings / income * 100) if income > 0 else 0

    prompt = f"""
You are an expert Indian financial planner.

Analyze the user's financial situation and provide clear, actionable advice for a specific life event.

-------------------------
USER FINANCIAL DETAILS
-------------------------
• Monthly Income: ₹{income}
• Current Savings: ₹{savings}
• Existing Debt: ₹{debt}

-------------------------
LIFE EVENT
-------------------------
• Event: {event}

-------------------------
OUTPUT REQUIREMENTS
-------------------------
• Give EXACTLY 5 bullet points.
• Each bullet should be 1–2 lines, simple and beginner-friendly.
• Focus on practical steps for savings, investments, emergency fund, debt management, and risk.
• Do not add any extra text or greetings.
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",   # safer model
            contents=prompt
        )

        advice = response.text.replace("*", "")
        
        lines = [f"• {line.strip()}" for line in advice.split("\n") if line.strip()]
        final_advice = "<br>".join(lines)

    except Exception as e:
        print("AI ERROR:", e)

        final_advice = """
• Build an emergency fund covering at least 3–6 months of expenses.
• Allocate 20–30% of income towards investments.
• Reduce any high-interest debt before investing aggressively.
• Maintain a balanced mix of savings and long-term investments.
• Review your financial plan quarterly.
"""

    return final_advice