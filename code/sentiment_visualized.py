import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data with sentiment already analyzed
df = pd.read_csv("customer_feedback.csv")

# Optional: If sentiment analysis is not done, uncomment the following lines to perform it

### ---
from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

df["sentiment_score"] = df["feedback"].apply(get_sentiment)

def classify_sentiment(score):
    if score > 0.2:
        return "Positive"
    elif score < -0.2:
        return "Negative"
    else:
        return "Neutral"

df["sentiment_label"] = df["sentiment_score"].apply(classify_sentiment)

### ---

# Count the number of each sentiment label
sentiment_counts = df["sentiment_label"].value_counts().reset_index()
sentiment_counts.columns = ["sentiment", "count"]

# Create a bar plot 
sns.set(style="whitegrid")
plt.figure(figsize=(6, 4))
sns.barplot(x="sentiment", y="count", data=sentiment_counts, palette="viridis")

# Add labels and title
plt.title("Customer Feedback Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Feedbacks")
plt.tight_layout()

# Show the plot
plt.show()
