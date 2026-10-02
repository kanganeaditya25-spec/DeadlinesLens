# 📅 DeadlineLens

### AI Academic Deadline Tracker

DeadlineLens is a simple AI-powered academic deadline tracker built with **Streamlit and Google Gemini**.

It allows students to upload a photo of their syllabus, timetable, assignment sheet, exam schedule, or college notice. Gemini analyzes the image and helps identify important academic dates and deadlines.

Students can also chat with the AI about the uploaded document and generate a deadline digest that can be sent to their email.

---

## ✨ Features

- 📸 Upload syllabus, timetable, assignment sheets, and exam schedules
- 🤖 AI-powered document understanding using Google Gemini
- 📅 Extract academic deadlines from images
- 📝 Identify:
  - Assignments
  - Exams
  - Practicals
  - Projects
  - Presentations
  - Quizzes
  - Tests
  - College events
- 💬 Chat with the AI about your academic deadlines
- 🔍 Handles unclear or incomplete information without intentionally inventing dates
- 📋 Generate a deadline digest
- 📧 Send the deadline digest through email
- 🔐 API keys and email credentials are stored using Streamlit Secrets
- 🌐 Deployable using Streamlit Community Cloud

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application |
| Google Gemini | AI chat and image understanding |
| Google GenAI SDK | Connects Python with Gemini |
| Gmail SMTP | Sending deadline emails |
| GitHub | Source code and version control |
| Streamlit Community Cloud | Deployment |

---

## 📂 Project Structure

```text
DeadlineLens/
│
├── app.py
├── prompts.py
├── deadline_parser.py
├── notifier.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml