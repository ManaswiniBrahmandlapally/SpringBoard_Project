# rating_based.py

import pandas as pd

# load dataset
data = pd.read_csv("clean_data.csv")

# create user-item matrix
user_item_matrix = data.pivot_table(
    index="User's ID",
    columns="Name",
    values="Rating"
)

# function to get top 15 products and their ratings for a user
def get_user_product_ratings(user_id, top_n=15):

    if user_id not in user_item_matrix.index:
        print("User not found")
        return None

    # get ratings of the user
    user_ratings = user_item_matrix.loc[user_id]

    # remove unrated items
    user_ratings = user_ratings.dropna()

    # sort by rating (highest first)
    user_ratings = user_ratings.sort_values(ascending=False)

    # get top 15
    user_ratings = user_ratings.head(top_n)

    return user_ratings


# main
if _name_ == "_main_":

    target_user_id = 10

    ratings = get_user_product_ratings(target_user_id, top_n=15)

    print("\nTop 15 Products and Ratings:\n")

    if ratings is not None:
        for product, rating in ratings.items():
            print(f"{product} → Rating: {rating}")