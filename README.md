# 📅 DeadlineLens

## AI Academic Deadline Tracker

**Developed by Aditya Kangane**

DeadlineLens is a simple AI-powered academic deadline tracker built
using **Python, Streamlit, and Google Gemini**.

The project helps students find important academic deadlines from
documents such as examination schedules, timetables, assignment sheets,
college notices, and other academic documents.

Instead of manually searching through every document, students can
upload an image and DeadlineLens uses AI to identify and organize
important academic dates.

------------------------------------------------------------------------

## 👨‍💻 Developer

**Name:** Aditya Kangane\
**Branch:** Computer Engineering\
**College:** JSPM's Narhe Technical Campus

------------------------------------------------------------------------

## 🚀 Live Demo

**Deployed Application:**

https://deadlines-lens.streamlit.app/

You can open the live application and try the project directly.

------------------------------------------------------------------------

## 📌 Project Overview

Students regularly receive academic information through different
documents:

-   Examination timetables
-   Assignment notices
-   College circulars
-   Practical schedules
-   Project submission notices
-   Presentation schedules
-   Quiz and test schedules

Finding every important date manually can be time-consuming.

**DeadlineLens** provides a simple solution:

> Upload the document → Let AI understand it → Extract deadlines →
> Create a deadline digest → Send it by email.

------------------------------------------------------------------------

# ✨ Features

### 📸 Academic Document Upload

Upload an academic document as an image.

Supported image formats:

-   JPG
-   JPEG
-   PNG

### 🤖 AI Vision

Google Gemini analyses the uploaded academic document and identifies
important information.

### 📅 Deadline Extraction

The application extracts:

-   Subject
-   Task or event
-   Date
-   Time, if available
-   Important notes, if available

### 💬 AI Chat

Users can ask questions about their academic deadlines through the chat
interface.

### 📋 Deadline Digest

After deadlines are extracted, users can create a simple
reminder-friendly summary.

### 📧 Email Notification

The generated deadline digest can be sent to the user's email using
Gmail SMTP.

### 🔄 Duplicate Prevention

The application avoids adding the same extracted deadline multiple times
during the session.

### 🎓 Student-Friendly Interface

The interface is intentionally simple so that students can easily
understand and use it.

------------------------------------------------------------------------

# 🧠 How DeadlineLens Works

The application follows a simple workflow:

``` text
Student enters name and email
            ↓
       DeadlineLens
            ↓
Upload academic document
            ↓
   Google Gemini analyses image
            ↓
   Important dates are identified
            ↓
    Deadlines are extracted
            ↓
     Extracted deadlines
            ↓
   Create Deadline Digest
            ↓
     Review the summary
            ↓
     Send digest by Email
```

------------------------------------------------------------------------

# 🏗️ Project Architecture

The project is divided into a few simple Python files.

``` text
DeadlineLens/
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py
├── deadline_parser.py
├── notifier.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

------------------------------------------------------------------------

## 📂 File Description

### `app.py`

The main Streamlit application.

It handles:

-   Page setup
-   User onboarding
-   Gemini connection
-   Chat interface
-   Image upload
-   Deadline display
-   Deadline digest generation
-   Email sending

### `deadline_parser.py`

This file sends the uploaded image to Google Gemini and extracts
academic deadlines in JSON format.

### `prompts.py`

Contains the prompts used by DeadlineLens:

-   System prompt
-   Welcome message
-   Deadline digest prompt

### `notifier.py`

Handles sending the generated deadline digest through Gmail SMTP.

### `requirements.txt`

Contains the Python packages required to run DeadlineLens.

### `.streamlit/secrets.toml`

Stores private API keys and email credentials.

**Do not upload this file to GitHub.**

### `.gitignore`

Prevents private files, virtual environments, cache files, and other
unnecessary files from being uploaded to GitHub.

------------------------------------------------------------------------

# 🛠️ Technologies Used

  Technology                  Purpose
  --------------------------- ------------------------------------
  Python                      Main programming language
  Streamlit                   Web application and user interface
  Google Gemini               AI vision and chat
  Google GenAI SDK            Gemini API integration
  JSON                        Structured deadline data
  Gmail SMTP                  Email notification
  Git                         Version control
  GitHub                      Source code hosting
  Streamlit Community Cloud   Deployment

------------------------------------------------------------------------

# 👁️ NxtWave AI Vision Chatbot Project

DeadlineLens was developed using concepts learned from the **NxtWave AI
Vision Chatbot project/workshop**.

The AI Vision Chatbot project introduced the idea of combining:

-   AI Vision
-   Google Gemini
-   Chat
-   Prompt Engineering
-   User onboarding
-   Action/notification features
-   Streamlit

The same basic concept was adapted to create a student-focused academic
deadline tracker.

### From AI Vision Chatbot to DeadlineLens

``` text
NxtWave AI Vision Chatbot
            ↓
      Image Understanding
            ↓
        Google Gemini
            ↓
            Chat
            ↓
       Action / Output
            ↓
        DeadlineLens
            ↓
    Academic Document
            ↓
      Gemini Vision
            ↓
    Deadline Extraction
            ↓
      Deadline Digest
            ↓
       Email Output
