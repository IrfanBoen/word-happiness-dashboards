import pandas as pd
import streamlit as st
import plotly.express as px

# Load the combined data
df = pd.read_csv("happiness_combined.csv")

# Sidebar Filters
st.sidebar.header("Filter Data")
year = st.sidebar.selectbox("Select Year", sorted(df["Year"].unique(), reverse=True))
region = st.sidebar.multiselect("Select Region(s)", df["Regional indicator"].unique(), default=df["Regional indicator"].unique())

# Filtered Data
filtered_df = df[(df["Year"] == year) & (df["Regional indicator"].isin(region))]

# Title
st.title("World Happiness Dashboard")

# Show Table
st.subheader(f"Happiness Data for {year}")
st.dataframe(filtered_df)

# Bar Chart: Happiness Score by Country
fig = px.bar(filtered_df.sort_values("Ladder score", ascending=False),
             x="Country name", y="Ladder score", color="Regional indicator",
             title="Happiness Score by Country")
st.plotly_chart(fig)

# Line Chart: Trend Over Time
st.subheader("Happiness Score Over Time")
selected_countries = st.multiselect("Select Countries to Compare", df["Country name"].unique())

if selected_countries:
    line_df = df[df["Country name"].isin(selected_countries)]
    fig_line = px.line(line_df, x="Year", y="Ladder score", color="Country name", markers=True,
                       title="Happiness Score Trend")
    st.plotly_chart(fig_line)
