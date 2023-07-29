import pandas as pd
import streamlit as st

# Function to convert Google Sheets URL to CSV URL
def convert_sheets_to_csv_url(sheets_url):
    return sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")

# Read in data from the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data():
    url = convert_sheets_to_csv_url("https://docs.google.com/spreadsheets/d/1GxUiFb00sCTytJ4XkegN8qnZ4WAmsXWGVV98eMN8F_I/edit#gid=2084622647")
    data = pd.read_csv(url, parse_dates=['Date'], date_parser=lambda x: pd.to_datetime(x, format='%b %d, %Y'))
    data['Date'] = data['Date'].dt.strftime('%b %Y')
    return data.copy()

@st.cache_data(ttl=600)
def load_rss_data():
    url = convert_sheets_to_csv_url("https://docs.google.com/spreadsheets/d/1GxUiFb00sCTytJ4XkegN8qnZ4WAmsXWGVV98eMN8F_I/edit#gid=1687625614")
    rss_data = pd.read_csv(url, parse_dates=['Date'], date_parser=lambda x: pd.to_datetime(x, format='%b %d, %Y'))
    data['Date'] = data['Date'].dt.strftime('%b %Y')
    return rss_data.copy()

