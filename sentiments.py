import pandas as pd

# Load dataset
df = pd.read_csv("news_data.csv")

# Count sentiments
sentiment_counts = df['sentiment'].value_counts()

# Print counts
# -----------------------------
# Sentiment Analysis
# -----------------------------
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment to titles
df['sentiment'] = df['title'].apply(get_sentiment)

# Count sentiments
sentiment_counts = df['sentiment'].value_counts()

# Display sentiment counts
st.subheader("Sentiment Counts")

st.write("Positive:", sentiment_counts.get("Positive",0))
st.write("Neutral:", sentiment_counts.get("Neutral",0))
st.write("Negative:", sentiment_counts.get("Negative",0))