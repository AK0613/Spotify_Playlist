# This app will extract track information from a Spotify Playlist

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Used to load sensitive data to the Environment variables.
from dotenv import load_dotenv

load_dotenv()
# PrettyPrint to make it easier on the eye
import pprint

pp = pprint.PrettyPrinter()

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

# ID of the playlist
playlist = 'https://open.spotify.com/playlist/5gSSKO3y0Bziz6V9Sc7egA?si=4a0b64b7255c4839'

# Will hold the list of tracks
tracks = []
result = sp.playlist_items(playlist, fields='items.track.name, items.track.artists.name, items.track.album.name',
                           additional_types=['track'])
tracks.extend(result['items'])

# Ensures all songs are captured.
# while result['next']:
#     result = sp.next(result)
#     tracks.extend(result['items'])

pp.pprint(tracks)

# Test
