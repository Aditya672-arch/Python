"""
AI Resume Analyzer + Job Recommendation System
Run with:  streamlit run app.py
"""

import streamlit as st
import pandas as pd

from data.job_roles import JOB_ROLES
from utils.resume_parser import extract_text_from_pdf, extract_candidate_name, extract_email, extract_phone
from utils.skill_extractor import extract_skills
from utils.job_matcher import match_against_role, match_against_custom_jd, rank_all_roles
from utils.suggestions import suggest_courses, generate_interview_questions

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠", layout="wide")

st.title("🧠 AI Resume Analyzer + Job Recommendation System")
st.caption(
    "Upload a resume, pick a target role (or paste a custom job description), "
    "and get a skill-match score, gap analysis, course suggestions, and interview prep."
)

# ---------------------------------------------------------------------------
# Sidebar: inputs
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("1. Upload Resume")
    uploaded_file = st.file_uploader("Resume (PDF)", type=["pdf"])

    st.header("2. Choose Comparison")
    mode = st.radio("Compare against:", ["A predefined job role", "A custom job description"])

    selected_role = None
    custom_jd = None
    if mode == "A predefined job role":
        selected_role = st.selectbox("Job role", list(JOB_ROLES.keys()))
    else:
        custom_jd = st.text_area("Paste job description here", height=200)

    analyze_clicked = st.button("🔍 Analyze Resume", type="primary", use_container_width=True)

# ---------------------------------------------------------------------------
# Session state so results persist across reruns (e.g. tab clicks)
# ---------------------------------------------------------------------------
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False

if analyze_clicked:
    if uploaded_file is None:
        st.error("Please upload a resume PDF first.")
    elif mode == "A custom job description" and not (custom_jd and custom_jd.strip()):
        st.error("Please paste a job description, or switch to a predefined role.")
    else:
        with st.spinner("Reading resume and extracting skills..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            resume_skills = extract_skills(resume_text)

            if mode == "A predefined job role":
                match_result = match_against_role(resume_skills, selected_role)
            else:
                match_result = match_against_custom_jd(resume_skills, custom_jd)

            top_roles = rank_all_roles(resume_skills)
            courses = suggest_courses(match_result["missing"])
            interview_qs = generate_interview_questions(match_result["matched"], match_result["missing"])

        st.session_state.update(
            analyzed=True,
            resume_text=resume_text,
            resume_skills=resume_skills,
            candidate_name=extract_candidate_name(resume_text),
            candidate_email=extract_email(resume_text),
            candidate_phone=extract_phone(resume_text),
            match_result=match_result,
            top_roles=top_roles,
            courses=courses,
            interview_qs=interview_qs,
        )

# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------
if st.session_state.analyzed:
    mr = st.session_state.match_result

    st.subheader(f"👤 {st.session_state.candidate_name}")
    contact_bits = [c for c in [st.session_state.candidate_email, st.session_state.candidate_phone] if c]
    if contact_bits:
        st.caption(" • ".join(contact_bits))

    col1, col2, col3 = st.columns(3)
    col1.metric("Match against", mr["role"])
    col2.metric("Match %", f"{mr['match_percent']}%")
    col3.metric("Skills detected", len(st.session_state.resume_skills))

    st.progress(min(mr["match_percent"] / 100, 1.0))

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        ["📊 Skill Match", "🎯 Recommended Roles", "📚 Courses to Learn",
         "❓ Interview Prep", "📄 Extracted Skills"]
    )

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### ✅ Matched Skills")
            if mr["matched"]:
                for s in mr["matched"]:
                    st.markdown(f"- {s}")
            else:
                st.info("No overlapping skills found.")
        with c2:
            st.markdown("### ❌ Missing Skills")
            if mr["missing"]:
                for s in mr["missing"]:
                    st.markdown(f"- {s}")
            else:
                st.success("No gaps — great match!")

    with tab2:
        st.markdown("### Suitable Job Roles, Ranked by Fit")
        df = pd.DataFrame(
            [{"Role": r["role"], "Match %": r["match_percent"],
              "Matched Skills": len(r["matched"]), "Required Skills": r["required_total"]}
             for r in st.session_state.top_roles]
        )
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.bar_chart(df.set_index("Role")["Match %"])

    with tab3:
        st.markdown("### Suggested Courses / Resources for Missing Skills")
        if st.session_state.courses:
            for skill, course in st.session_state.courses.items():
                st.markdown(f"**{skill.title()}** — {course}")
        else:
            st.success("No missing skills — nothing to suggest!")

    with tab4:
        iq = st.session_state.interview_qs
        st.markdown("### Based on Your Existing Skills")
        for skill, q in iq["based_on_your_skills"]:
            st.markdown(f"- *({skill})* {q}")
        st.markdown("### To Prepare Before You Apply (Gap Skills)")
        if iq["prepare_for_gaps"]:
            for skill, q in iq["prepare_for_gaps"]:
                st.markdown(f"- *({skill})* {q}")
        else:
            st.info("No gap skills to prep for.")

    with tab5:
        st.markdown("### All Skills Detected in Resume")
        st.write(", ".join(st.session_state.resume_skills) or "None detected.")
        with st.expander("View extracted resume text"):
            st.text(st.session_state.resume_text)

else:
    st.info("⬅️ Upload a resume and click **Analyze Resume** to get started.")
