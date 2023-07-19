import smtplib as S
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Connect to the SMTP server
emaill = S.SMTP("smtp.gmail.com", 587)
emaill.ehlo()
emaill.starttls()

your_email = input("Enter your email address to login: ")
pass_key = input("Enter your password to login successfully: ")

try:
    emaill.login(your_email, pass_key)
except S.SMTPAuthenticationError as error:
    print("Login Failed. Make sure you have entered the correct credentials.\nError:", error)
    exit(1)

recipent_email = "reciever@gmail.com"

#msg container for animation
msg = MIMEMultipart('alternative')
msg['subject'] = "Special Offer - 15% Discount"
msg['From'] = your_email
msg['To'] = recipent_email

html = """
your html code
"""

part2 = MIMEText(html,'html')
msg.attach(part2)
try:
    emaill.sendmail(your_email, recipent_email, msg.as_string())
    print(f"Email is sent to {recipent_email}")
except Exception as error:
    print(f"Not Executed, error:\n {error}")
emaill.quit()