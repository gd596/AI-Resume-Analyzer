import streamlit as st

from parser import extract_text_from_pdf, extract_text_from_docx
from ats import calculate_ats_score
from ai_feedback import get_ai_feedback


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

.hero {
    padding: 2rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #eef2ff, #f8fafc);
    border: 1px solid #e5e7eb;
    margin-bottom: 1.5rem;
}

.hero h1 {
    color: #0f172a !important;
}
            
.card {
    padding: 1.2rem;
    border-radius: 14px;
    background: white;
    border: 1px solid #e5e7eb;
    margin-bottom: 1rem;
}

.small-text {
    color: #64748b;
    font-size: 0.95rem;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>📄 AI Resume Analyzer</h1>
    <p class="small-text">
        Upload your resume and get ATS-oriented scoring, section analysis,
        and AI-powered improvement suggestions.
    </p>
</div>
""", unsafe_allow_html=True)


with st.sidebar:
    st.header("About")
    st.write(
        "This app analyzes resumes using rule-based ATS checks "
        "and AI-generated feedback."
    )

    st.header("Tech Stack")
    st.write("Python • Streamlit • Groq API • PyPDF2 • python-docx")

    st.header("How it works")
    st.write(
        "1. Upload resume\n"
        "2. Extract text\n"
        "3. Calculate ATS score\n"
        "4. Generate AI feedback"
    )


uploaded_resume = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=180,
    placeholder="Optional: paste the internship/job description here..."
)

analyze_clicked = st.button("Analyze Resume", type="primary")


if analyze_clicked:
    if uploaded_resume is None:
        st.error("Please upload a resume first.")
        st.stop()

    if uploaded_resume.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_resume)

    elif uploaded_resume.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        resume_text = extract_text_from_docx(uploaded_resume)

    else:
        st.error("Unsupported file type.")
        st.stop()

    if not resume_text.strip():
        st.error("Could not extract text from this resume. Please try another file.")
        st.stop()

    ats_result = calculate_ats_score(resume_text, job_description)

    st.subheader("Analysis Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("ATS Score", f"{ats_result['score']}/100")

    with col2:
        st.metric("Suggestions", len(ats_result["feedback"]))

    with st.expander("📌 ATS Suggestions", expanded=True):
        if ats_result["feedback"]:
            for item in ats_result["feedback"]:
                st.write("•", item)
        else:
            st.success("No major ATS issues found.")

    with st.expander("📄 Extracted Resume Text"):
        st.text_area("Resume Content", resume_text, height=300)

    st.subheader("AI Feedback")

    with st.spinner("Analyzing with AI..."):
        ai_response = get_ai_feedback(resume_text, job_description)

    st.write(ai_response)