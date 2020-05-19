# Sends an E-Mail

import smtplib
from email.message import EmailMessage


def send_mail():

    msg = EmailMessage()
    msg.set_content("The article is available again.")

    msg['Subject'] = "Subject"
    msg['From'] = "from@gmail.com"
    msg['To'] = "to@gmail.com"

    # Send the message via our own SMTP server.
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("user@gmail.com", "password")
    server.send_message(msg)
    server.quit()


