import email.utils
from email.mime.text import MIMEText
import smtplib

sadd = "your_email_address@gmail.com"
pw = "your_application_passworld"

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
    smtpobj.login(sadd, pw)
    body = "Hello World!"
    subject = "Hello"
    fromAddress = sadd
    toAddress = "your_target_address@gmail.com"
    msg = create_message(body, subject, fromAddress, toAddress)
    smtpobj.send_message(msg)
    smtpobj.close()

if __name__ == "__main__":
    main()

