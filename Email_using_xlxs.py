import pandas as pd
import smtplib as S


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


#           !IF you would change the format of a file, it may cause error due to being unstable!
Reciever_Sheet = pd.read_excel("*path_to_file*")

names = Reciever_Sheet['Name']
email_addresses = Reciever_Sheet['Email']

subject = f"Hi {{}}, Sheikh here!"  
#The name will be inserted using .format() later

body = "This email is sent to a trusted person, via python using pandas and smptplib modules"

for i in range(len(email_addresses)):
    recipient_name = names[i]
    msg = "To: {}\nSubject: {}\n\n{}".format(email_addresses[i], subject.format(recipient_name), body)
    
    try:
        email.sendmail(your_email, [email_addresses[i]], msg)
        print(f"Email sent to {recipient_name}.")
    except Exception as err:
        print(f"Failed to send email to {recipient_name}.\nError: {err}")

email.quit()