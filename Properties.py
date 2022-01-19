class Property:
    name = ""

    def __init__(self, min=None, max=None, target=None):
        self.min = min
        self.max = max
        self.target = target

    def __str__(self):
        contents = []
        if (self.min is not None):
            min_string = f"min_{self.name}={self.min}&"
            contents.append(min_string)
        if (self.max is not None):
            max_string = f"max_{self.name}={self.max}&"
            contents.append(max_string)
        if (self.target is not None):
            target_string = f"target_{self.name}={self.target}&"
            contents.append(target_string)

        total_string = ""
        for item in contents:
            total_string += item
        return total_string

    def __repr__(self):
        tmp = self._str__()
        return tmp

class Acousticness(Property):
    name = "acousticness"

class Danceability(Property):
    name = "danceability"

class Duration(Property):
    name = "duration_ms"

class Energy(Property):
    name = "energy"

class Instrumentalness(Property):
    name = "instrumentalness"

class Key(Property):
    name = "key"

class Liveness(Property):
    name = "liveness"

class Loudness(Property):
    name = "loudness"

class Mode(Property):
    name = "mode"

class Popularity(Property):
    name = "popularity"

class Tempo(Property):
    name = "tempo"

class TimeSignature(Property):
    name = "time_signature"

class Valence(Property):
    name = "valence"