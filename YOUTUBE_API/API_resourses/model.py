class Model:
    URL = "https://www.googleapis.com/youtube/v3/"
    params = {
        "maxResults": 5,
        "part": "snippet",
    }

    def __init__(self, client):
        self.client = client
        self.params["key"] = self.client.api_key
