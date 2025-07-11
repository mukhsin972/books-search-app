import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="Book Crawler", layout="wide")
st.title("📚 Books to Scrape Viewer")

try:
    with open("data/books.json", "r") as file:
        books = json.load(file)
    df = pd.DataFrame(books)

    st.dataframe(df)

    rating_filter = st.selectbox("Filter by Rating", options=["All"] + sorted(df["rating"].unique()))
    if rating_filter != "All":
        df = df[df["rating"] == rating_filter]

    st.write(f"Showing {len(df)} books")
    st.dataframe(df)
except Exception as e:
    st.error(f"Error loading data: {e}")
