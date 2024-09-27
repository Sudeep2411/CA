# generate_data.py
import pandas as pd
import random

# Function to generate synthetic user data
def generate_user_data(num_users=100):
    user_data = []
    genres = ['Action', 'Comedy', 'Drama', 'Fantasy', 'Horror', 'Romance']
    actors = ['Actor A', 'Actor B', 'Actor C', 'Actor D', 'Actor E']

    for user_id in range(1, num_users + 1):
        watched_genres = random.sample(genres, k=random.randint(1, 3))
        favorite_actors = random.sample(actors, k=random.randint(1, 3))
        ratings = random.randint(1, 5)
        
        # Convert lists to a comma-separated string
        user_data.append([
            user_id, 
            ', '.join(watched_genres), 
            ', '.join(favorite_actors), 
            ratings
        ])

    return pd.DataFrame(user_data, columns=['User_ID', 'Watched_Genres', 'Favorite_Actors', 'Ratings'])

# Save the dataset to CSV
if __name__ == "__main__":
    user_df = generate_user_data()
    user_df.to_csv('user_data.csv', index=False)
    print(f"Data generated and saved to 'user_data.csv' with {len(user_df)} users.")
