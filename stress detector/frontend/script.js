// ---------- PAGE SWITCHING ----------
function showPage(page) {
  document.querySelectorAll(".page").forEach(p => {
    p.classList.remove("active");
  });

  document.getElementById(page + "-section")
    .classList.add("active");

  document.querySelectorAll(".sidebar li").forEach(li => {
    li.classList.remove("active");
  });

  event.target.classList.add("active");
}

// ---------- CHART ----------
const ctx = document.getElementById("stressChart");
const chart = new Chart(ctx, {
  type: "line",
  data: {
    labels: ["Mon","Tue","Wed","Thu","Fri"],
    datasets: [{
      label: "Stress Level",
      data: [3,5,4,6,5],
      borderColor: "#6d4c41",
      tension: 0.4
    }]
  }
});

// ---------- AI QUESTIONS ----------
let questions = [];
let answers = [];
let i = 0;

fetch("http://127.0.0.1:5000/questions")
  .then(res => res.json())
  .then(data => {
    questions = data;
    document.getElementById("question").innerText = questions[i];
  });

function next() {
  answers.push(Number(document.getElementById("answer").value));
  document.getElementById("status").innerText =
    `Answered ${answers.length} questions`;

  i++;
  if (i < questions.length) {
    document.getElementById("question").innerText = questions[i];
  } else {
    analyze();
  }
}

function analyze() {
  document.getElementById("status").innerText = "Detecting stress…";

  fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({ answers })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText = data.stress_level;
    document.getElementById("advice").innerText = data.message;
    document.getElementById("status").innerText = "Stress Detected ✔";
  });
}
