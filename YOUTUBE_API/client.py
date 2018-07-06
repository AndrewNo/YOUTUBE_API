from YOUTUBE_API.API_resourses.chanel import Chanel
from YOUTUBE_API.API_resourses.search import Search
from YOUTUBE_API.API_resourses.video import Video
import requests


class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.Search = Search(self)
        self.Chanel = Chanel(self)
        self.Video = Video(self)

    def get(self, url, params):
        return requests.get(url, params=params).json()

    def get_user_location(self):
        send_url = 'http://ipinfo.io/json'
        r = requests.get(send_url).json()
        return r.get('loc')
