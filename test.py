from YOUTUBE_API.client import Client

client = Client('AIzaSyBoyPSgmbLVO1wW7iKFXaMxovwOO_RfWqI')

# i = 1
# for item in client.Search.get_by_keyword('python'):
#     print(str(i) + '. ' + item.channelTitle)
#     print(item.title)
#     print(item.description)
#     i += 1
#     print('-------------------------')


# i = 1
# for item in client.Search.get_by_location('surfing''):
#     print(str(i) + '. ' + item.channelTitle)
#     print(item.title)
#     print(item.description)
#     i += 1
#     print('-------------------------')

# i = 1
# for item in client.Search.get_events('news'):
#     print(str(i) + '. ' + item.channelTitle)
#     print(item.title)
#     print(item.description)
#     i += 1
#     print('-------------------------')
# i = 1
# for item in client.Search.get_by_keyword('python'):
#     for rel_vid in client.Search.get_related_videos(item.videoId):
#         print(str(i) + '. ' + rel_vid.channelTitle)
#         print(rel_vid.title)
#         print(rel_vid.description)
#         i += 1
#         print('-------------------------')

i = 1
for item in client.Search.get_by_keyword('python'):
    for rel_vid in client.Chanel.get_by_chanel_id(item.chanelId):
        print(str(i) + '. ' + rel_vid.channelTitle)
        print(rel_vid.title)
        print(rel_vid.description)
        i += 1
        print('-------------------------')