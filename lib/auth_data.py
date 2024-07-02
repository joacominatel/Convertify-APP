import os, spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from ytmusicapi import YTMusic

load_dotenv('.env')

# Spotify API credentials
CLIENT_ID_SPOTIFY = os.getenv('CLIENT_ID_SPOTIFY')
CLIENT_SECRET_SPOTIFY = os.getenv('CLIENT_SECRET_SPOTIFY')

scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private'
callback = os.getenv('CALLBACK_URL')
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID_SPOTIFY, client_secret=CLIENT_SECRET_SPOTIFY, scope=scope, redirect_uri=callback))

# Authenticate with Youtube Music
ytmusic = YTMusic('oauth.json')