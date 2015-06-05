import os

root_folder = "/mnt/Data/Music/"


class Main:
    @staticmethod
    def get_all_artists():
        for artist in os.listdir(root_folder):
            if os.path.isdir(os.path.join(root_folder, artist)):
                absolute_path = os.path.join(root_folder, artist)
                icon_name = Main.get_icon_name(absolute_path, 0)
                if icon_name != None:
                    Main.set_icon(absolute_path, icon_name)
                Main.get_all_albums_by_artist(absolute_path)

    @staticmethod
    def get_all_albums_by_artist(artist_folder):
        for album in os.listdir(artist_folder):
            if os.path.isdir(os.path.join(artist_folder, album)):
                absolute_path = os.path.join(artist_folder, album)
                icon_name = Main.get_icon_name(absolute_path, 1)
                if icon_name != None:
                    Main.set_icon(absolute_path, icon_name)

    @staticmethod
    def get_icon_name(folder, is_album):
        for file in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, file)):
                if is_album:
                    if file.startswith("cover."):
                        return file
                else:
                    if file.startswith("artist."):
                        return file
        return None

    @staticmethod
    def set_icon(folder, icon):
        response = os.system('gvfs-set-attribute -t string %r metadata::custom-icon "file://%s"' % (folder, os.path.join(folder, icon)))
        if response != 0:
            print("Error while setting cover for: " + folder)

Main.get_all_artists()
