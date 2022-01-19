import ApiCalls as apic
import Properties
import argparse
import json


parser = argparse.ArgumentParser(description='Get Seeds and song properties')

parser.add_argument('--max_acousticness', type=float, default=None, help='0.0 <= acousticness <= 1.0', required=False)
parser.add_argument('--max_danceability', type=float, default=None, help='0.0 <= danceability <= 1.0', required=False)
parser.add_argument('--max_duration', type=int, default=None, help='integer (in milliseconds)', required=False)
parser.add_argument('--max_energy', type=float, default=None, help='0.0 <= energy <= 1.0', required=False)
parser.add_argument('--max_instrumentalness', type=float, default=None, help='0.0 <= instrumentalness <= 1.0', required=False)
parser.add_argument('--max_key', type=int, default=None, help='-1 <= key <= 11', required=False)
parser.add_argument('--max_liveness', type=float, default=None, help='0.0 <= liveness <= 1.0', required=False)
parser.add_argument('--max_loudness', type=int, default=None, help='loudness in decibels (usually [-60, 0])', required=False)
parser.add_argument('--max_mode', type=int, default=None, help='0 = minor, 1 = major', required=False)
parser.add_argument('--max_popularity', type=int, default=None, help='0 <= popularity <= 100', required=False)
parser.add_argument('--max_valence', type=float, default=None, help='0.0 <= valence <= 1.0', required=False)

parser.add_argument('--min_acousticness', type=float, default=None, help='0.0 <= acousticness <= 1.0', required=False)
parser.add_argument('--min_danceability', type=float, default=None, help='0.0 <= danceability <= 1.0', required=False)
parser.add_argument('--min_duration', type=int, default=None, help='integer (in milliseconds)', required=False)
parser.add_argument('--min_energy', type=float, default=None, help='0.0 <= energy <= 1.0', required=False)
parser.add_argument('--min_instrumentalness', type=float, default=None, help='0.0 <= instrumentalness <= 1.0', required=False)
parser.add_argument('--min_key', type=int, default=None, help='-1 <= key <= 11', required=False)
parser.add_argument('--min_liveness', type=float, default=None, help='0.0 <= liveness <= 1.0', required=False)
parser.add_argument('--min_loudness', type=int, default=None, help='loudness in decibels (usually [-60, 0])', required=False)
parser.add_argument('--min_mode', type=int, default=None, help='0 = minor, 1 = major', required=False)
parser.add_argument('--min_popularity', type=int, default=None, help='0 <= popularity <= 100', required=False)
parser.add_argument('--min_valence', type=float, default=None, help='0.0 <= valence <= 1.0', required=False)

parser.add_argument('--target_acousticness', type=float, default=None, help='0.0 <= acousticness <= 1.0', required=False)
parser.add_argument('--target_danceability', type=float, default=None, help='0.0 <= danceability <= 1.0', required=False)
parser.add_argument('--target_duration', type=int, default=None, help='integer (in milliseconds)', required=False)
parser.add_argument('--target_energy', type=float, default=None, help='0.0 <= energy <= 1.0', required=False)
parser.add_argument('--target_instrumentalness', type=float, default=None, help='0.0 <= instrumentalness <= 1.0', required=False)
parser.add_argument('--target_key', type=int, default=None, help='-1 <= key <= 11', required=False)
parser.add_argument('--target_liveness', type=float, default=None, help='0.0 <= liveness <= 1.0', required=False)
parser.add_argument('--target_loudness', type=int, default=None, help='loudness in decibels (usually [-60, 0])', required=False)
parser.add_argument('--target_mode', type=int, default=None, help='0 = minor, 1 = major', required=False)
parser.add_argument('--target_popularity', type=int, default=None, help='0 <= popularity <= 100', required=False)
parser.add_argument('--target_valence', type=float, default=None, help='0.0 <= valence <= 1.0', required=False)

