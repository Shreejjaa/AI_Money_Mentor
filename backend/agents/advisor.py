import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_advice(user_data, plan):

    prompt = f"""
You are an expert Indian financial advisor.

User Financial Data:
Income: ₹{user_data.get('income')}
Expenses: ₹{user_data.get('expenses')}
Debt: ₹{user_data.get('debt')}

Investment Plan:
Monthly SIP: ₹{plan['monthly_sip']}
Equity Allocation: {plan['allocation']['equity']}%
Debt Allocation: {plan['allocation']['debt']}%
Gold Allocation: {plan['allocation']['gold']}%

Provide short bullet-point financial advice (maximum 5 points).
Focus on:
• savings improvement
• investment strategy
• emergency fund
• risk balance
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error generating advice: {str(e)}"