```

The NxtWave project provided the foundation for understanding how an AI
vision application can receive an image, use Gemini to understand the
content, interact with the user, and produce a useful output.

DeadlineLens applies that concept to a different real-world problem:
**academic deadline management for students**.

------------------------------------------------------------------------

# 🔑 Gemini Integration

DeadlineLens uses Google Gemini for two main tasks.

## 1. Image Understanding

When a student uploads an academic document, Gemini analyses the image
and provides a response based on the document.

## 2. Deadline Extraction

A separate extraction prompt asks Gemini to return deadline information
in a structured JSON format.

Example:

``` json
[
    {
        "subject": "Data Structures",
        "task": "Assignment Submission",
        "date": "10/10/2026",
        "time": "11:59 PM",
        "notes": "Submit through college portal"
    }
]
```

The application then displays these deadlines in a simple format.

------------------------------------------------------------------------

# 📋 Deadline Digest

Once at least one deadline has been extracted, the **Create Deadline
Digest** button becomes available.

The flow is:

``` text
Upload Document
       ↓
Extract Deadlines
       ↓
Create Deadline Digest
       ↓
AI generates summary
       ↓
Review Digest
       ↓
Send by Email
```

The digest is designed to be short and easy for a student to understand.

------------------------------------------------------------------------

# 📧 Email Notification

DeadlineLens uses Gmail SMTP to send the generated deadline digest.

The application uses:

``` text
Gmail SMTP
smtp.gmail.com
Port 587
```

A Gmail **App Password** should be used instead of the normal Gmail
password.

------------------------------------------------------------------------

# ⚙️ Installation

## 1. Clone the Repository

``` bash
git clone https://github.com/kanganeaditya25-spec/DeadlinesLens.git
```

Move into the project directory:

``` bash
cd DeadlinesLens
```

------------------------------------------------------------------------

## 2. Create a Virtual Environment

``` bash
python -m venv venv
```

### Windows

``` bash
venv\Scripts\activate
```

### macOS / Linux

``` bash
source venv/bin/activate
```

------------------------------------------------------------------------

## 3. Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# 🔐 Configure Secrets

Create this file:

``` text
.streamlit/secrets.toml
```

Add your credentials:

``` toml
GEMINI_API_KEY = "your-gemini-api-key"

GMAIL_EMAIL = "your-email@gmail.com"

