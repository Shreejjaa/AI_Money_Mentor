def generate_plan(analysis, risk):

    savings = analysis["savings"]
    expenses = analysis["expenses"]

    # Recommend investing 50% of savings
    monthly_sip = round(savings * 0.5, 2)

    # Emergency fund recommendation
    emergency_fund_target = round(expenses * 6, 2)

    # Asset allocation based on risk
    if risk == "Low":
        equity = 40
        debt = 50
        gold = 10

    elif risk == "Medium":
        equity = 60
        debt = 30
        gold = 10

    else:  # High risk
        equity = 70
        debt = 20
        gold = 10

    return {
        "monthly_sip": monthly_sip,

        "emergency_fund_target": emergency_fund_target,

        "allocation": {
            "equity": equity,
            "debt": debt,
            "gold": gold
        },

        "goal_suggestion": "Start long-term SIP investments for wealth creation and retirement."
    }