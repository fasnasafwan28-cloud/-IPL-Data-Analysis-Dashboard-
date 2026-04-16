import streamlit as st
import pandas as pd

st.title("🏏 IPL Data Analysis Dashboard")

df = pd.read_csv("IPL_Dataset(2008-2024).csv")

st.sidebar.title("📊 Customize IPL Analysis")

df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year

team = st.sidebar.selectbox("Select Team", df['Teams'].unique())
year = st.sidebar.slider("Select Year", int(df['Year'].min()), int(df['Year'].max()))

filtered_df = df[(df['Teams'] == team) & (df['Year'] == year)]


st.write("### 🔍 Filtered Match Insights")
st.dataframe(filtered_df)


import plotly.express as px

win_df = df['Match_Winner'].value_counts().reset_index()
win_df.columns = ['Teams', 'Wins']


fig = px.bar(
    win_df,
    x="Teams",
    y="Wins",
    color="Teams",
    title="IPL Team Wins",
    width = 700,
    height = 800
)
fig.update_layout(
    title_text="IPL Team Wins",
    title_font=dict(size=30)
)

st.plotly_chart(fig)



analysis_type = st.selectbox(
    " Choose Analysis",
    ["Match Winners", "Toss Winners"]
)

if analysis_type == "Match Winners":
    st.write(df['Match_Winner'].value_counts())

elif analysis_type == "Toss Winners":
    st.write(df['Toss_Winner'].value_counts())


st.header("Overview")
st.write(df.head())



