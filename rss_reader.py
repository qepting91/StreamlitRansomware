import streamlit as st
from data_load import load_rss_data

def rss_reader():
    rss_data = load_rss_data()
    st.title("RSS Reader")

    for index, row in rss_data.iterrows():
        markdown_string = f"[{row['Title']} ({row['Date']})]({row['Link']})"
        st.markdown(markdown_string, unsafe_allow_html=True)