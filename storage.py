import csv

all_articles = []

with open('articles.csv', encoding = "utf-8") as f:
    csv_reader = csv.reader(f)
    article_data = list(csv_reader)
    column_names = article_data[0]
    for values in article_data[1:]:
        all_articles.append(dict(zip(column_names, values)))
    
    all_articles = [d for d in all_articles if d['lang'] == 'en']


liked_articles = []
not_liked_articles = []