import pandas as pd

# --------------------------------------
# Step 1: Create Music Database
# --------------------------------------
def create_music_database():
    """
    Simulates a music database with genres, song details, and ranking metrics.
    Returns:
        pandas.DataFrame: A DataFrame containing music data.
    """
    data = {
        "Genre": ["Hip-hop", "Classical", "Bollywood", "Hip-hop", 
                  "Classical", "Bollywood", "Hip-hop"],
        "Song": ["Rap God", "Fur Elise", "Tum Hi Ho", "Sicko Mode", 
                 "Moonlight Sonata", "Chaiyya Chaiyya", "Lose Yourself"],
        "Popularity": [95, 90, 92, 89, 88, 93, 96],
        "Listen Count": [1500000, 1200000, 1300000, 1400000, 1000000, 
                         1250000, 1550000],
        "Likes": [100000, 95000, 97000, 92000, 91000, 98000, 105000],
    }
    return pd.DataFrame(data)

# --------------------------------------
# Step 2: Display Available Genres
# --------------------------------------
def display_genres(database):
    """
    Displays the unique genres available in the database.
    Args:
        database (pandas.DataFrame): The music database.
    Returns:
        list: A list of unique genres.
    """
    print("Available Genres:")
    genres = database["Genre"].unique()
    for i, genre in enumerate(genres, start=1):
        print(f"{i}. {genre}")
    return genres

# --------------------------------------
# Step 3: Fetch Recommendations
# --------------------------------------
def fetch_recommendations(database, genre):
    """
    Fetches recommended songs based on the selected genre, 
    ranked by popularity, listen count, and likes.
    Args:
        database (pandas.DataFrame): The music database.
        genre (str): Selected genre.
    Returns:
        pandas.DataFrame: A DataFrame of ranked song recommendations.
    """
    filtered_songs = database[database["Genre"] == genre]
    ranked_songs = filtered_songs.sort_values(by=["Popularity", 
                                                  "Listen Count", 
                                                  "Likes"], ascending=False)
    return ranked_songs

# --------------------------------------
# Step 4: Main Application Logic
# --------------------------------------
def music_application():
    """
    Main function to run the music recommendation application.
    """
    print("Welcome to the Music Recommendation Application!")
    
    # Initialize the music database
    music_db = create_music_database()
    
    # Display genres and get user selection
    genres = display_genres(music_db)
    try:
        choice = int(input("\nSelect a genre by entering its number: "))
        if choice < 1 or choice > len(genres):
            raise ValueError("Invalid choice! Please select a valid genre number.")
    except ValueError as e:
        print(e)
        return
    
    selected_genre = genres[choice - 1]
    print(f"\nYou selected: {selected_genre}")
    
    # Fetch and display recommendations
    recommendations = fetch_recommendations(music_db, selected_genre)
    print("\nRecommended Songs:")
    for idx, row in recommendations.iterrows():
        print(f"- {row['Song']} (Popularity: {row['Popularity']}, "
              f"Listen Count: {row['Listen Count']}, Likes: {row['Likes']})")

# --------------------------------------
# Step 5: Run the Application
# --------------------------------------
if __name__ == "__main__":
    music_application()
