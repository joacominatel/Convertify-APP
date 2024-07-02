"""
Convertify:
    - Convertify is a simple web application that converts playlist from spotify to youtube Music.
    - It uses the Spotify API and ytmusicapi (unofficial API for youtube music) to convert the playlist.
"""
import os, datetime, time
from dotenv import load_dotenv
from flask import Flask, session, render_template, jsonify
from lib.auth_data import sp, ytmusic

load_dotenv('.env') # Load environment variables

# Flask app configuration
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# session management
@app.before_request
def before_request():
    if 'username' not in session:
        session['username'] = None

# Import authentication routes
from routes import auth_bp

app.register_blueprint(auth_bp)

# import func
def convertToYoutubeMusic(playlist_id):
        try:
            playlist_name = sp.playlist(playlist_id)['name']
            playlist = sp.playlist_tracks(playlist_id)
            tracks = playlist['items']
        except:
            return jsonify({'success': False, 'error': 'Could not fetch playlist tracks.'}), 400
        
        new_playlist = ytmusic.create_playlist(playlist_name, description='Converted by Convertify')
        not_added = []
        added = []
        process = len(tracks)
        start_time = time.time()

        for track in tracks:
            try:
                track_name = track['track']['name']
                artist = track['track']['artists'][0]['name']
                search_results = ytmusic.search(f'{track_name} {artist}')
                ytmusic.add_playlist_items(new_playlist, [search_results[0]['videoId']])
                added.append(track_name)
            except:
                not_added.append(track_name)
            finally:
                process -= 1
                final_time = time.time() - start_time
                print(f'{process} tracks left to add')
                socketio.emit('update', {'tracks_left': process})
        return {
            'success': True,
            'message': f'Playlist {playlist_name} has been converted successfully in {str(datetime.timedelta(seconds=final_time))}.',
            'playlist_id': new_playlist,
            'not_added': not_added,
            'added': added,
            'time': str(datetime.timedelta(seconds=final_time))
        }

# Routes
@app.route('/')
def index():
    if session['username']:
        playlists = sp.current_user_playlists()['items']
        return render_template('index.html', username=session['username'], playlists=playlists)
    return render_template('index.html', username=None)

@app.route('/convert/<playlist_id>', methods=['POST'])
def convert(playlist_id):
    response = convertToYoutubeMusic(playlist_id)
    return jsonify(response), 200 if response['success'] else 500


if __name__ == '__main__':
    from flask_socketio import SocketIO
    socketio = SocketIO(app)
    socketio.run(app, port=8000, debug=True)