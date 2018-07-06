from YOUTUBE_API.API_resourses.model import Model
from YOUTUBE_API.response import Response
from YOUTUBE_API.errors import ApiErrors


class Search(Model):
    SUB_URL = 'search'
    error = ApiErrors()

    def get_by_keyword(self, keyword, type_search='', maxResults=5):
        self.params["q"] = keyword
        self.params["type"] = type_search
        self.params["maxResults"] = maxResults
        response = self.client.get(self.URL + self.SUB_URL, self.params)

        if(response.get('error')):
            print(self.error.responseError(response.get('error').get('code')))
            return []

        if (response.get('pageInfo').get('totalResults') == 0):
            print(self.error.empty_result(keyword))

        results = []
        for item in response['items']:
            resp = Response()
            resp.title = item.get('snippet')['title']
            resp.description = item.get('snippet')['description']
            resp.channelTitle = item.get('snippet')['channelTitle']
            resp.chanelId = item.get('snippet').get('channelId')
            resp.videoId = item.get('id').get('videoId')
            results.append(resp)

        return results

    def get_by_location(self, keyword):
        self.params["q"] = keyword
        self.params["type"] = 'video'
        self.params["location"] = self.client.get_user_location()
        self.params["locationRadius"] = '10mi'
        response = self.client.get(self.URL + self.SUB_URL, self.params)

        if(response.get('error')):
            print(self.error.responseError(response.get('error').get('code')))
            return []

        if (response.get('pageInfo').get('totalResults') == 0):
            print(self.error.empty_result(keyword))

        results = []
        for item in response['items']:
            resp = Response()
            resp.title = item.get('snippet')['title']
            resp.description = item.get('snippet')['description']
            resp.channelTitle = item.get('snippet')['channelTitle']
            resp.chanelId = item.get('snippet').get('channelId')
            resp.videoId = item.get('id').get('videoId')
            results.append(resp)

        return results

    def get_events(self, keyword, maxResults=5):
        self.params["q"] = keyword
        self.params["type"] = 'video'
        self.params["maxResults"] = maxResults
        self.params["eventType"] = "live"
        response = self.client.get(self.URL + self.SUB_URL, self.params)

        if(response.get('error')):
            print(self.error.responseError(response.get('error').get('code')))
            return []

        if (response.get('pageInfo').get('totalResults') == 0):
            print(self.error.empty_result(keyword))

        results = []
        for item in response['items']:
            resp = Response()
            resp.title = item.get('snippet')['title']
            resp.description = item.get('snippet')['description']
            resp.channelTitle = item.get('snippet')['channelTitle']
            resp.chanelId = item.get('snippet').get('channelId')
            resp.videoId = item.get('id').get('videoId')
            results.append(resp)

        return results

    def get_my_video(self, keyword, maxResults=5):
        self.params["q"] = keyword
        self.params["type"] = 'video'
        self.params["maxResults"] = maxResults
        self.params["forMine"] = True
        response = self.client.get(self.URL + self.SUB_URL, self.params)

        if(response.get('error')):
            print(self.error.responseError(response.get('error').get('code')))
            return []

        if (response.get('pageInfo').get('totalResults') == 0):
            print(self.error.empty_result(keyword))

        results = []
        for item in response['items']:
            resp = Response()
            resp.title = item.get('snippet')['title']
            resp.description = item.get('snippet')['description']
            resp.channelTitle = item.get('snippet')['channelTitle']
            resp.chanelId = item.get('snippet').get('channelId')
            resp.videoId = item.get('id').get('videoId')
            results.append(resp)

        return results

    def get_related_videos(self, relatedToVideoId):
        self.params["type"] = 'video'
        self.params["relatedToVideoId"] = relatedToVideoId
        response = self.client.get(self.URL + self.SUB_URL, self.params)

        if(response.get('error')):
            print(self.error.responseError(response.get('error').get('code')))
            return []

        if (response.get('pageInfo').get('totalResults') == 0):
            print(self.error.empty_result(relatedToVideoId))

        results = []
        for item in response['items']:
            resp = Response()
            resp.title = item.get('snippet')['title']
            resp.description = item.get('snippet')['description']
            resp.channelTitle = item.get('snippet')['channelTitle']
            resp.chanelId = item.get('snippet').get('channelId')
            resp.videoId = item.get('id').get('videoId')
            results.append(resp)

        return results
