import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

# Email parameters
MY_ADDRESS = "xxxxxxxxxxxx@gmail.com"         # Replace with yours
MY_PASSWORD = "xxxxxxx"      # Replace with yours
RECIPIENT_ADDRESS = "xxx@gmail.com"  # Replace with yours

HOST_ADDRESS = 'smtp.gmail.com'   # Replace with yours
HOST_PORT = 587                          # Replace with yours


# Connection with the server
server = smtplib.SMTP(host=HOST_ADDRESS, port=HOST_PORT)
server.starttls()
server.login(MY_ADDRESS, MY_PASSWORD)

# Creation of the MIMEMultipart Object
message = MIMEMultipart()

# Setup of MIMEMultipart Object Header
message['From'] = MY_ADDRESS
message['To'] = RECIPIENT_ADDRESS
message['Subject'] = "Automated Email with Attachment"

# Creation of a MIMEText Part
textPart = MIMEText("This is my first plain text automated Email with an Attachment.\n\nAlessio", 'plain')

# Creation of a MIMEApplication Part
filename = "document.txt"
filePart = MIMEApplication(open(filename,"rb").read(),Name=filename)
filePart["Content-Disposition"] = 'attachment; filename="%s' % filename

# Parts attachment
message.attach(textPart)
message.attach(filePart)

# Send Email and close connection
server.send_message(message)
server.quit()