GMAIL_APP_PASSWORD = "your-gmail-app-password"
```

### Important

Never commit `secrets.toml` to GitHub.

The project `.gitignore` is configured to ignore:

``` text
.streamlit/secrets.toml
```

------------------------------------------------------------------------

# ▶️ Run Locally

Start the Streamlit application:

``` bash
streamlit run app.py
```

The application will open in your browser.

------------------------------------------------------------------------

# 🧪 How to Use

### Step 1 --- Start the Application

Open DeadlineLens.

### Step 2 --- Enter Your Details

Enter:

-   Your name
-   Your email address

Then click:

**Start DeadlineLens 🚀**

### Step 3 --- Upload a Document

Upload an image of:

-   Exam timetable
-   Assignment sheet
-   College notice
-   Project schedule
-   Practical schedule
-   Other academic documents

### Step 4 --- Let Gemini Analyse It

DeadlineLens sends the document to Gemini.

### Step 5 --- View Extracted Deadlines

The application displays the identified academic deadlines.

### Step 6 --- Create the Digest

Click:

**📋 Create Deadline Digest**

The button becomes active automatically after deadlines are found.

### Step 7 --- Send the Digest

After reviewing the generated summary, click:

**📧 Send deadline digest**

The digest is sent to the email address entered during onboarding.

------------------------------------------------------------------------

# 🎯 Project Objective

The main objective of DeadlineLens is to make academic deadline
management easier for students.

Instead of manually checking multiple documents and remembering
different dates, students can use one simple application to identify and
organize their important academic deadlines.

------------------------------------------------------------------------

# 💡 Problem Statement

Students receive important academic dates from many different sources.

For example:

-   An exam date may be present in a timetable.
-   An assignment deadline may be present in a notice.
-   A project submission date may be shared separately.
-   A presentation schedule may be provided as an image.

Important dates can easily be missed.

DeadlineLens attempts to solve this problem by using AI to convert
academic documents into an organized list of deadlines.

------------------------------------------------------------------------

# 🌟 Advantages

-   Simple to use
-   Student-focused
-   Uses AI vision
-   Saves manual effort
-   Extracts multiple deadlines
-   Creates a readable summary
-   Provides email delivery
-   Can be accessed through a web browser
-   Uses a simple technology stack

------------------------------------------------------------------------

# 📚 Learning Outcomes

Through this project, I learned and practiced:

-   Python programming
-   Streamlit application development
-   Google Gemini API integration
-   AI Vision
-   Prompt Engineering
-   JSON data handling
-   Image processing
-   Session state in Streamlit
-   Gmail SMTP
-   API key management
-   Git and GitHub
-   Cloud deployment

I also learned how concepts from an AI Vision Chatbot project can be
adapted to create a different practical application.

------------------------------------------------------------------------

# 🔮 Future Improvements

Possible future improvements include:

-   📱 Better mobile interface
-   📄 PDF document support
-   📅 Google Calendar integration
-   🔔 Automatic deadline reminders
-   💬 WhatsApp notifications
-   📲 Telegram notifications
-   📊 Student dashboard
-   🗂️ Subject-wise deadline organization
-   ⏰ Upcoming deadline alerts
-   👥 Multiple course/semester support
-   🔍 Better document and date recognition

------------------------------------------------------------------------

# ☁️ Deployment

DeadlineLens is deployed using **Streamlit Community Cloud**.

### Live Application

https://deadlines-lens.streamlit.app/

### Source Code

https://github.com/kanganeaditya25-spec/DeadlinesLens

------------------------------------------------------------------------

# 🔒 Security Notes

The project uses API keys and email credentials.

Private credentials should always be stored in:

``` text
.streamlit/secrets.toml
```

and should never be committed to GitHub.

The following should remain private:

-   Gemini API key
-   Gmail email credentials
-   Gmail App Password

------------------------------------------------------------------------

# 📝 Example

Suppose a student uploads an examination timetable containing:

``` text
Data Structures - 05/10/2026
Object Oriented Programming - 06/10/2026
Operating Systems - 07/10/2026
Digital Electronics - 08/10/2026
Open Elective - 09/10/2026
Universal Human Values - 10/10/2026
```

DeadlineLens can identify these dates and display them as:

``` text
📅 Extracted Deadlines

05/10/2026 - Data Structures - Examination
06/10/2026 - Object Oriented Programming - Examination
07/10/2026 - Operating Systems - Examination
08/10/2026 - Digital Electronics - Examination
09/10/2026 - Open Elective - Examination
10/10/2026 - Universal Human Values - Examination
```

The student can then create a single deadline digest from these entries.

------------------------------------------------------------------------

# 🤝 Project Purpose

This project was created as a learning project to understand how AI,
vision models, APIs, and simple web applications can be combined to
solve a practical student problem.

The goal is not to replace existing college systems, but to provide a
simple helper for students to organize academic deadlines.

------------------------------------------------------------------------

# 👨‍💻 Author

## Aditya Kangane

**Computer Engineering Student**\
**JSPM's Narhe Technical Campus**

Built as a student project using Python, Streamlit, and Google Gemini.

------------------------------------------------------------------------

# ⭐ DeadlineLens

### Turning academic documents into organized deadlines. 📅🤖

**Live Demo:**\
https://deadlines-lens.streamlit.app/

**GitHub Repository:**\
https://github.com/kanganeaditya25-spec/DeadlinesLens
