import lyricsgenius as lg
import json


class Genius:

    def __init__(self):
        """Inicialize class Genius
                     """
        self.ACCESS_TOKEN = "q7zhP1ZDTjsAO22dTy7NbLFbQg8IkEpa20ckW1eGsgop0GAcbDm5FT4WvYj0BaFm"
        self.genius = lg.Genius(self.ACCESS_TOKEN,  # Client access token from Genius Client API page
                                skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"])

    def get_lyrics(self, name, k):
        """ function to get artist data.
                       Args
                       ----
                           name(str): artists name
                           k(int):songs Number on list
                       Returns
                       -------
                          """
        try:
            artist = self.genius.search_artist(name, max_songs=k, sort='popularity', per_page=10)
            artist_songs = artist.songs
            artist_songs_title = [song.title for song in artist_songs]
            return artist_songs_title

        except:  # Broad catch which will give us the name of artist and song that threw the exception
            print(f"some exception at {name}")


if __name__ == '__main__':
    g = Genius()
    v = g.get_lyrics('Frank Sinatra', 10)
    print(v)
    # g.get_lyrics('Rihanna', 10)
