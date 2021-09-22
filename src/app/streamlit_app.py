import streamlit as st

# Layout
st.set_page_config(
    layout="wide",
    page_title='Job Scraper',
    page_icon=":moneybag:")
st.title("Job Scraper Dashboard")

# Make 2 input boxes, one for the job title and one for the location
job_title = st.sidebar.text_input("Job Title", "Data Scientist")
location = st.sidebar.text_input("Location", "New York")