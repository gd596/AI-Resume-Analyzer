# AI Resume Analyzer

An AI-powered resume analyzer built with Python, Streamlit, and a local Qwen LLM. The application evaluates resumes using a hybrid approach that combines rule-based ATS scoring with AI-generated feedback and job description matching.

---

## Features

- Upload resumes in PDF and DOCX formats
- Extract resume text automatically
- Rule-based ATS score (0–100)
- Resume section analysis
- Missing section detection
- AI-powered resume evaluation using Qwen
- Job description comparison
- Actionable improvement suggestions

---

## Tech Stack

- Python
- Streamlit
- Ollama
- Qwen 2.5 (7B)
- PyPDF2
- python-docx
- Regular Expressions (re)

---

## Project Structure

```
AI-Resume-Analyzer/
│
├── app.py              # Streamlit application
├── parser.py           # Resume text extraction
├── ats.py              # Rule-based ATS scoring
├── ai_feedback.py      # AI evaluation using Qwen
├── requirements.txt
└── .gitignore
```

---

## How It Works

1. Upload a resume (PDF or DOCX).
2. Resume text is extracted.
3. A rule-based ATS engine evaluates:
   - Contact Information
   - Education
   - Skills
   - Projects
   - Experience
   - Certifications
4. The extracted resume and optional job description are sent to a locally hosted Qwen model.
5. The AI provides detailed suggestions, identifies missing keywords, and recommends improvements.

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/gd596/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama and download the model:

```bash
ollama pull qwen2.5:7b
```

Run the application:

```bash
streamlit run app.py
```

---

## Current Features

- Rule-based ATS scoring
- AI resume evaluation
- Resume parser
- Job description input
- Resume improvement suggestions

---

## Planned Improvements

- ATS score breakdown by category
- Parallel AI and rule-based evaluation
- Keyword highlighting
- Resume rewrite suggestions
- Multiple model selection (Qwen 7B / 14B)
- Better UI and visual analytics
- Cloud deployment

---

## Author

**Gaurav Datta**

Built as a portfolio project to demonstrate practical Python development, LLM integration, and AI-assisted resume analysis.
