import ollama

# Local LLM used for resume analysis.
MODEL = "qwen2.5:7b"


# Build the prompt sent to the language model.
def build_prompt(resume_text, job_description):

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


# Send the prompt to the local Qwen model.
def query_llm(prompt):

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.3,
            "num_predict": 600
        }
    )

    return response["message"]["content"]


# Main function used by app.py.
def get_ai_feedback(resume_text, job_description=""):

    prompt = build_prompt(resume_text, job_description)

    feedback = query_llm(prompt)

    return feedback