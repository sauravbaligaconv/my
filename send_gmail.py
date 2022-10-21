# Import modules
import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
## The pandas library is only for generating the current date, which is not necessary for sending emails
import pandas as pd

# Define the HTML document
html = '''
    <html>
        <body>
            <h1>Thank you For Being our Client</h1>
            <img src="https://mailsender10.herokuapp.com/static/images/saurav1234567" alt="SMILE" style="width:42px;height:42px;">
        </body>
    </html>
    '''

# Set up the email addresses and password. Please replace below with your email address and password
email_from = 'raysauravballo@gmail.com'
password = 'agcfmpnlfmzpdfhe'
email_to = ['sauravbaliga17@gmail.com','sauravbaliga1718@gmail.com']

# Generate today's date to be included in the email Subject

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['BCC']=", ".join(email_to)
email_message['Subject'] = 'Discount'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))
# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(email_from, password)
    server.sendmail(email_from, email_message['BCC'], email_string)