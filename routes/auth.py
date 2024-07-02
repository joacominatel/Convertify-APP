from flask import Blueprint, redirect, request, session, url_for

# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth_bp', __name__)

# Spotify API credentials and configuration
from lib.auth_data import sp

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
