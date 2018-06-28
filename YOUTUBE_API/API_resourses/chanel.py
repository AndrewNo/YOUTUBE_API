from YOUTUBE_API.API_resourses.model import Model
from YOUTUBE_API.response import Response

class Chanel(Model):
    SUB_URL = 'channels'

    def get_by_chanel_id(self, channelId):
        self.params["part"] += ',contentDetails,statistics'
        self.params["id"] = channelId
        response = self.client.get(self.URL + self.SUB_URL, self.params)

        if (response.get('pageInfo').get('totalResults') == 0):
            print('Nothing was found for your request')

        results = []
        for item in response['items']:
            resp = Response()
            resp.title = item.get('snippet')['title']
            resp.description = item.get('snippet')['description']
            results.append(resp)

        return results
