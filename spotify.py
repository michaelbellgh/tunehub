from provider import *
import tekore as tk

class Spotify( Provider ):

    _clientsecret, _clientid = "",""
    _myuser=""
    api = None
    def __init__(self, username, password, clientid="", clientsecret="", my_username=""):
        Provider.__init__(self)
        self._name = "Spotify"

        if clientid != "":
            self._clientid = clientid
        if clientsecret != "":
            self._clientsecret = clientsecret

        if my_username != "":
            self._myuser = my_username
        
        self.login()

    def login(self):      
        token = tk.request_client_token(self._clientid, self._clientsecret)
        self.api = tk.Spotify(token)

    def get_playlist(self, name):
        playlists = self.api.playlists(self._myuser)
        for item in playlists.items:
            if item.name == name:
                songs = self.api.playlist_items(item.id)
                provider_songs = []
                for song in songs.items:
                    s = Song(song.track.name, song.track.artists[0].name, song.track.album.name, provider_values=song)
                    provider_songs.append(s)
                return Playlist(name, songs=provider_songs)
        return None

    def get_playlist_names(self):
        playlists = self.api.playlists(self._myuser)
        names = [x.name for x in playlists.items]
        return names
    
    def test(self):
        album = self.api.album('3RBULTZJ97bvVzZLpxcB0j')
        for track in album.tracks.items:
            print(track.track_number, track.name)
        