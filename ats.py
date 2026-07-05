import re


def calculate_ats_score(resume_text, job_description=""):
    score = 0
    feedback = []

    text = resume_text.lower()

    # Contact information
    email_found = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume_text)
    phone_found = re.search(r"\+?\d[\d\s\-]{8,}\d", resume_text)

    if email_found:
        score += 10
    else:
        feedback.append("Missing email address.")

    if phone_found:
        score += 10
    else:
        feedback.append("Missing phone number.")

    # Main resume sections
    sections = ["education", "skills", "projects", "experience"]

    for section in sections:
        if section in text:
            score += 15
        else:
            feedback.append(section.title() + " section missing.")

    # Certifications
    if "certification" in text or "certifications" in text:
        score += 10
    else:
        feedback.append("No certifications found.")

    # Skills check
    skills = [
        "python", "sql", "excel", "power bi", "tableau",
        "git", "github", "pandas", "numpy", "streamlit",
        "machine learning", "data analysis"
    ]

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    score += min(len(found_skills) * 2, 10)

    if len(found_skills) < 4:
        feedback.append("Add more relevant technical skills.")

    # Action verbs
    action_verbs = [
        "built", "developed", "created", "designed",
        "implemented", "improved", "analyzed", "automated"
    ]

    found_verbs = []

    for verb in action_verbs:
        if verb in text:
            found_verbs.append(verb)

    score += min(len(found_verbs) * 2, 10)

    if len(found_verbs) < 3:
        feedback.append("Use stronger action verbs in your bullet points.")

    # Metrics / numbers
    numbers = re.findall(r"\d+%|\d+\+|\d+", resume_text)

    score += min(len(numbers) * 2, 10)

    if len(numbers) < 3:
        feedback.append("Add measurable achievements using numbers or percentages.")

    # Job description keyword match
    matched_keywords = []
    missing_keywords = []

    if job_description.strip():
        jd_words = job_description.lower().split()

        important_words = []

        for word in jd_words:
            word = word.strip(".,:;()[]{}")

            if len(word) > 4 and word not in important_words:
                important_words.append(word)

        important_words = important_words[:15]

        for word in important_words:
            if word in text:
                matched_keywords.append(word)
            else:
                missing_keywords.append(word)

        if len(important_words) > 0:
            match_score = int((len(matched_keywords) / len(important_words)) * 100)
        else:
            match_score = 0
    else:
        match_score = None

    # Keep score within 100
    score = min(score, 100)

    return {
        "score": score,
        "feedback": feedback,
        "found_skills": found_skills,
        "found_verbs": found_verbs,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "match_score": match_score
    }