import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
# download once
nltk.download('stopwords')

# sample dataframe
df = pd.DataFrame({
    "text": [
        "AI is transforming the world!",
        "Python programming is very easy to learn.",
        "Stock markets are growing rapidly in 2026."
    ]
})

stop_words = set(stopwords.words('english'))

def clean_text(text):
    # lowercase
    text = text.lower()

    # remove punctuation & numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # tokenize
    tokens = text.split()

    # remove stopwords
    meaningful_tokens = [word for word in tokens if word not in stop_words]

    return " ".join(meaningful_tokens)

# create new column
df["processed_text"] = df["text"].apply(clean_text)

print(df)


#TF-IDF Vectorization

# Initialize and fit TF-IDF Vectorizer
if 'df' in locals() and 'processed_text' in df.columns:
    tfidf_vectorizer = TfidfVectorizer(max_features=5000) # You can adjust max_features as needed
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['processed_text'].astype(str))

    print(f"Shape of TF-IDF matrix: {tfidf_matrix.shape}")
else:
    print("Error: 'df' DataFrame or 'processed_text' column not found. Please ensure the preprocessing steps were successful.")

#REMOVE STOPWORDS


def remove_stopwords(text):
    # Ensure the input text is a string before splitting
    if not isinstance(text, str):
        return ""
    return " ".join([w for w in text.split() if w not in ENGLISH_STOP_WORDS])

# Check if 'processed_text' column exists before applying the function
if 'processed_text' in df.columns:
    df["processed_text"] = df["processed_text"].apply(remove_stopwords)
    print("Stopwords removed from 'processed_text' column.")
else:
    print("Error: 'processed_text' column not found. Please ensure the preprocessing steps were successful.")


  # Extracting meaningful keywords using TF-IDFS

vectorizer = TfidfVectorizer(
    stop_words="english",      # remove common words
    max_df=0.85,               # ignore very frequent words
    min_df=1,                  # ignore rare words
    ngram_range=(1,2),         # single + double keywords
    max_features=1000
)

X = vectorizer.fit_transform(df["processed_text"].astype(str))

# Sum scores safely
s_scores = np.asarray(X.sum(axis=0)).ravel()
s_words = vectorizer.get_feature_names_out()

# Top 10 meaningful keywords
top_words = [word for word, score in sorted(zip(s_words, s_scores),
                                            key=lambda x: x[1],
                                            reverse=True)[:10]]

print("Top 10 Meaningful News Keywords:")
for word in top_words:
    print(word)

# Sentiment count
import pandas as pd
from textblob import TextBlob

# Load dataset
df = pd.read_csv("news_data.csv")

# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# Print column names to verify
print("Dataset Columns:", df.columns)

# Change this if your dataset uses 'Title'
text_column = 'title' if 'title' in df.columns else 'Title'

# Sentiment function
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df['sentiment'] = df[text_column].apply(get_sentiment)

# Count sentiments
sentiment_counts = df['sentiment'].value_counts()

# Print results
print("\nSentiment Counts:")
print("Positive:", sentiment_counts.get("Positive", 0))
print("Neutral :", sentiment_counts.get("Neutral", 0))
print("Negative:", sentiment_counts.get("Negative", 0))


# Topic Modeling using LDA

# Load dataset
df = pd.read_csv("news_data.csv")

# Remove extra spaces in column names
df.columns = df.columns.str.strip()

# Use correct column name
text_column = 'title' if 'title' in df.columns else 'Title'

# Text data
text_data = df[text_column].dropna()

# Convert text to word matrix
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(text_data)

# Create LDA model
lda = LatentDirichletAllocation(n_components=3, random_state=42)

# Train model
lda.fit(X)

# Get words
words = vectorizer.get_feature_names_out()

# Print topics
for i, topic in enumerate(lda.components_):
    print(f"\nTopic {i+0}:")
    topic_words = [words[j] for j in topic.argsort()[-10:]]
    print(", ".join(topic_words))