# collaborative_based.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from cleaning_data import process_data


# Load and process data
raw_data = pd.read_csv("clean_data.csv")
data = process_data(raw_data)


def collaborative_filtering_recommendations(data, target_user_id, top_n=5):

    # Check if user exists
    if target_user_id not in data['ID'].values:
        print("This target user ID is not present in the data")
        return pd.DataFrame()

    # Create user-item matrix
    user_item_matrix = data.pivot_table(
        index='ID',
        columns='ProdID',
        values='Rating',
        aggfunc='mean'
    ).fillna(0)

    # Compute user similarity
    user_similarity = cosine_similarity(user_item_matrix)

    # Get target user index
    target_user_index = user_item_matrix.index.get_loc(target_user_id)

    # Get similarity scores
    user_similarities = user_similarity[target_user_index]

    # Top similar users
    k_similar_users = 10
    similar_users_indices = user_similarities.argsort()[::-1][1:k_similar_users+1]

    recommended_items = []

    for user_index in similar_users_indices:

        similar_user_ratings = user_item_matrix.iloc[user_index]

        target_user_ratings = user_item_matrix.iloc[target_user_index]

        # Items rated by similar user but not by target user
        not_rated_items = similar_user_ratings[
            (similar_user_ratings > 0) &
            (target_user_ratings == 0)
        ]

        recommended_items.extend(not_rated_items.index.tolist())

    # Remove duplicates
    recommended_items = list(set(recommended_items))

    # Limit results
    recommended_items = recommended_items[:top_n]

    # Get product details
    recommendations = data[data['ProdID'].isin(recommended_items)]

    return recommendations[['Name', 'Brand', 'Rating']]


# MAIN
if _name_ == "_main_":

    print("=== YOUR COLLABORATIVE RECOMMENDATION SYSTEM ===")

    target_user_id = 10
    top_n = 5

    recommendations = collaborative_filtering_recommendations(
        data,
        target_user_id,
        top_n
    )

    print(f"\nSUCCESS! Got {len(recommendations)} recommendations for User {target_user_id}:\n")

    print(recommendations)

    print("\nYOUR COLLABORATIVE FILTERING IS WORKING!")