📌 Stress Detector

Stress Detector is a dashboard-based AI-powered web application designed to analyze and visualize a user’s stress level using psychological assessment questions and backend logic. The project focuses on mental health awareness and provides a clean, modern interface inspired by real-world wellness platforms.

🧠 Project Overview

Mental stress is a growing concern in modern lifestyles. The Stress Detector project aims to provide an easy-to-use, non-invasive system that helps users understand their stress levels through structured questions and AI-driven analysis, presented in a professional dashboard format.

This project is built as a major project, following a modular architecture with frontend and backend separation.

✨ Key Features

📊 Interactive Dashboard

Stress trend visualization

Current stress level display

🧠 AI-Based Stress Detection

Psychological questionnaire

Backend-driven stress analysis

🧩 Multiple Sections

Dashboard

Mental Health Insights

Activity Overview

Reports

🎨 Modern UI/UX

Brown / earthy professional theme

Card-based layout inspired by wellness apps

🔄 Single Page Application (SPA) Behavior

No page reloads

Smooth navigation

⚠️ Privacy-Friendly

No personal data stored

No medical diagnosis claims

🛠️ Tech Stack
Frontend

HTML5

CSS3 (Grid & Flexbox)

JavaScript (Vanilla)

Chart.js (for data visualization)

Backend

Python

Flask

Flask-CORS

📂 Project Structure
stress-detector/
│
├── backend/
│   └── app.py
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js

⚙️ How It Works

User opens the Stress Detector dashboard.

The application fetches AI-generated stress-related questions from the backend.

The user answers the questions.

Answers are sent to the Python backend.

Backend analyzes responses and calculates stress level.

Stress result and insights are displayed on the dashboard.

User can explore Mental Health, Activity, and Reports sections.

🚀 Installation & Run Guide
1️⃣ Backend Setup
cd backend
python app.py


Backend will run on:

http://127.0.0.1:5000


Test API:

http://127.0.0.1:5000/questions

2️⃣ Frontend Setup

Open frontend/index.html using:

VS Code Live Server (recommended), or

A modern browser (Chrome / Edge)
