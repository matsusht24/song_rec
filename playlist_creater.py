import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
import sys

def findArtist(artist_name, playlist_id):
    results = sp.search(q=artist_name, type='artist')
    artists = results['artists']['items']

    if not artists:
        print("Artist not found.")
    else:
        artist_id = artists[0]['id']  # Take the first artist if multiple are found

        # Fetch the top tracks for the artist
        top_tracks = sp.artist_top_tracks(artist_id, country='US')  # You can specify a different country if desired

        # Get the track IDs of the top 5 tracks
        track_ids = [track['id'] for track in top_tracks['tracks'][:5]]

        # Add the top tracks to the playlist
        if track_ids:
            sp.playlist_add_items(playlist_id, track_ids)
            print(f"Added top 5 tracks of '{artist_name}' to the playlist.")
        else:
            print("No tracks found for the artist.")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIPY_CLIENT_ID'),
                                               client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
                                               redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
                                               scope='playlist-modify-private'))


user_id = sp.me()['id']  # Get current user ID
usr_check = input(f"is this your user id {user_id}: Y/N")
print("Wrong account fix env") or sys.exit(1) if usr_check != "Y" else print("Sweet lets make your playlist")

playlist_name = input('Enter Playlist Name: ')  # Name of the playlist

# Fetch current user's playlists
playlists = sp.current_user_playlists()

# Create a set of playlist names for quick lookup
playlist_names = {playlist['name'] for playlist in playlists['items']}

# Checks if the playlist name is already taken
print(input("Playlist already exist\n Give another name: ") if playlist_name in playlist_names else "Name saved.")
playlist_description = input('Enter your playlist Description: ') # Description of playlist

# Create playlist
new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)

Artist = schedule = [
        "Afrojack", 
        "Steve Aoki", 
        "Alison Wonderland", 
        "Illenium",
        "CrankDat", 
        "Riot Ten", 
        "Ghastly, Ghengar", 
        "Level Up", 
        "Hvdes", 
        "Anger Fist",
        "Softest Chill", 
        "Trivecta", 
        "Adventure Clue", 
        "Martin Garrix", 
        "Seven Lion"

]


print(f"Playlist created: {new_playlist['name']}")

