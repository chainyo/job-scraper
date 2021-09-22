import streamlit as st

# Main layout
st.set_page_config(
    layout="wide",
    page_title='Job Scraper',
    page_icon=":moneybag:")
st.title("Job Scraper Dashboard")

# Sidebar
job_title = st.sidebar.text_input("Job Title", "ex: Data Scientist")
location = st.sidebar.text_input("Location", "ex: Paris")

if st.sidebar.button("Start Scraping"):
    # Scraping logic here
