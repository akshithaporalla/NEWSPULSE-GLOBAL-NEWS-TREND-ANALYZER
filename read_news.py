import pandas as pd

# Replace with your dataset file name
news_data = pd.read_csv('/content/news_data.csv', on_bad_lines='skip', engine='python')

# Show first 5 rows
news_data.head()