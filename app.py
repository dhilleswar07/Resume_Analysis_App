import streamlit as st
from pdf_reader import extract_pdf
from analyzer import analyze_resume

st.set_page_config(
    page_title="Dhilleswar Resume Analyzer App",
    layout="wide"
)

st.title("Dhilleswar Resume Analyzer App")
st.write("Upload a resume in PDF format to analyze its content and get insights.")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:
    with st.spinner("Reading resume..."):
        resume = extract_pdf(uploaded_file)

    st.success("Resume read successfully!")

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing resume..."):
            result = analyze_resume(resume)

        st.success("Resume analyzed successfully!")

        st.markdown("### Analysis Result")
        st.write(result)

        st.download_button(
            label="Download Analysis Result",
            data=result,
            file_name="analysis_result.txt"
        )