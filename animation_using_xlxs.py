import pandas as pd
import smtplib as S
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Connect to the SMTP server
email = S.SMTP("smtp.gmail.com", 587)
email.ehlo()
email.starttls()

your_email = input("Enter your email address to login :")
pass_key = input("Enter your password to login successfully :")

try:
    email.login(your_email, pass_key)
except S.SMTPAuthenticationError as error:
    print("Login Failed. Make you have entered the correct credentials\n\nerror:",error,"\n")
    exit(1)

#!IF you would change the format of a file, it may cause error due to being unstable!
Reciever_Sheet = pd.read_excel('link')

names = Reciever_Sheet['Name']
email_addresses = Reciever_Sheet['Email']
#----------For template
html = """
      your html code
       """
#----------

for i in range(len(email_addresses)):
    recipient_name = names[i]
    subject = "Hi {}, Special Offer for you".format(recipient_name)

    # Create a new MIMEMultipart object for each email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = your_email
    msg['To'] = email_addresses[i]
    # Attach the HTML content to the email message using as_string()
    part_attach = MIMEText(html, 'html')
    msg.attach(part_attach)

    try:
        email.sendmail(your_email, [email_addresses[i]], msg.as_string())
        print(f"Email sent to {recipient_name}.")
    except Exception as err:
        print(f"Failed to send email to {recipient_name}.\nError: {err}")    

email.quit()