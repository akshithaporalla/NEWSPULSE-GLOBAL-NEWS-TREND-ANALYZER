

import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics import accuracy_score
from textblob import TextBlob
from collections import Counter
import re

# -----------------------------
# Title
# -----------------------------
st.title(" Newspulse Global News Trend Analyzer")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("news_data.csv")

# -----------------------------
# Show News Articles
# -----------------------------
st.subheader(" News Articles")
st.write(df['title'])

# -----------------------------
# Total News Articles
# -----------------------------
total_articles = len(df)
st.subheader(" Total News Articles")
st.write(total_articles)

# -----------------------------
# Sentiment Analysis on Titles
# -----------------------------
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df['sentiment'] = df['title'].apply(get_sentiment)

# Sentiment Counts
sentiment_counts = df['sentiment'].value_counts()

st.subheader(" Sentiment Counts")
st.write(sentiment_counts)

# -----------------------------
# Keyword Extraction
# -----------------------------
text = " ".join(df['title'].dropna())

words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())

stopwords = ["the","and","for","with","that","this","from","are","was","have","has","will","after","over","into","about"]

filtered_words = [w for w in words if w not in stopwords]

keyword_counts = Counter(filtered_words).most_common(10)

keywords = [k[0] for k in keyword_counts]
counts = [k[1] for k in keyword_counts]

# -----------------------------
# Top 10 Keywords
# -----------------------------
st.subheader(" Top 10 Keywords")
for i in keyword_counts:
    st.write(i[0], ":", i[1])

# -----------------------------
# Bar Graph for Keywords
# -----------------------------
st.subheader(" Keyword Frequency")

fig1, ax1 = plt.subplots()
ax1.bar(keywords, counts)
ax1.set_xlabel("Keywords")
ax1.set_ylabel("Frequency")
plt.xticks(rotation=45)

st.pyplot(fig1)
# -----------------------------
# Sentiment Distribution (Pie Chart)
# -----------------------------
st.subheader(" Sentiment Distribution")

fig, ax = plt.subplots()

ax.pie(
    sentiment_counts.values,
    labels=sentiment_counts.index,
    autopct='%1.1f%%',
    startangle=90
)

ax.axis('equal')  # makes pie circular

st.pyplot(fig)

# -----------------------------
# Model Accuracy
# -----------------------------

# predicted sentiment from titles
df['predicted_sentiment'] = df['title'].apply(get_sentiment)

# actual sentiment column (if exists in dataset)
true_sentiment = df['sentiment']

# predicted sentiment
pred_sentiment = df['predicted_sentiment']

# calculate accuracy
accuracy = accuracy_score(true_sentiment, pred_sentiment)

st.subheader("Model Accuracy")
st.write(round(accuracy*100,2), "%")

#topic modeling




st.subheader(" Topic Modeling")

# Use titles
text_data = df['title'].dropna()

# Text to matrix
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(text_data)

# LDA model
lda = LatentDirichletAllocation(n_components=3, random_state=42)
lda.fit(X)

# Words
words = vectorizer.get_feature_names_out()

# Create columns
col1, col2, col3 = st.columns(3)

topics = []

for topic in lda.components_:
    top_words = [words[i] for i in topic.argsort()[-10:]]
    topics.append(top_words)

# Print topics side by side
with col1:
    st.write("### Topic 1")
    st.write(topics[0])

with col2:
    st.write("### Topic 2")
    st.write(topics[1])

with col3:
    st.write("### Topic 3")
    st.write(topics[2])