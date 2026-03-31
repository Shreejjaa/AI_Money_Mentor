AI Money Mentor (India)

An AI-powered personal finance mentor designed to make financial planning as simple as using WhatsApp.

Problem

95% of Indians lack a structured financial plan. Traditional financial advisors charge ₹25,000+ annually and primarily serve High Net-Worth Individuals (HNIs), leaving the majority underserved.

Solution

AI Money Mentor democratizes financial advice by providing:

* Personalized financial planning
* Real-time AI guidance
* Simple, beginner-friendly insights

Tech Stack

* **Backend:** Flask, Flask-CORS
* **AI Engine:** Google Gemini API
* **Data Processing:** Pandas
* **Frontend:** HTML, CSS, JavaScript
* **Environment:** Python-dotenv

Features

Money Health Score

* Evaluates financial health across 6 dimensions
* Provides actionable suggestions

FIRE Planner

* Calculates retirement corpus
* Suggests monthly SIP investment

Life Advisor

* AI guidance for life events (bonus, marriage, etc.)

Tax Wizard

* Compares old vs new tax regimes
* Suggests deductions

Couple Planner

* Joint financial optimization

AI Chat

* Conversational financial assistant

Project Structure
```
AI_money_mentor/
│
├── backend/
│   ├── agents/
│   │   ├── advisor.py
│   │   ├── analyzer.py
│   │   ├── budget_analyzer.py
│   │   ├── couple_planner.py
│   │   ├── fire_planner.py
│   │   ├── health.py
│   │   ├── life_event_advisor.py
│   │   ├── planner.py
│   │   ├── risk.py
│   │   └── tax_wizard.py
│   │
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
|
├── .env
└── README.md (optional but recommended at root)
```
Setup Instructions

1. Clone the repo:

git clone https://github.com/Shreejjaa/AI_Money_Mentor.git

OR

git clone https://github.com/RiyaBehera/AI_Money_Mentor

2. Install dependencies:

pip install -r requirements.txt

3. Add `.env` file:

GEMINI_API_KEY=your_api_key

4. Run Flask:

python app.py

5. Open in Live Server:

(http://127.0.0.1:5500/frontend/index.html)

Future Improvements

* Graph visualizations
* User login & memory
* Mobile app version

Team

This project was built for ET Gen AI Hackathon by a collaborative team.

Contributors are listed in the repository:
See Contributors Section on GitHub
