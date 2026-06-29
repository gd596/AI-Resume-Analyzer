import re

# Calculate an ATS score by checking the resume against a set of predefined rules.
def calculate_ats_score(resume_text):

    # Initialise the total score and feedback list.
    score = 0
    feedback = []

    # Convert the resume to lowercase for case-insensitive matching.
    text = resume_text.lower()

    # Check whether the resume contains valid contact information.
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    phone_pattern = r"\+?\d[\d\s\-]{8,}\d"

    email_found = re.search(email_pattern, resume_text)
    phone_found = re.search(phone_pattern, resume_text)

    if email_found:
        score += 8
    else:
        feedback.append("Missing email address.")

    if phone_found:
        score += 7
    else:
        feedback.append("Missing phone number.")

    # Verify that the resume contains an Education section.
    if "education" in text:
        score += 15
    else:
        feedback.append("Education section missing.")

    # Check for a Skills section and count recognised technical skills.
    if "skills" in text:
        score += 10

        skills = [
            "python", "sql", "excel", "power bi", "tableau",
            "git", "github", "java", "c++", "javascript",
            "pandas", "numpy", "streamlit", "machine learning",
            "data analysis"
        ]

        skill_count = 0

        for skill in skills:
            if skill in text:
                skill_count += 1

        # Award additional points based on recognised skills.
        score += min(skill_count, 10)

    else:
        feedback.append("Skills section missing.")

    # Evaluate the Projects section using action verbs and measurable achievements.
    if "project" in text or "projects" in text:
        score += 10

        action_verbs = [
            "built", "developed", "created", "designed",
            "implemented", "optimized", "automated",
            "engineered", "improved", "analyzed"
        ]

        verb_count = 0

        # Count strong action verbs used throughout the resume.
        for verb in action_verbs:
            verb_count += text.count(verb)

        score += min(verb_count, 5)

        # Reward resumes that include measurable results or metrics.
        metrics = re.findall(r"\d+%|\d+\+?|\$\d+", resume_text)

        score += min(len(metrics), 10)

    else:
        feedback.append("Projects section missing.")

    # Verify that previous work or internship experience is included.
    if "experience" in text:
        score += 15
    else:
        feedback.append("Experience section missing.")

    # Reward professional certifications if present.
    if "certification" in text or "certifications" in text:
        score += 10
    else:
        feedback.append("No certifications found.")

    # Return both the ATS score and improvement suggestions.
    return {
        "score": score,
        "feedback": feedback
    }