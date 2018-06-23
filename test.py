from YOUTUBE_API.client import Client

client = Client('AIzaSyBoyPSgmbLVO1wW7iKFXaMxovwOO_RfWqI')

i = 1
for item in client.Search.get_by_keyword('python'):
    print(str(i) + '. ' + item.channelTitle)
    print(item.title)
    print(item.description)
    i += 1
    print('-------------------------')