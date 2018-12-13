from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='9c000e40b7d74f57aec50234ab78010f')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(
    q='trump',
    language='en')

print(str(top_headlines))
