from YOUTUBE_API.API_resourses.model import Model
from YOUTUBE_API.response import Response
from YOUTUBE_API.errors import ApiErrors

class Chanel(Model):
    SUB_URL = 'channels'
    error = ApiErrors()

    def get_by_chanel_id(self, channelId):
        self.params["part"] += ',contentDetails,statistics'
        self.params["id"] = channelId
        response = self.client.get(self.URL + self.SUB_URL, self.params)

        if(response.get('error')):
            print(self.error.responseError(response.get('error').get('code')))
            return []
        
        if (response.get('pageInfo').get('totalResults') == 0):
            print(self.error.empty_result(channelId))

        results = []
        for item in response['items']:
            resp = Response()
            resp.title = item.get('snippet')['title']
            resp.description = item.get('snippet')['description']
            results.append(resp)

        return results
