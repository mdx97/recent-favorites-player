import json
import spotipy.oauth2
import spotipy.util
import pyfy

config_file = open('config.json', 'r')
config = json.load(config_file)

username = input('Spotify Username: ')

token = spotipy.util.prompt_for_user_token(
    username,
    scope='user-library-read%20user-modify-playback-state',
    client_id=config['SPOTIFY_CLIENT_ID'],
    client_secret=config['SPOTIFY_CLIENT_SECRET'],
    redirect_uri=config['SPOTIFY_REDIRECT_URI'])

user_creds = pyfy.UserCreds(access_token=token)
client = pyfy.Spotify(user_creds=user_creds)

track_ids = [item['track']['id'] for item in client.user_tracks(limit=50)['items']]
client.play(track_ids=track_ids)
client.shuffle()
