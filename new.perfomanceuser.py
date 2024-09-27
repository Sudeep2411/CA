# update_data.py
import pandas as pd

def add_new_user_preferences(user_id, watched_genres, favorite_actors, rating):
    new_entry = pd.DataFrame([[user_id, watched_genres, favorite_actors, rating]], 
                             columns=['User_ID', 'Watched_Genres', 'Favorite_Actors', 'Ratings'])
    new_entry.to_csv('user_data.csv', mode='a', header=False, index=False)

# Add new data and track it with DVC
add_new_user_preferences(101, ['Action', 'Comedy'], ['Actor A', 'Actor F'], 5)

