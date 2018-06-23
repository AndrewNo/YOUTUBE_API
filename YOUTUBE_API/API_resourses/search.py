from YOUTUBE_API.API_resourses.model import Model
from YOUTUBE_API.response import Response


class Search(Model):
    SUB_URL = 'search'

    def get_by_keyword(self, keyword, type_search=''):
        self.params["q"] = keyword
        self.params["type"] = type_search
        response = self.client.get(self.URL + self.SUB_URL, self.params)
        results = []
        for item in response['items']:
            resp = Response(item.get('snippet')['title'], item.get('snippet')['description'], item.get('snippet')['channelTitle'])
            results.append(resp)

        return results

