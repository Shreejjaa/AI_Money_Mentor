import pandas as pd

def analyze_portfolio(file):

    df = pd.read_csv(file)

    total_investment = df["investment_amount"].sum()
    current_value = df["current_value"].sum()

    profit = current_value - total_investment

    equity_value = df[df["category"]=="Equity"]["current_value"].sum()
    debt_value = df[df["category"]=="Debt"]["current_value"].sum()

    diversification_score = 80

    if equity_value > debt_value:
        advice = "Your portfolio is equity heavy. Consider adding some debt funds for stability."
    else:
        advice = "Your portfolio is balanced. Continue SIP investing."

    return {
        "total_investment": int(total_investment),
        "current_value": int(current_value),
        "profit": int(profit),
        "equity_value": int(equity_value),
        "debt_value": int(debt_value),
        "diversification_score": diversification_score,
        "advice": advice
    }