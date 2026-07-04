# AI Resume Analyzer

🚀 **Live Demo:** (https://gd-ai-resume-analyzer.streamlit.app/)

An AI-powered Resume Analyzer built with Python and Streamlit that evaluates resumes using a hybrid approach combining rule-based ATS scoring with Large Language Model (LLM) feedback and job description matching.

---

## Features

- 📄 Upload resumes in PDF and DOCX formats
- 🔍 Automatic resume text extraction
- 📊 Rule-based ATS score (0–100)
- 📑 Resume section detection and analysis
- ⚠️ Missing section identification
- 🤖 AI-powered resume evaluation
- 🎯 Job description comparison
- 💡 Actionable resume improvement suggestions

---

## Tech Stack

- Python
- Streamlit
- Groq API/Llama
- PyPDF2
- python-docx
- Regular Expressions (re)
- Git & GitHub

---

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py              # Streamlit web application
├── parser.py           # Resume parsing & text extraction
├── ats.py              # Rule-based ATS scoring engine
├── ai_feedback.py      # AI feedback generation
├── requirements.txt
└── .gitignore
```

---

## How It Works

1. Upload a resume in PDF or DOCX format.
2. Resume text is extracted automatically.
3. A rule-based ATS engine evaluates:
   - Contact Information
   - Education
   - Skills
   - Projects
   - Experience
   - Certifications
4. The extracted resume (and optional job description) is analyzed by the LLM.
5. The application generates:
   - ATS score
   - Missing section analysis
   - AI-generated feedback
   - Resume improvement suggestions
   - Job description match analysis

---

## Installation

Clone the repository

```bash
git clone https://github.com/gd596/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Roadmap

- ATS score breakdown by category
- Resume keyword highlighting
- Resume rewrite suggestions
- Improved UI/UX
- Multiple AI model selection
- Resume comparison against multiple job descriptions
- Downloadable PDF analysis report
- Interactive analytics dashboard

---

## Skills Demonstrated

- Python Development
- Streamlit
- LLM Integration
- Prompt Engineering
- Resume Parsing
- Rule-Based Scoring Systems
- Modular Software Design
- Git & GitHub

---

## Author

**Gaurav Datta**

Built as a portfolio project demonstrating practical Python development, document parsing, LLM integration, and AI-assisted resume analysis.