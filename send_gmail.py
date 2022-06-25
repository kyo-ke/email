import email.utils
from email.mime.text import MIMEText
import smtplib

SENDADDRESS = "your_email_address@gmail.com"
APP_PASSWORD = "your_application_password"
TOADDRESS = "your_target_address@gmail.com"

def create_message(body, subject, fromAddress, toAddress):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = email.utils.formatdate()
    return msg

def main():
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(SENDADDRESS, APP_PASSWORD)
    body = "Hello World!"
    subject = "Hello"
    msg = create_message(body, subject, SENDADDRESS, TOADDRESS)
    smtpobj.send_message(msg)
    smtpobj.close()

if __name__ == "__main__":
    main()

