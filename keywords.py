import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import numpy as np

# Load dataset
news_data = pd.read_csv("D:/akki/milestone1/news_data.csv")

# Step 1: Apply TF-IDF
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(news_data['cleaned_title'])

# Step 2: Get TF-IDF scores
scores = np.sum(X.toarray(), axis=0)
words = vectorizer.get_feature_names_out()

# Combine words with scores
word_scores = list(zip(words, scores))

# Sort by highest TF-IDF score
sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)

top_10 = sorted_words[:10]

# Combine all cleaned text
all_words = " ".join(news_data['cleaned_title']).split()

# Count frequency
word_count = Counter(all_words)

print("Top 10 Trending Keywords with Frequency:\n")

for word, score in top_10:
    print(f"{word} | Repeated: {word_count[word]} times")