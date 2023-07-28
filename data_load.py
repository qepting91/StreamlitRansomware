import streamlit as st
from streamlit_gsheets import GSheetsConnection

@st.cache_data
def load_data():
    url = "https://docs.google.com/spreadsheets/d/1GxUiFb00sCTytJ4XkegN8qnZ4WAmsXWGVV98eMN8F_I/edit#gid=2084622647"
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url, usecols=[0, 1, 2])
    return data

@st.cache_data
def load_rss_data():
    url = "https://docs.google.com/spreadsheets/d/1GxUiFb00sCTytJ4XkegN8qnZ4WAmsXWGVV98eMN8F_I/edit#gid=1687625614"
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    rss_data = conn.read(spreadsheet=url, usecols=[0, 1, 2])
    return rss_data