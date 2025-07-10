import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def rank_repos_from_df(df):
    if df.empty:
        return df

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(df['description'].fillna(""))
    df["seo_score"] = vectors.sum(axis=1).A1
    return df.sort_values("seo_score", ascending=False).reset_index(drop=True)

def rank_repos(csv_path):
    df = pd.read_csv(csv_path)
    tfidf = TfidfVectorizer(stop_words='english', max_features=1000)
    X = tfidf.fit_transform(df['description'].fillna(''))

    seo_score = X.sum(axis=1).A1
    vector_score = df['stars'].fillna(0) ** 0.5
    df['seo_vector_score'] = seo_score * vector_score

    return df.sort_values(by='seo_vector_score', ascending=False)

if __name__ == '__main__':
    ranked = rank_repos('../data/mit_repo_list.csv')
    ranked.to_csv('../data/ranked_repos.csv', index=False)

