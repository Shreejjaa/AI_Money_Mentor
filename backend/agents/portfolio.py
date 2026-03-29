import pandas as pd

def analyze_portfolio(file):

    df = pd.read_csv(file)

    total_investment = df["investment_amount"].sum()
    current_value = df["current_value"].sum()
    profit = current_value - total_investment

    # Asset allocation
    equity_value = df[df["category"]=="Equity"]["current_value"].sum()
    debt_value = df[df["category"]=="Debt"]["current_value"].sum()

    total_value = equity_value + debt_value
    equity_ratio = (equity_value / total_value) * 100 if total_value > 0 else 0

    diversification_score = 80  # keep simple for now

    # =========================
    # NEW FEATURES START HERE
    # =========================

    # 1. XIRR (dummy for now)
    xirr = 12.5

    # 2. Benchmark (use NIFTY 50 approx)
    benchmark_return = 14

    if xirr > benchmark_return:
        performance = "Outperforming"
    else:
        performance = "Underperforming"

    # 3. Overlap (based on duplicate holdings)
    if "holding" in df.columns:
        duplicate_count = df["holding"].duplicated().sum()
        overlap = int((duplicate_count / len(df)) * 100)
    else:
        overlap = 0

    # 4. Expense Ratio Impact
    if "expense_ratio" in df.columns:
        avg_expense = df["expense_ratio"].mean()
        expense_impact = int((avg_expense / 100) * current_value)
    else:
        avg_expense = 0
        expense_impact = 0

    # =========================
    # SMART AI ADVICE
    # =========================

    advice_list = []

    if equity_ratio > 80:
        advice_list.append("Allocate 20–30% to debt funds for stability.")

    if overlap > 30:
        advice_list.append("Reduce overlap by removing duplicate large-cap funds.")

    if avg_expense > 1:
        advice_list.append("Switch to lower expense ratio funds to save costs.")

    if performance == "Underperforming":
        advice_list.append("Consider reallocating to funds beating benchmark like NIFTY 50.")

    if not advice_list:
        advice_list.append("Your portfolio looks well balanced. Continue investing.")

    final_advice = " ".join(advice_list)

    # =========================
    # RETURN ALL DATA
    # =========================

    return {
        "total_investment": int(total_investment),
        "current_value": int(current_value),
        "profit": int(profit),

        "equity_value": int(equity_value),
        "debt_value": int(debt_value),
        "diversification_score": diversification_score,

        "xirr": xirr,
        "benchmark_return": benchmark_return,
        "performance": performance,

        "overlap": overlap,
        "expense_impact": expense_impact,

        "advice": final_advice
    }