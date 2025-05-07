import pandas as pd
from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the customer feedback dataset
df = pd.read_csv("customer_feedback.csv")

# Analyze sentiment of feedback
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df["sentiment_score"] = df["feedback"].apply(get_sentiment)

# Classify sentiment based on score
def classify_sentiment(score):
    if score > 0.2:
        return "Positive"
    elif score < -0.2:
        return "Negative"
    else:
        return "Neutral"

df["sentiment_label"] = df["sentiment_score"].apply(classify_sentiment)

# --- Streamlit App ---
st.title("🧠 Customer Feedback Sentiment Analysis")

st.write("Upload customer reviews and get instant insights into customer sentiment.")

# Show table
st.subheader("Raw Feedback with Sentiment Analysis")
st.dataframe(df[["feedback", "sentiment_score", "sentiment_label"]])

# Plot
st.subheader("Sentiment Distribution")

sentiment_counts = df["sentiment_label"].value_counts().reset_index()
sentiment_counts.columns = ["sentiment", "count"]

fig, ax = plt.subplots()
sns.barplot(x="sentiment", y="count", data=sentiment_counts, palette="viridis", ax=ax)
ax.set_title("Sentiment Distribution")
ax.set_xlabel("Sentiment")
ax.set_ylabel("Number of Feedbacks")

st.pyplot(fig)
st.markdown("---")
st.caption("Made by Daffa | Feedback Analysis App - May 2025")