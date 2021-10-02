from redis import Redis
import datetime


class RedisCache:
    def __init__(self):
        """Inicialize class Redis to put data on cache"""

        self.redis = Redis(
            host='localhost',
            port='6379')

    def add_cache(self, name, list_songs):
        """ Function add registry data  on Redis.
               Args
               ----
                   name(str): artists name

               Returns
               -------
                  """
        days = datetime.timedelta(days=7)
        seconds = days.total_seconds()
        self.redis.set(name, list_songs)
        self.redis.expire(name, time=int(seconds))
        print('Registro adicionado a cache')

    def get_cache(self, name):
        """ Function get registry data  on Redis.
               Args
               ----
                   name(str): artists name

               Returns
               -------
                  """
        value = self.redis.get(name)
        return value

    def registry_exists(self, name):
        """ Function to verify if registry data exists on Redis.
                Args
                ----
                    name(str): artists name

                Returns
                -------
                   """
        exists = self.redis.exists(name)
        return exists

    def delete_registry(self, name):
        """ Function to delete registry data on Redis.

                Args
                ----
                    name(str): artists name

                Returns
                -------
            """
        self.redis.delete(name)
        print('Registro em cache deletado')
