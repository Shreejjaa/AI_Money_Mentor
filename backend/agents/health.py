def calculate_health_score(analysis):

    score = 0

    savings_rate = analysis["savings_rate"]

    if savings_rate > 40:
        score += 40
    elif savings_rate > 20:
        score += 30
    elif savings_rate > 10:
        score += 20
    else:
        score += 10

    expense_ratio = analysis["expense_ratio"]

    if expense_ratio < 50:
        score += 40
    elif expense_ratio < 70:
        score += 30
    else:
        score += 20

    debt = analysis["debt"]

    if debt == 0:
        score += 20
    else:
        score += 10

    return min(score, 100)