parser.add_argument('--limit', type=int, help='1 <= number of recommendations to get <= 100, default 20', required=False)
parser.add_argument('--genres', type=str, default="", help='seed genres', required=False)
parser.add_argument('--artists', type=str, default="", help='seed artists', required=False)
parser.add_argument('--tracks', type=str, default="", help='seed tracks', required=False)

parser.add_argument('--dance_type', type=str, help='type of dance', required=True)
parser.add_argument('--dance_level', type=str, help='level of dance', required=True)

args = parser.parse_args()

client_id = "1a7784245f6e4517b6ae96bf7463c1fc"
client_secret = "3547047b32c04af3b40ac17a2de6dcad"

token = apic.get_client_token(client_id, client_secret)

header = {"Authorization": f"Bearer {token}"}

seeds_dict = {"genres": [], "artists": [], "tracks": []}


acousticness = Properties.Acousticness(min=args.min_acousticness, max=args.max_acousticness, target=args.target_acousticness)
danceability = Properties.Danceability(min=args.min_danceability, max=args.max_danceability, target=args.target_danceability)
duration = Properties.Duration(min=args.min_duration, max=args.max_duration, target=args.target_duration)
energy = Properties.Energy(min=args.min_energy, max=args.max_energy, target=args.target_energy)
instrumentalness = Properties.Instrumentalness(min=args.min_instrumentalness, max=args.max_instrumentalness, target=args.target_instrumentalness)
key = Properties.Key(min=args.min_key, max=args.max_key, target=args.target_key)
liveness = Properties.Liveness(min=args.min_liveness, max=args.max_liveness, target=args.target_liveness)
loudness = Properties.Loudness(min=args.min_loudness, max=args.max_loudness, target=args.target_loudness)
mode = Properties.Mode(min=args.min_mode, max=args.max_mode, target=args.target_mode)
popularity = Properties.Popularity(min=args.min_popularity, max=args.max_popularity, target=args.target_popularity)
valence = Properties.Valence(min=args.min_valence, max=args.max_valence, target=args.target_valence)

file = open("/Users/allisonlisciandro/PersonalProjects/PopJig/DanceTempos.json")
dance_data = json.load(file)
    
dance_type = args.dance_type
dance_level = args.dance_level


target_time_signature = apic.get_time_signature(dance_type, dance_data)

min_tempo = apic.get_min_tempo(dance_type, dance_level, dance_data)
max_tempo = apic.get_max_tempo(dance_type, dance_level, dance_data)

tempo = Properties.Tempo(min=min_tempo, max=max_tempo)
time_signature = Properties.TimeSignature(target=target_time_signature, min=target_time_signature, max=target_time_signature)

properties = [acousticness, danceability, duration, energy, instrumentalness, key, liveness, loudness, mode, popularity, tempo, time_signature, valence]

genres_list = args.genres.replace(" ", "").split(",")
if ("" not in genres_list):
    seeds_dict["genres"] = genres_list

artists_list = args.artists.replace(" ", "").split(",")
if ("" not in artists_list):
    seeds_dict["artists"] = artists_list

tracks_list = args.tracks.replace(" ", "").split(",")
if ("" not in tracks_list):
    seeds_dict["tracks"] = tracks_list

seeds_string = ""
for seed in seeds_dict:
    seeds_string += apic.create_seeds_string(seed, seeds_dict[seed])

try:
    apic.get_recommendations(token, seeds_string, properties=properties, limit=1)
except:
    #target_tempo = (min_tempo + max_tempo) / 2
    #tempo = Properties.Tempo(target=target_tempo, min=(target_tempo-10), max=(target_tempo+10))
    time_signature = Properties.TimeSignature(target=target_time_signature)
    properties = [acousticness, danceability, duration, energy, instrumentalness, key, liveness, loudness, mode, popularity, tempo, time_signature, valence]
    apic.get_recommendations(token, seeds_string, properties=properties, limit=1)


#apic.get_song_id(token, "Prayer X", "King Gnu")

