import streamlit as st
import plotly.express as px
import glob
from nltk.sentiment import SentimentIntensityAnalyzer

filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()

positivity = []
negativity = []
for filepath in filepaths:
    with open(filepath, "r") as file:
        content = file.read()
        scores = analyzer.polarity_scores(content)
        positivity.append(scores['pos'])
        negativity.append(scores['neg'])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary Tone")

st.subheader("Positivity")
figure_positivity = px.line(x=dates, y=positivity,
                            labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure_positivity)

st.subheader("Negativity")
figure_negativity = px.line(x=dates, y=negativity,
                            labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure_negativity)