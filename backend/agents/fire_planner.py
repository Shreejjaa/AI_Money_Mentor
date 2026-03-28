def calculate_fire_plan(age, savings):

    retirement_age = 60
    years_left = retirement_age - age

    target_corpus = 50000000  # ₹5 Crore target

    monthly_sip_needed = target_corpus / (years_left * 12)

    return {
        "target_corpus": target_corpus,
        "years_left": years_left,
        "monthly_sip_needed": round(monthly_sip_needed, 2)
    }