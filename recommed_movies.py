# recommend_movies.py
import pandas as pd

def recommend_movies(user_id, user_data):
    # Extract user preferences
    user_preferences = user_data[user_data['User_ID'] == user_id].iloc[0]
    watched_genres = set(user_preferences['Watched_Genres'])
    favorite_actors = set(user_preferences['Favorite_Actors'])

    # Recommend movies based on similar preferences
    recommendations = user_data[
        (user_data['User_ID'] != user_id) & 
        (user_data['Watched_Genres'].apply(lambda x: len(set(x).intersection(watched_genres)) > 0) |
        user_data['Favorite_Actors'].apply(lambda x: len(set(x).intersection(favorite_actors)) > 0))
    ]

    return recommendations[['User_ID', 'Watched_Genres', 'Favorite_Actors']]

# Load user data and test the recommendation function
user_df = pd.read_csv('user_data.csv')
print(recommend_movies(1, user_df))
