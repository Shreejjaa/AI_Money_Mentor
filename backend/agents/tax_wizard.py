
from agents.advisor import client

def tax_advice(salary, deductions):

    # ===== BASIC CALCULATIONS =====
    annual_income = salary * 12

    # OLD REGIME
    standard_deduction = 50000
    taxable_old = max(0, annual_income - standard_deduction - deductions)

    if taxable_old <= 250000:
        tax_old = 0
    elif taxable_old <= 500000:
        tax_old = (taxable_old - 250000) * 0.05
    else:
        tax_old = (250000 * 0.05) + (taxable_old - 500000) * 0.2

    # NEW REGIME
    taxable_new = annual_income

    if taxable_new <= 700000:
        tax_new = 0   # rebate
    elif taxable_new <= 1000000:
        tax_new = (taxable_new - 300000) * 0.05
    else:
        tax_new = (700000 * 0.05) + (taxable_new - 1000000) * 0.1

    # BEST REGIME
    best_regime = "Old Regime" if tax_old < tax_new else "New Regime"

    # ===== AI ADVICE =====
    prompt = f"""
You are an expert Indian tax advisor.

Income: ₹{annual_income}
Deductions: ₹{deductions}

Old Regime Tax: ₹{int(tax_old)}
New Regime Tax: ₹{int(tax_new)}

Give EXACTLY 5 bullet points:
- Suggest tax-saving options (80C, ELSS, PPF)
- Mention if deductions should be increased
- Keep simple and practical
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
        "annual_income": int(annual_income),
        "tax_old": int(tax_old),
        "tax_new": int(tax_new),
        "best_regime": best_regime,
        "advice": final_advice
    }