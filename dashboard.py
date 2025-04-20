import streamlit as st
import pandas as pd

st.set_page_config(page_title="YouTube Trending Dashboard", layout="wide")

st.title("📊 YouTube Trending Videos Dashboard")

try:
    df = pd.read_csv("data/raw_data/trending_videos.csv")
    st.write("### Top 10 Trending Videos")
    st.dataframe(df.head(10))

    st.write("### Title Length Distribution")
    df["title_length"] = df["title"].apply(len)
    st.bar_chart(df["title_length"].value_counts().sort_index())

except FileNotFoundError:
    st.error("Trending data not found. Please run the scraper first.")
