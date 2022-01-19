import requests
import base64
import json

base_url = "https://api.spotify.com/v1"
recommendations_url = f"{base_url}/recommendations"
genres_url = f"{recommendations_url}/available-genre-seeds"

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
    return time_sig

def get_min_tempo(dance, level, payload):
    tempo_params = payload[dance]['tempo'][level]
    return tempo_params[0]

def get_max_tempo(dance, level, payload):
    tempo_params = payload[dance]['tempo'][level]
    return tempo_params[1]

def create_seeds_string(seed_type, seed_values):
    num_seeds = len(seed_values)
    if (num_seeds == 0):
        return ""

    comma = "%2C"
    seed_string = f"seed_{seed_type}="
    for index in range(0, num_seeds):
        value = seed_values[index]
        seed_string += f"{value}"
        if (index < (num_seeds - 1)):
            seed_string += comma
    seed_string += "&"
    return seed_string

def get_genres(token):
    header = {"Authorization": f"Bearer {token}"}
    genres_response = requests.get(genres_url, headers=header)
    genre_response_content = json.loads(genres_response.text)

    all_genres = str(genre_response_content['genres'])
    return all_genres.replace("[", "").replace("]", "")

def get_song_id(token, song_title, artist):
    header = {"Authorization": f"Bearer {token}"}
    song_title = song_title.replace(" ", "%20")
    artist = artist.replace(" ", "%20")
    search_url = f"https://api.spotify.com/v1/search?q=track:{song_title}%20artist:{artist}&type=track&limit=1"
    response = requests.get(search_url, headers=header)
    response_content = json.loads(response.text)
    print(response_content["tracks"]["items"][0]["id"])

def get_recommendations(token, seeds, properties=[], limit=20):
    header = {"Authorization": f"Bearer {token}"}
    full_recommendations_url = f"{recommendations_url}?{seeds}"
    for property in properties:
        full_recommendations_url += str(property)
    full_recommendations_url += f"limit={limit}"

    print(full_recommendations_url)

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


