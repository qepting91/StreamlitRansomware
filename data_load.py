from sqlalchemy import create_engine, Table, MetaData, select
import pandas as pd
import streamlit as st

# Create the SQLAlchemy engine
database_url = st.secrets["database"]["url"]
engine = create_engine(database_url)

# Reflect the ransomware_fulldata table
metadata = MetaData()
ransomware_fulldata = Table('ransomware_fulldata', metadata, autoload_with=engine)

# Function to convert Google Sheets URL to CSV URL
def convert_sheets_to_csv_url(sheets_url):
    return sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")

# Read in data from CockroachDB.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def load_data():
    # Query the table
    stmt = select(ransomware_fulldata)
    with engine.connect() as connection:
        result = connection.execute(stmt)
        data = pd.DataFrame(result.fetchall(), columns=result.keys())

    # Convert the 'date' column to datetime format and reformat it to '%b %Y'
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%b %Y')

    return data.copy()

@st.cache(ttl=600)
def load_rss_data():
    url = convert_sheets_to_csv_url("https://docs.google.com/spreadsheets/d/1GxUiFb00sCTytJ4XkegN8qnZ4WAmsXWGVV98eMN8F_I/edit#gid=1687625614")
    rss_data = pd.read_csv(url, usecols=[0, 1, 2])
    return rss_data.copy()
