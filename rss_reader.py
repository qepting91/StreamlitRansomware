import streamlit as st
from data_load import load_rss_data
import pandas as pd

def rss_reader():
    rss_data = load_rss_data()
    
    # Convert 'Date' column to datetime format and then to '%b %Y' format
    rss_data['Date'] = pd.to_datetime(rss_data['Date']).dt.strftime('%b %Y')

    st.title("RSS Reader")

    for index, row in rss_data.iterrows():
        markdown_string = f"[{row['Title']} ({row['Date']})]({row['Link']})"
        st.markdown(markdown_string, unsafe_allow_html=True)

