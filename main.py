import requests as rq

api_key = "63db823ba71b4bff92181fe350035877"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-19&" \
      "sortBy=publishedAt&apiKey=" \
      "63db823ba71b4bff92181fe350035877"

# make a request
request = rq.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
