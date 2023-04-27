from email.message import EmailMessage
from app2 import password
import ssl
import smtp 

email_sender = 'spiritedndiligent@gmail.com'
email_password = password

email_receiver = ''

subject = 'Please remember to subscribe'
body = ''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
