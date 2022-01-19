import requests
import base64
import json
import sys
import Properties

def get_client_token(client_id, client_secret):
    token_url = "https://accounts.spotify.com/api/token"
    authorization = f"{client_id}:{client_secret}"
    message_bytes = authorization.encode('ascii')
    b64_encoded = base64.b64encode(message_bytes)
    auth_encoded = b64_encoded.decode('ascii')
    header = {"Authorization": f"Basic {auth_encoded}"}
    request_body = {"grant_type": "client_credentials"}
    response = requests.post(token_url, headers=header, data=request_body)
    token = json.loads(response.text)["access_token"]
    return token


def calculate_time_signature(top_val, bottom_val):
    to_divide_by = bottom_val / 4
    time_signature = int(top_val / to_divide_by)
    return time_signature

def get_time_signature(dance, payload):
    time_sig_params = payload[dance]['time signature']
    top_val = time_sig_params[0]
    bottom_val = time_sig_params[1]
    time_sig = calculate_time_signature(top_val, bottom_val)
    return f"target_time_signature={time_sig}" 

def get_min_tempo(dance, level, payload):
    tempo_params = payload[dance]['tempo'][level]
    return f"min_tempo={tempo_params[0]}"

def get_max_tempo(dance, level, payload):
    tempo_params = payload[dance]['tempo'][level]
    return f"max_tempo={tempo_params[1]}"

def get_recommendations(seed_genres, min_tempo, max_tempo, target_time_signature, limit="limit=1", target_danceability="target_danceability=0.9"):
    full_recommendations_url = f"{recommendations_url}?{limit}&{seed_genres}&{target_danceability}&{min_tempo}&{max_tempo}&{target_time_signature}"
    response = requests.get(full_recommendations_url, headers=header)
    response_content = json.loads(response.text)

    track = response_content["tracks"][0]["name"]
    album = response_content["tracks"][0]["album"]["name"]
    artist_names = []
    for artist in response_content["tracks"][0]["artists"]:
        artist_names.append(artist["name"])

    print(f"Track: {track}")
    print(f"Album: {album}")
    print(f"Artist Names: {artist_names}")


    return response_content["tracks"][0]["external_urls"]["spotify"]


client_id = "1a7784245f6e4517b6ae96bf7463c1fc"
client_secret = "3547047b32c04af3b40ac17a2de6dcad"

token = get_client_token(client_id, client_secret)
#token = "BQBaPQzn-Yehzfp81PVxAmIShe4nEDx92HmUk0_wmV9K3CPGBwZfek4InmUtBqdBaCkFfjRKUgEv2y7THRA"

base_url = "https://api.spotify.com/v1"
recommendations_url = f"{base_url}/recommendations"
header = {"Authorization": f"Bearer {token}"}

#target_time_signature = "target_time_signature=4"
#min_tempo = "min_tempo=112" 
#max_tempo = "max_tempo=116"
limit = "limit=1"
seed_genres = "seed_genres=pop"
target_danceability = "target_danceability=0.9"


## first input will be dance type - reel, slip jig, hop jig, light jig, treble jig, hornpipe
## second input will be level - beginner, intermediate, champion

file = open("/Users/allisonlisciandro/PersonalProjects/PopJig/DanceTempos.json")
dance_data = json.load(file)
    
#dance_type = sys.argv[1]
dance_type = "hornpipe"
#dance_level = sys.argv[2]
dance_level = "beginner"


target_time_signature = get_time_signature(dance_type, dance_data)
min_tempo = get_min_tempo(dance_type, dance_level, dance_data)
max_tempo = get_max_tempo(dance_type, dance_level, dance_data)

response_url = get_recommendations(seed_genres, min_tempo, max_tempo, target_time_signature)
print(response_url)


genres_query = f"{recommendations_url}/available-genre-seeds"
genres_response = requests.get(genres_query, headers=header)
genre_response_content = json.loads(genres_response.text)

for genre in genre_response_content['genres']:
    print(genre)





## parameters

comma = "%2C"

seed_artists = []
seed_genres = []
seed_tracks = []
limit = -1
market = ""

max_acousticness = -1       ## 0.0 <= acousticness <= 1.0
max_danceability = -1       ## 0.0 <= danceability <= 1.0
max_duration_ms = -1        ## integer (in milliseconds)
max_energy = -1             ## 0.0 <= energy <= 1.0
max_instrumentalness = -1   ## 0.0 <= instrumentalness <= 1.0
max_key = -1                ## -1 <= key <= 11
max_liveness = -1           ## 0.0 <= liveness <= 1.0
max_loudness = -1           ## loudness in decibels (usually [-60, 0])
max_mode = -1               ## 0 = minor, 1 = major
max_popularity = -1         ## 0 <= popularity <= 100
max_tempo = -1              ## tempo in bpm (can't be 0 or negative)
max_time_signature = -1     ## 3 <= time_signature <= 7
max_valence = -1            ## 0.0 <= valence <= 1.0

min_acousticness = -1
min_danceability = -1
min_duration_ms = -1
min_energy = -1
min_instrumentalness = -1
min_key = -1
min_liveness = -1
min_loudness = -1
min_mode = -1
min_popularity = -1
min_tempo = -1
min_time_signature = -1
min_valence = -1

target_acousticness = -1
target_danceability = -1
target_duration_ms = -1
target_energy = -1
target_instrumentalness = -1
target_key = -1
target_liveness = -1
target_loudness = -1
target_mode = -1
target_popularity = -1
target_tempo = -1
target_time_signature = -1
target_valence = -1