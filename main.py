# This app will extract track information from a Spotify Playlist

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# Used to load sensitive data to the Environment variables.
from dotenv import load_dotenv

# Used to write to csv
import csv

# Load credentials to environment
load_dotenv()
auth_manager = SpotifyClientCredentials()
# Instantiate Spotipy
sp = spotipy.Spotify(auth_manager=auth_manager)

# ID of the playlist
playlist = 'https://open.spotify.com/playlist/5gSSKO3y0Bziz6V9Sc7egA?si=4a0b64b7255c4839'

# Will hold the list of tracks
tracks = []

# Get playlist items but filter by track name, artist, and album
result = sp.playlist_items(playlist,
                           fields='items.track.name, items.track.artists.name',
                           additional_types=['track'])
# Add results to the list
tracks.extend(result['items'])

with open('Wedding Songs.csv', 'w', encoding='UTF8', newline='') as file:
    header = ['Artist', 'Song']
    writer = csv.writer(file, escapechar=' ', quoting=csv.QUOTE_NONE)
    writer.writerow(header)

    for values in tracks:
        # Convert dictionary items into a string
        temp = str(values)
        # Cleanup
        temp = temp.replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace(':', '').replace("\"",
                                                                                                                 "")
        temp = temp.replace('track', '').replace('\'', '').replace('album name', '').replace('artists name',
                                                                                             '').replace(
            'name', '')
        temp = " ".join(temp.split())
        writer.writerow([temp])
