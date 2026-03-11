# content_based.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load data
data = pd.read_csv("clean_data.csv")

# Basic cleaning
data['Name'] = data['Name'].astype(str).str.lower().str.strip()
data['Tags'] = data['Tags'].astype(str).str.lower().str.strip()
data['Tags'] = data['Tags'].fillna("")


def content_based_recommendations(data, item_name, top_n=10):

    # Check if item exists (partial match allowed)
    matches = data[data['Name'].str.contains(item_name.lower(), na=False)]

    if matches.empty:
        print("This item is not present in the data")
        return pd.DataFrame()

    # TF-IDF Vectorization
    tfidf = TfidfVectorizer(stop_words='english')

    tfidf_matrix = tfidf.fit_transform(data['Tags'])

    # Cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix)

    # Get index of selected item
    idx = matches.index[0]

    # Get similarity scores
    similarity_scores = list(enumerate(cosine_sim[idx]))

    # Sort scores
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Get top recommendations
    similarity_scores = similarity_scores[1:top_n+1]

    product_indices = [i[0] for i in similarity_scores]

    recommendations = data.iloc[product_indices]

    return recommendations[['Name', 'Brand', 'Rating']]


# MAIN
if _name_ == "_main_":

    print("=== YOUR CONTENT BASED RECOMMENDATION SYSTEM ===")

    item_name = "toothpaste"
    top_n = 10

    recommendations = content_based_recommendations(
        data,
        item_name,
        top_n
    )

    print(f"\nSUCCESS! Got {len(recommendations)} recommendations for '{item_name}':\n")

    print(recommendations)