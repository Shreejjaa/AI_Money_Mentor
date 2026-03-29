const BASE_URL = "http://127.0.0.1:5000";

/* =========================
SCROLL FUNCTION
========================= */
function scrollToSection(id){
    document.getElementById(id).scrollIntoView({
        behavior: "smooth"
    });
}

/* =========================
GENERATE FINANCIAL PLAN
========================= */
async function generatePlan(){

const age = document.getElementById("age").value;
const income = document.getElementById("income").value;
const expenses = document.getElementById("expenses").value;
const debt = document.getElementById("debt").value;

if(!age || !income || !expenses){
    alert("Please fill all required fields");
    return;
}

/*  Loading UI */
document.getElementById("result").innerHTML =
"<p class='loading'>Analyzing your finances...</p>";

try{

const res = await fetch(`${BASE_URL}/generate-plan`,{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
age:Number(age),
income:Number(income),
expenses:Number(expenses),
debt:Number(debt)
})
});

const data = await res.json();

/*  Result UI */
document.getElementById("result").innerHTML = `
<div class="score-badge">💰 ${data.health_score}/100</div>

<p><b>Income:</b> ₹${data.analysis.income}</p>
<p><b>Expenses:</b> ₹${data.analysis.expenses}</p>
<p><b>Savings:</b> ₹${data.analysis.savings}</p>

<h3> Monthly SIP: ₹${data.plan.monthly_sip}</h3>

<div class="chart-container">
    <canvas id="chart"></canvas>
</div>

<p><b>AI Advice:</b> ${data.advice}</p>
`;

/*  Chart */
const ctx = document.getElementById("chart");

new Chart(ctx,{
type:"pie",
data:{
labels:["Equity","Debt","Gold"],
datasets:[{
data:[
data.plan.allocation.equity,
data.plan.allocation.debt,
data.plan.allocation.gold
]
}]
},
options:{
responsive:true,
maintainAspectRatio:false
}
});

}catch(error){
document.getElementById("result").innerHTML =
"<p style='color:red;'> Backend connection error</p>";
}

}

/* =========================
AI CHAT (PREMIUM STYLE)
========================= */
async function sendMessage(){

const input = document.getElementById("chatInput");
const chatBox = document.getElementById("chatBox");

const message = input.value.trim();
if(!message) return;

/*  User bubble */
chatBox.innerHTML += `<div class="chat-user">${message}</div>`;
input.value = "";

/*  Typing indicator */
chatBox.innerHTML += `<div class="chat-ai" id="typing">Typing...</div>`;
chatBox.scrollTop = chatBox.scrollHeight;

try{

const res = await fetch(`${BASE_URL}/chat`,{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({message})
});

const data = await res.json();

/* Remove typing */
document.getElementById("typing").remove();

/* AI response */
chatBox.innerHTML += `<div class="chat-ai">${data.reply}</div>`;
chatBox.scrollTop = chatBox.scrollHeight;

}catch(error){

document.getElementById("typing").remove();
chatBox.innerHTML += `<div class="chat-ai">❌ AI unavailable</div>`;
}

}

/* =========================
ENTER KEY SUPPORT
========================= */
document.addEventListener("DOMContentLoaded", () => {
document.getElementById("chatInput").addEventListener("keypress",function(e){
    if(e.key === "Enter"){
        sendMessage();
    }
});
});

/* =========================
LIFE EVENT ADVISOR
========================= */
async function lifeEventAdvice(){

document.getElementById("lifeEventResult").innerHTML =
"<p class='loading'>Analyzing life event...</p>";

try{

const res = await fetch(`${BASE_URL}/life-event`,{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
event:document.getElementById("eventType").value,
income:document.getElementById("eventIncome").value,
savings:document.getElementById("eventSavings").value,
debt:document.getElementById("eventDebt").value
})
});

const data = await res.json();

document.getElementById("lifeEventResult").innerHTML =
`<p>${data.advice}</p>`;

}catch{
document.getElementById("lifeEventResult").innerHTML =
"<p style='color:red;'>Error fetching advice</p>";
}

}

/* =========================
TAX WIZARD
========================= */
async function taxWizard(){

document.getElementById("taxResult").innerHTML =
"<p class='loading'>Calculating tax strategy...</p>";

try{

const res = await fetch(`${BASE_URL}/tax-wizard`,{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
salary:document.getElementById("salary").value,
deductions:document.getElementById("deductions").value
})
});

const data = await res.json();

document.getElementById("taxResult").innerHTML =
`<p>${data.advice}</p>`;

}catch{
document.getElementById("taxResult").innerHTML =
"<p style='color:red;'>Error fetching tax advice</p>";
}

}

/* =========================
COUPLE PLANNER
========================= */
async function couplePlanner(){

document.getElementById("coupleResult").innerHTML =
"<p class='loading'>Analyzing couple finances...</p>";

try{

const res = await fetch(`${BASE_URL}/couple-plan`,{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
income1:document.getElementById("income1").value,
income2:document.getElementById("income2").value,
expenses:document.getElementById("coupleExpenses").value
})
});

const data = await res.json();

document.getElementById("coupleResult").innerHTML =
`<p>${data.advice}</p>`;

}catch{
document.getElementById("coupleResult").innerHTML =
"<p style='color:red;'>Error fetching plan</p>";
}

}
/* =========================
MF PORTFOLIO X-RAY
========================= */
async function analyzePortfolio(){

const fileInput = document.getElementById("portfolioFile");
const resultBox = document.getElementById("portfolioResult");

if(!fileInput.files.length){
    alert("Please upload your portfolio CSV file");
    return;
}

const file = fileInput.files[0];

const formData = new FormData();
formData.append("file", file);

/* Loading UI */
resultBox.innerHTML =
"<p class='loading'>Analyzing portfolio...</p>";

try{

const res = await fetch(`${BASE_URL}/portfolio-xray`,{
method:"POST",
body:formData
});

const data = await res.json();

resultBox.innerHTML = `

<h3> Portfolio Summary</h3>

<p><b>Total Investment:</b> ₹${data.total_investment}</p>

<p><b>Current Value:</b> ₹${data.current_value}</p>

<p><b>Profit / Loss:</b> ₹${data.profit}</p>

<h3> Asset Allocation</h3>

<p>Equity: ₹${data.equity_value}</p>

<p>Debt: ₹${data.debt_value}</p>

<p>Diversification Score: ${data.diversification_score}/100</p>

<h3> AI Portfolio Advice</h3>

<p>${data.advice}</p>

`;

}catch(error){

resultBox.innerHTML =
"<p style='color:red;'> Error analyzing portfolio</p>";

}

}