## imports
import smtplib, ssl
from email.message import EmailMessage
from datetime import datetime

## establish variables
sender = "mylesphung03@gmail.com"
password = input("Email password: ")
recipient = input("Recipient Email Address: ")
date = datetime.now() ## needed for the date header when sending emails
college = input("College: ")

## message
msg = f"""\
From: {sender}
To: {recipient}
Date: {date}
Subject: Connect with professor/undergrad research opportunities

Good morning {college} Admissions,

I hope this email finds you well. My name is Myles Phung, and I'm a rising senior at Milton High School in Massachusetts. I'm interested in applying to {college} for computer science. I was wondering if you could connect me with a CS professor, who would be willing to chat about the program? I'm also very interested in doing an undergrad research project, so if they could speak on that, it would be great. If not, no worries. By the way, my main email is myles@5050creative.com, but the email wasn't sending for some reason.

Much appreciated,
Myles"""

## SSL variables and establish SSL context (not using default because my 5050creative doesn't have a certificate)
port = 465
context = ssl.create_default_context()

## send email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recipient, msg)
        print("Email sent successfully.")

except:
    print("An error occurred.")
    quit()
