import provider, spotify, csv

def write_playlist_obj_to_csv(playlist_obj, outputfile):
    headers = ["Title", "Artist", "Album"]
    writer = csv.DictWriter(open(outputfile, 'w', newline=''), fieldnames=headers)

    writer.writeheader()

    for song in playlist_obj.songs:
        writer.writerow({"Title" : song.title, "Artist" : song.artist, "Album" : song.album})


def export_all_playlists_to_csv(provider_instance, directory):
    names = provider_instance.get_playlist_names()
    for playlist in names:
        playlist_obj = provider_instance.get_playlist(playlist)
        write_playlist_obj_to_csv(playlist_obj, directory + "\\" + playlist + ".csv")