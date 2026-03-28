def calculate_risk(analysis):

    savings_rate = analysis["savings_rate"]
    expenses = analysis["expenses"]
    savings = analysis["savings"]

    # If user barely saves money
    if savings_rate < 10 or savings <= 0:
        return "Low"

    # Moderate savings
    elif 10 <= savings_rate < 30:
        return "Medium"

    # Strong financial position
    else:
        return "High"