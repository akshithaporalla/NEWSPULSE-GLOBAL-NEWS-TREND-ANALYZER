import csv
import re

# File name
filename = "news_data.csv"

# Raw data (uncleaned)
raw_news = [
    [" AI startups raise funding!!! ", " Reuters ", "2026-02-07 "],
    ["Tech updates released***", " CNN", " 2026-02-07"],
    ["Global economy improves ", "BBC ", "2026-02-07"]
]

# Function to clean text
def clean_text(text):
    text = text.strip()                    # remove extra spaces
    text = re.sub(r'[^\w\s-]', '', text)  # remove special characters
    return text

# Cleaned data
cleaned_news = []
for title, source, date in raw_news:
    cleaned_news.append([
        clean_text(title),
        clean_text(source),
        date.strip()
    ])

# Write CSV
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Header
    writer.writerow(["Title", "Source", "Published Date"])
    
    # Rows
    writer.writerows(cleaned_news)

print(" Cleaned CSV created successfully!")