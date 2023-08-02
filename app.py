import streamlit as st
from data_load import load_data
from visualization import display_options
from about import about_section
from wiki import wiki_section
from rss_reader import rss_reader
import pandas as pd

PAGES = {
    "About": about_section,
    "Wiki": wiki_section,
    "Visualizations": display_options,
    "RSS Reader": rss_reader
}

def main():
    data = pd.DataFrame(result, columns=['id', 'group', 'title', 'date'])

    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page_func = PAGES[selection]

    if selection == "Visualizations":
        page_func(data)
    else:
        page_func()

if __name__ == "__main__":
    main()
