import requests     # pulls coingecko ethereum API data
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass      # To mask password when enter


eth_api_url = 'https://api.coingecko.com/api/v3/coins/ethereum'
name = input('Enter your name please: ')
email = input('Enter your email address (gmail please): ')
password = getpass.getpass()
send_email_to = input('Enter email address to send to: ')
alert_amount = input('Alert if Ethereum drops below: ')


def send_email():
    # create message object instance
    msg = MIMEMultipart()

    # Parameter of the message
    pwd = password
    msg['From'] = email
    msg['To'] = send_email_to
    msg['Subject'] = 'Present Ethereum Price'

    # incoming message
