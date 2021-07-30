from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

shared_articles = pd.read_csv('articles.csv')
shared_articles = shared_articles[shared_articles['title'].notna()]

count_vectorizer = CountVectorizer(stop_words = 'english')
count_matrix = count_vectorizer.fit_transform(shared_articles['title'])

cosine = cosine_similarity(count_matrix, count_matrix)

shared_articles = shared_articles.reset_index()
indices = pd.Series(shared_articles.index, index = shared_articles['contentId'])

def get_recommendations(title):
    index = indices[title]

    similarity_scores = list(enumerate(cosine[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:11]

    article_indices = [i[0] for i in similarity_scores]
    return shared_articles[["id",
            "index",
            "timestamp",
            "eventType",
            "contentId",
            "authorPersonId",
            "authorSessionId",
            "authorUserAgent",
            "authorRegion",
            "authorCountry",
            "contentType",
            "url",
            "title",
            "text",
            "lang",
            "total_events"]].iloc[article_indices].values.tolist()