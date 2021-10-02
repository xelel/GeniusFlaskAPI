from genius import Genius
from flask import Flask, request
from flask_restful import Resource, Api
from dynamo_db import DynamoDB
import json
from rediscache import RedisCache

app = Flask(__name__)
api = Api(app)


class Artist(Resource):

    def __init__(self):
        """Inicialize class Genius,dynamoDB and RedisCache"""
        self.songs_api = Genius()
        self.db = DynamoDB()
        self.cache = RedisCache()
        self.db.create_table_artists()

    def get(self, name):
        """function to get the artists name from the URL
           Args
           name(str):artist name searched
           songs(list):10 most popular songs by the artist
           ----
           Returns
           -------
              """
        #query_string verify
        if request.args.get('cache') is None:
            cache_query_string = True

        else:
            cache_query_string = eval(request.args.get('cache'))

        #number of most popular musics
        music_number = 10

        #if the registry already exists on cache select them
        if self.cache.registry_exists(name):
            songs_list = self.cache.get_cache(name)
            response = {f'{name} 10 most popularity songs': eval(songs_list),
                        'cache': cache_query_string}

        #if the registry not exists yet on cache create cache and save on dynamodb
        else:
            popular_musics = self.songs_api.get_lyrics(name, music_number)
            self.db.insert_artists_songs(name, popular_musics)
            response = {f'{name} 10 most popularity songs': popular_musics,
                        'cache': cache_query_string}
            self.cache.add_cache(name, str(popular_musics))

        #if cache param == False delete registry and insert artist on dynamoDB
        if not cache_query_string:
            self.cache.delete_registry(name)
            popular_musics = self.songs_api.get_lyrics(name, music_number)
            self.db.insert_artists_songs(name, popular_musics)

        else:
            print('cache=True, Utilizando os dados em cache')
            self.cache.get_cache(name)

        return response


api.add_resource(Artist, '/artist/<name>')

if __name__ == '__main__':
    app.run(debug=True)
