from flask import Blueprint, redirect, request, session, url_for
import spotipy, os
from spotipy.oauth2 import SpotifyOAuth

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth_bp', __name__)

# Spotify API credentials and configuration
CLIENT_ID_SPOTIFY = os.getenv('CLIENT_ID_SPOTIFY')
CLIENT_SECRET_SPOTIFY = os.getenv('CLIENT_SECRET_SPOTIFY')
scope = 'playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private'
callback = 'http://localhost:8000/callback'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID_SPOTIFY, client_secret=CLIENT_SECRET_SPOTIFY, scope=scope, redirect_uri=callback))

@auth_bp.route('/login')
def login():
    try:
        return redirect(sp.auth_manager.get_authorize_url())
    except Exception as e:
        print(f"Error during login: {e}")
        return redirect(url_for('index'))

@auth_bp.route('/callback')
def callback():
    try:
        sp.auth_manager.get_access_token(request.args['code'])
        session['username'] = sp.me()['display_name']
    except Exception as e:
        print(f"Error during callback: {e}")
    return redirect(url_for('index'))

@auth_bp.route('/logout')
def logout():
    session['username'] = None
    return redirect(url_for('index'))
