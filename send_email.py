import smtplib
import ssl
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = st.secrets.credentials.username
    password = st.secrets.credentials.password
    receiver = st.secrets.credentials.receiver
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
