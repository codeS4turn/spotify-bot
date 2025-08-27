import spotipy
from spotipy.oauth2 import SpotifyOAuth

# --- CONFIGURATION ---
# Replace these with your actual Spotify app credentials
CLIENT_ID = 'dbc56fef15ed4de6a6d9cfb15d86011a'
CLIENT_SECRET = '13d5dc588b464a00b659f8c53867898a'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'  # Must match your Spotify app settings
SCOPE = 'playlist-modify-public user-read-playback-state user-modify-playback-state'

# --- AUTHENTICATION ---
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE
))

def search_and_add_to_playlist(song_name, playlist_id):
    # Search for the song
    results = sp.search(q=song_name, limit=1, type='track')
    tracks = results.get('tracks', {}).get('items', [])
    if not tracks:
        print(f"No track found for '{song_name}'")
        return
    track_id = tracks[0]['id']
    track_name = tracks[0]['name']
    print(f"Found track: {track_name} (ID: {track_id})")

    # Add to playlist
    sp.playlist_add_items(playlist_id, [track_id])
    print(f"Added '{track_name}' to playlist {playlist_id}")

if __name__ == "__main__":
    # Example usage
    playlist_id = 'YOUR_PLAYLIST_ID'
    song_name = input("Enter song name to add to playlist: ")
    search_and_add_to_playlist(song_name, playlist_id)