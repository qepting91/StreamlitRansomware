import streamlit as st
from data_load import load_rss_data
from data_process import process_data

def rss_reader():
    rss_data = load_rss_data()
    rss_data = process_data(rss_data)  # Apply the same processing used for the main data
    st.title("RSS Reader")

    for index, row in rss_data.iterrows():
        markdown_string = f"[{row['Title']} ({row['Date']})]({row['Link']})"
        st.markdown(markdown_string, unsafe_allow_html=True)
