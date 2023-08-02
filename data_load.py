import psycopg2
import pandas as pd
import streamlit as st

# Get the database URL from secrets
database_url = st.secrets["database"]["url"]

# Function to convert Google Sheets URL to CSV URL
def convert_sheets_to_csv_url(sheets_url):
    return sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")

# Read in data from CockroachDB.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data():
    # Connect to the database
    conn = psycopg2.connect(database_url)
    cur = conn.cursor()

    # Query the table
    cur.execute("SELECT * FROM ransomware")
    result = cur.fetchall()

    # Fetch column names from cursor description
    col_names = [desc[0] for desc in cur.description]

    # Create a DataFrame from the result
    data = pd.DataFrame(result, columns=col_names)

    # Convert the 'date' column to datetime format and reformat it to '%b %d, %Y'
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%b %d, %Y')

    # Close the cursor and connection
    cur.close()
    conn.close()

    return data.copy()
@st.cache_data(ttl=600)
def load_rss_data():
    url = convert_sheets_to_csv_url("https://docs.google.com/spreadsheets/d/1GxUiFb00sCTytJ4XkegN8qnZ4WAmsXWGVV98eMN8F_I/edit#gid=1687625614")
    rss_data = pd.read_csv(url, usecols=[0, 1, 2])
    return rss_data.copy()
