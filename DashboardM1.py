import csv

import pandas as pd

# File name
filename = "news_data.csv"

# Data to write
headers = ["Title", "Source", "Published Date"]

news_data = [
    ["AI startups raise funding", "Reuters", "2026-02-07"],
    ["Tech updates released", "CNN", "2026-02-07"],
    ["Global economy improves", "BBC", "2026-02-07"]
]

# Create and write to CSV file
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write headers
    writer.writerow(headers)

    # Write rows
    writer.writerows(news_data)

print("CSV file created successfully!")
import pandas as pd

# Adding more news articles
data = [
    ["AI news update", "Reuters", "2026-02-07"],
    ["Tech growth report", "CNN", "2026-02-07"],
    ["Global economy improves", "BBC", "2026-02-07"],
    ["Stock markets surge", "Bloomberg", "2026-02-07"],
    ["New climate policy announced", "Al Jazeera", "2026-02-07"],
    ["Cybersecurity threats increase", "Reuters", "2026-02-08"],
    ["SpaceX launches new rocket", "BBC", "2026-02-08"],
    ["AI beats human champions", "CNN", "2026-02-08"],
    ["Healthcare reforms introduced", "WHO", "2026-02-08"],
    ["Electric cars demand rises", "Bloomberg", "2026-02-08"],
    ["Sports tournaments resume", "ESPN", "2026-02-09"],
    ["New smartphone released", "TechCrunch", "2026-02-09"],
    ["Oil prices fluctuate", "Reuters", "2026-02-09"],
    ["Education system reforms", "BBC", "2026-02-09"],
    ["Global trade expands", "CNN", "2026-02-09"],
    ["Robotics innovation summit", "TechCrunch", "2026-02-10"],
    ["Banking sector growth", "Bloomberg", "2026-02-10"],
    ["Climate summit highlights", "Al Jazeera", "2026-02-10"],
    ["AI startup funding boom", "Reuters", "2026-02-10"],
    ["Medical breakthrough discovered", "WHO", "2026-02-10"],
    ["New gaming console launched", "IGN", "2026-02-11"],
    ["Cryptocurrency market update", "CoinDesk", "2026-02-11"],
    ["Renewable energy expansion", "BBC", "2026-02-11"],
    ["Tech conference 2026 highlights", "CNN", "2026-02-11"],
    ["International peace talks", "Al Jazeera", "2026-02-11"]
]

# Create DataFrame
df = pd.DataFrame(data, columns=["Title", "Source", "Published Date"])

# Save to CSV
df.to_csv("cleaned_data.csv", index=False)

print("File created successfully!")
print("Total Articles:", len(df))
print("Unique Sources:", df["Source"].nunique())



# Sample news data
import requests
api_key = "YOUR_API_KEY"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

response = requests.get(url)
data = response.json()
data = response.json()

print("\nTop 5 News Articles:\n")

for i, news in enumerate(news_data, start=1):
    print(f"News {i}")
    print("Title:", news[0])
    print("Source:", news[1])
    print("Published Date:", news[2])
    print("-" * 40)

# Sample data for dashboard

# Sample news data
news_data = [
    ["AI Revolutionizing Financial Markets in 2026", "Reuters", "2026-02-16"],
    ["Global Stock Markets Show Strong Recovery", "CNN Business", "2026-02-15"],
    ["India Launches New Digital Education Initiative", "The Hindu", "2026-02-14"],
    ["Climate Summit 2026 Focuses on Renewable Energy", "BBC News", "2026-02-15"],
    ["Tech Giants Invest in AI-Powered Healthcare", "Economic Times", "2026-02-16"]
]

# Create DataFrame
df = pd.DataFrame(news_data, columns=["Title", "Source", "Published Date"])

# Save to CSV file
df.to_csv("main.csv", index=False)

print("Data successfully saved to main.csv")
