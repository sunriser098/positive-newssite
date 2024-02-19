import requests as rq
import streamlit as st
from send_email import send_email

topic = "tesla"
api_key = st.secrets.credentials.api_key
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-01-19&sortBy=publishedAt&apiKey=" + api_key + "&language=en"

# make a request
request = rq.get(url)

# Get a dictionary with data
content = request.json()

body = " "
# Access the article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        if article["description"] is not None:
            body = "Subject: Today's news" + "\n" + body + article["title"] \
                   + "\n" + article["description"] + "\n" + article["url"] \
                   + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

