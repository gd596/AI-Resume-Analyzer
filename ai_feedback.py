import streamlit as st
from groq import Groq

MODEL = "llama-3.1-8b-instant"


def build_prompt(resume_text, job_description=""):
    return f"""
You are an expert ATS recruiter and resume reviewer.

Evaluate the following resume.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:
1. Missing Keywords
2. Weak Sections
3. Suggested Skills
4. Improved Resume Bullet Points
5. Overall Feedback

Keep the response concise and practical.
"""


def query_llm(prompt):
    try:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are an expert resume reviewer and ATS optimization assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=800
        )

        return response.choices[0].message.content

    except Exception:
        return "AI feedback is currently unavailable. Please try again later."


def get_ai_feedback(resume_text, job_description=""):
    prompt = build_prompt(resume_text, job_description)
    return query_llm(prompt)