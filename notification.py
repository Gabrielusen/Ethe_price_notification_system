import requests     # pulls coingecko ethereum API data
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass      # To mask password when enter
from email.message import EmailMessage


name = input('Enter your name please: ')
email = input('Enter your email address (gmail please): ')
password = getpass.getpass()
send_email_to = input('Enter email address to send to: ')
alert_amount = input('Alert if Ethereum drops below: ')


def send_email():
    # create message object instance
    msg = EmailMessage()

    # Parameter of the message
    pwd = password
    msg['From'] = email
    msg['To'] = send_email_to
    msg['Subject'] = 'ETHEREUM PRICE, BUY QUICKLY'

    # incoming message
    message = f"Hello {name} Ethereum prices are now {str(ethereum_rate)}."

    # adds in the message from the above variable
    msg.attach(MIMEText(message, 'plain'))

    # make the gmail server
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()

    # Login parameters for sending the email
    server.login(msg['From'], pwd)

    # sends the message
    server.sendmail(msg['From'], msg['To'], message)    # Come back and try send_message function
    server.quit()

    # prints to your console
    print('Successfully sent email to %s:' % (msg['To']))
    print(f"Price of Ethereum was at {str(ethereum_rate)}")


while True:
    eth_api_url = 'https://api.coingecko.com/api/v3/coins/ethereum'
    response = requests.get(
        eth_api_url,
        headers={'Accept': 'application/json'}
    )
    data = response.json()
    usd = data['market_data']['current_price']['usd']
    ethereum_rate = float(usd)
    if ethereum_rate < int(alert_amount):
        send_email()
        print('Will check back again in 3 minutes. Ctrl + C to quit.')
        time.sleep(180)
    else:
        time.sleep(300)
        print(f"Price is {str(ethereum_rate)}. Will check back again in 5 minutes. Ctrl + C to quit.")
