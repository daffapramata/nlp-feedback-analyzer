import pandas as pd
from textblob import TextBlob

# Load the customer feedback dataset
df = pd.read_csv("customer_feedback.csv")

# Function to analyze sentiment of feedback
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity # Polarity ranges from -1 (negative) to 1 (positive)

# Apply to each row
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

# Preview results
print(df[["feedback", "sentiment_score", "sentiment_label"]])