# Pop Jig
_This project is still in progress. Currently, it can return recommendations based on genre only (using artists and songs as seeds is the next step!)._


## Background

I have been irish dancing since I was 8 years old. A big part of Irish Dance has always been performance, specifically around St. Patrick's Day! While dancing to traditional music is fun, sometimes it's nice to change it up, and dance to songs that the general population listens to. However, using the same two songs (usually [Uptown Funk](https://open.spotify.com/album/3vLaOYCNCzngDf8QdBg2V1?highlight=spotify:track:32OlwWuMpZ6b0aN2RZOeMS) by Bruno Mars and [Galway Girl](https://open.spotify.com/album/3T4tUhGYeRNVUGevb0wThu?highlight=spotify:track:0afhq8XCExXpqazXczTSve) by Ed Sheeran) can get a little redundant.

When I started college I joined the Irish Dance Club and began performing a lot more to more modern songs. After learning a 5 minute performance to a song that did _not_ fit irish dancing well, I realized that finding songs to fit wasn't quite as easy as I first imagined. So, my idea for Pop Jig was born. The intent behind Pop Jig (named in reference to a type of dance called Hop Jig!), is to help recommend songs that will best fit with Irish Dance choreography. While some of the results in of themselves can be quite amusing, I hope to someday share this with other members of the Irish Dance community to help them quickly find songs that will work best for their choreo!

## How it Works

Pop Jig works by using the Spotify API to get recommendations based on the tempo and time signature for each kind of Irish Dance. Using seed genres, artists, and songs, it is then able to generate recommendations for songs that best fit the type and level of dance inputted. Below is a general description of what inputs can be specified:

| Input            | Description                                                              | Required | Default |
|------------------|--------------------------------------------------------------------------|----------|---------|
| Type             | One of: reel, light jig, slip jig, hop jig, treble jig, hornpipe         | Yes      |         |
| Level            | One of: beginner, intermediate, champion                                 | Yes      |         |
| Seeds            | Mix of seed genres, artists, and songs. 1 ≤ Number of Seeds ≤ 5          | Yes      |         |
| Limit            | Max number of recommendations to return. 1 <= limit <= 100               | No       | 20      |
| Acousticness     | Can specify min, max, and target. 0.0 <= acousticness <= 1.0             | No       |         |
| Danceability     | Can specify min, max, and target. 0.0 <= danceability <= 1.0             | No       |         |
| Duration         | Can specify min, max, and target. Integer (in milliseconds)              | No       |         |
| Energy           | Can specify min, max, and target. 0.0 <= energy <= 1.0                   | No       |         |
| Instrumentalness | Can specify min, max, and target. 0.0 <= instrumentalness <= 1.0         | No       |         |
| Key              | Can specify min, max, and target. -1 <= key <= 11                        | No       |         |
| Liveness         | Can specify min, max, and target. 0.0 <= liveness <= 1.0                 | No       |         |
| Loudness         | Can specify min, max, and target. Loudness in decibels (usually [-60, 0]) | No       |         |
| Mode             | Can specify min, max, and target. 0 = minor, 1 = major                   | No       |         |
| Popularity       | Can specify min, max, and target. 0 <= popularity <= 100                 | No       |         |
| Valence          | Can specify min, max, and target. 0.0 <= valence <= 1.0                  | No       |         |

For more information on how to specify each input, run ```python ./PopJig.py --help```

### Notes
* This program is far from perfect. The Spotify API only provides estimations for time signature and tempo for each song. This may mean that some song recommendations are not ideal.
* Treble jig is performed at a very uncommon tempo. In order to account for that, tempo has a higher priority than time signature. Even so, song recommendations for treble jig generally do not seem to work well. :(
