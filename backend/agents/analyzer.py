def analyze_data(data):
    income = float(data.get("income", 0))
    expenses = float(data.get("expenses", 0))
    debt = float(data.get("debt", 0))

    # Savings calculation
    savings = income - expenses

    # Savings rate
    savings_rate = (savings / income) * 100 if income > 0 else 0

    # Expense ratio
    expense_ratio = (expenses / income) * 100 if income > 0 else 0

    # Recommended emergency fund (6 months expenses)
    emergency_fund_required = expenses * 6

    return {
        "income": income,
        "expenses": expenses,
        "debt": debt,
        "savings": round(savings, 2),
        "savings_rate": round(savings_rate, 2),
        "expense_ratio": round(expense_ratio, 2),
        "emergency_fund_required": round(emergency_fund_required, 2)
    }