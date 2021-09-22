import streamlit as st
import pandas as pd
import numpy as np

from time import time
from src.modules.offer import Offer

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
    # Add results to st.session_state['offers']
    # st.session_state['offers'] = liste des offres
    pass

if st.session_state['offers']:
    st.session_state['offers'] = np.array(
        [i.__dict__ for i in st.session_state['offers']]
    )
    df_offers = pd.DataFrame(st.session_state['offers'])
    st.table(df_offers)
    
