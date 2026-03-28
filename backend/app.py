
from flask import Flask, request, jsonify
from flask_cors import CORS

from agents.analyzer import analyze_data
from agents.risk import calculate_risk
from agents.planner import generate_plan
from agents.advisor import get_advice, client
from agents.health import calculate_health_score
from agents.fire_planner import calculate_fire_plan
from agents.budget_analyzer import analyze_budget
from agents.life_event_advisor import life_event_advice
from agents.tax_wizard import tax_advice
from agents.couple_planner import couple_finance_advice
from agents.portfolio import analyze_portfolio
app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "AI Money Mentor Backend is running 🚀"


# ------------------------------------------------
# Financial Plan API
# ------------------------------------------------
@app.route("/generate-plan", methods=["POST"])
def generate_plan_api():

    data = request.get_json()

    try:
        # Convert values safely
        age = int(data.get("age", 0))
        income = float(data.get("income", 0))
        expenses = float(data.get("expenses", 0))
        debt = float(data.get("debt", 0))

        user_data = {
            "age": age,
            "income": income,
            "expenses": expenses,
            "debt": debt
        }

        # 1 Analyze financial data
        analysis = analyze_data(user_data)

        # 2️ Health score
        health_score = calculate_health_score(analysis)

        # 3️ Risk profile
        risk = calculate_risk(analysis)

        # 4️ Investment plan
        plan = generate_plan(analysis, risk)

        # 5️ FIRE retirement plan
        fire_plan = calculate_fire_plan(age, analysis["savings"])

        # 6️ AI financial advice
        advice = get_advice(user_data, plan)

        # -------- Clean AI Formatting --------
        advice = advice.replace("**", "")
        advice = advice.replace("*", "")

        lines = advice.split("\n")

        clean_lines = []
        for line in lines:
            line = line.strip()

            if line == "" or "financial advice" in line.lower():
                continue

            clean_lines.append("• " + line)

        advice = "<br>".join(clean_lines)

        return jsonify({
            "analysis": analysis,
            "health_score": health_score,
            "risk": risk,
            "plan": plan,
            "fire_plan": fire_plan,
            "advice": advice
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


# ------------------------------------------------
# AI Financial Mentor Chat
# ------------------------------------------------
@app.route("/chat", methods=["POST"])
def chat_with_ai():

    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"reply": "Please enter a question."})

    prompt = f"""
You are an expert Indian financial mentor helping beginners manage money.

User Question:
{message}

Give a simple answer in 3-5 short bullet points.
Avoid complex financial jargon.
Do not use markdown formatting like ** or *.
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )

        if hasattr(response, "text"):

            reply = response.text

            # Clean formatting
            reply = reply.replace("**", "")
            reply = reply.replace("*", "")

            lines = reply.split("\n")
            clean_lines = []

            for line in lines:
                line = line.strip()

                if line == "":
                    continue

                clean_lines.append("• " + line)

            reply = "<br>".join(clean_lines)

            return jsonify({"reply": reply})

        return jsonify({"reply": "Sorry, I couldn't generate a response."})

    except Exception:
        return jsonify({
            "reply": "AI service is temporarily unavailable. Please try again later."
        })

# ------------------------------------------------
# Budget Analyzer API
# ------------------------------------------------
@app.route("/analyze-budget", methods=["POST"])
def analyze_budget_api():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    try:
        result = analyze_budget(file)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -----------------------------
# Life Event Financial Advisor
# -----------------------------
@app.route("/life-event", methods=["POST"])
def life_event_api():

    data = request.get_json()

    event = data.get("event")
    income = float(data.get("income", 0))
    savings = float(data.get("savings", 0))
    debt = float(data.get("debt", 0))

    advice = life_event_advice(event, income, savings, debt)

    return jsonify({
        "event": event,
        "advice": advice
    })

# -----------------------------
# Tax Wizard
# -----------------------------
@app.route("/tax-wizard", methods=["POST"])
def tax_wizard_api():

    data = request.get_json()

    salary = float(data.get("salary", 0))
    deductions = float(data.get("deductions", 0))

    advice = tax_advice(salary, deductions)

    return jsonify({
        "salary": salary,
        "deductions": deductions,
        "advice": advice
    })

# -----------------------------
# Couple Financial Planner
# -----------------------------
@app.route("/couple-plan", methods=["POST"])
def couple_plan_api():

    data = request.get_json()

    income1 = float(data.get("income1", 0))
    income2 = float(data.get("income2", 0))
    expenses = float(data.get("expenses", 0))

    advice = couple_finance_advice(income1, income2, expenses)

    return jsonify({
        "combined_income": income1 + income2,
        "expenses": expenses,
        "advice": advice
    })
# -----------------------------
# MF Portfolio X-Ray
# -----------------------------
@app.route("/portfolio-xray", methods=["POST"])
def portfolio_xray_api():

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    try:
        result = analyze_portfolio(file)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
# ------------------------------------------------
# Run Server
# ------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
