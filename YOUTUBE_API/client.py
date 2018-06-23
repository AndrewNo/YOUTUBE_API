from YOUTUBE_API.API_resourses.chanel import Chanel
from YOUTUBE_API.API_resourses.search import Search
import requests


class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.Search = Search(self)
        self.Chanel = Chanel(self)

    def get(self, url, params):
        return requests.get(url, params=params).json()
