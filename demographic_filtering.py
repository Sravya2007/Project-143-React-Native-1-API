import pandas as pd
import numpy as np

shared_articles = pd.read_csv("articles.csv")

shared_articles = shared_articles.sort_values('total_events', ascending=False)

filtered_values = []
for values in shared_articles.head(20).values:
    column_names = shared_articles.columns
    filtered_values.append(dict(zip(column_names, values)))