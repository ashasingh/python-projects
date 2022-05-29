import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email parameters
MY_ADDRESS = "xxxx@gmail.com"         # Replace with yours
MY_PASSWORD = "xxxxxxxxxxx"      # Replace with yours
RECIPIENT_ADDRESS = "xxx@gmail.com"  # Replace with yours

HOST_ADDRESS = 'smtp.gmail.com'   # Replace with yours
HOST_PORT = 587                          # Replace with yours


# Connection with the server
server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
server.starttls()
server.login(MY_ADDRESS, MY_PASSWORD)

# Creation of the MIMEMultipart Object
message = MIMEMultipart("alternative")

# Setup of MIMEMultipart Object Header
message['From'] = MY_ADDRESS
message['To'] = RECIPIENT_ADDRESS
message['Subject'] = "Automated HTML Email"

# HTML Setup
html = """<html>
    <head></head>
    <body>
        <p style='color:orange;'>This is my first HTML automated email!</p>
        <p>Alessio</p>
    </body>
</html>"""

# Creation of a MIMEText Part
htmlPart = MIMEText(html, 'html')

# Part attachment
message.attach(htmlPart)

# Send Email and close connection
server.send_message(message)
server.quit()
