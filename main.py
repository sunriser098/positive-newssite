import requests as rq
import streamlit as st
from send_email import send_email

api_key = st.secrets.credentials.api_key
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-01-19&" \
      "sortBy=publishedAt&apiKey=" + api_key

# make a request
request = rq.get(url)

# Get a dictionary with data
content = request.json()

body = " "
# Access the article titles and description
for article in content["articles"]:
    if article["title"] is not None:
        if article["description"] is not None:
            body = body + article["title"] + "\n" + article["description"] + 2*"\n"
body = body.encode("utf-8")
send_email(message=body)

