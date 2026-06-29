import streamlit as st
from parser import extract_text_from_pdf, extract_text_from_docx
from ats import calculate_ats_score
from ai_feedback import get_ai_feedback

# Display the application title.
st.title("AI Resume Analyzer")

# Upload the user's resume (only PDF and DOCX are accepted).
uploaded_resume = st.file_uploader(
    "Upload your resume (PDF or DOCX)",
    type=["pdf", "docx"]
)

# Optional job description for comparing the resume against a specific role.
job_description = st.text_area(
    "Paste Job Description",
    height=200,
    placeholder="Paste the internship/job description here..."
)

# Start the resume analysis when clicked.
analyze_clicked = st.button("Analyze Resume")

# Run the analysis only after the user clicks the button.
if analyze_clicked:

    # Ensure a resume has been uploaded before continuing.
    if uploaded_resume is None:
        st.error("Please upload a resume first.")

    else:

        # Convert the uploaded resume into plain text based on its file type.
        if uploaded_resume.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_resume)

        elif uploaded_resume.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_text_from_docx(uploaded_resume)

        else:
            st.error("Unsupported file type.")
            st.stop()

        # Display the extracted text for verification/debugging.
        st.subheader("Extracted Resume Text")
        st.text_area("Resume Content", resume_text, height=300)

        # Calculate the rule-based ATS score and suggestions.
        ats_result = calculate_ats_score(resume_text)

        # Display the ATS score.
        st.subheader("ATS Score")
        st.metric("Score", f"{ats_result['score']}/100")

        # Display ATS improvement suggestions.
        st.subheader("Suggestions")
        for item in ats_result["feedback"]:
            st.write("•", item)

        # Send the resume and job description to the LLM for deeper evaluation.
        st.subheader("AI Feedback")

    with st.spinner("Analyzing with AI..."):
        ai_feedback = get_ai_feedback(resume_text, job_description)

    st.write(ai_feedback)


