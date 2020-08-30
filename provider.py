
class Provider:
    provider_username, provider_password = "",""
    _name = "Provider"

    def __init__(self, username="", password=""):
        global provider_username
        global provider_password
        
        if username != "" and password != "":
            provider_username = username
            provider_password = password

    @property
    def name(self): return self._name

    def login(self):
        pass

    def get_playlist(self, name):
        pass

    def get_playlist_names(self):
        pass


class Song:
    _title, _artist, _album = "","",""

    @property
    def title(self): return self._title

    @property
    def artist(self): return self._artist

    @property
    def album(self): return self._album


    def __init__(self, title, artist, album, provider_values={}):
        self._title = title
        self._artist = artist
        self._album = album
        self._provider_values = provider_values

class Playlist:
    _name = ""
    _songs = []

    @property
    def name(self): return self._name

    @property
    def songs(self): return self._songs

    def __getitem__(self, c):
        return self._songs[c]

    def __init__(self, name, songs=[]):
        self._name = name
        if len(songs) > 0:
            self._songs = songs



        