import smtplib
import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'xxxxx@hotmail.com'
PASSWORD = 'xxxxx'


def sendMail(hostname, offline_time):
    # Set up the SMTP server.
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587) # This is the host for outlook you may have to change it.
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    email = MIMEMultipart()  # Create an email.

    # Create the message.
    message = hostname + " has connected with the network at " + datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") \
              + ", " + hostname + " was " + str(offline_time) + " offline."

    # Parameters of the email.
    email['From'] = MY_ADDRESS
    email['To'] = MY_ADDRESS # Change this to send to somebody else.
    email['Subject'] = "Netwerk alert"

    # Add in the message body.
    email.attach(MIMEText(message, 'plain'))

    # Send the message via the server.
    s.send_message(email)
    del email

    # Terminate the SMTP session and close the connection.
    s.quit()
