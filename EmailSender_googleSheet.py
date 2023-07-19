#First of all, sign up at Google spreadsheet API. Upload your file there as you want.
#Then take that docs link and use it with request library's -> requests.get('docs_link')

import smtplib as S
import requests

#Setting up the email sending environment
emaill = S.SMTP("smtp.gmail.com",587)
emaill.ehlo()
emaill.starttls()

#credentials for login
your_email_address = str(input("-----TO LOGIN, Enter your credentials-----\n\nEnter your email address:"))
your_pass = str(input("Enter your password:"))

#Exceptional handling for errors
try:
    emaill.login(your_email_address,your_pass)
except S.SMTPAuthenticationError as error:
    print(f"login failed there is a problem with your credentials\nerror is : {error}")

#setting up API call to get data from website and send it in an email
r = requests.get("API link") #replace this URL with your publically available api

#Check if it gets or not
if r.status_code==200:
    data = r.json()["data"]
    print(r.status_code,"-> Success")
else:
    data = None
    print(r.status_code,'-> Failed')

#--------We can't use data directly to take Column names, we are using requests lib, we have to rely on index-------

for i in range(len(data)):
    names = data[i]["Name"].strip()
    email_address = data[i]["Email"].strip()
    #now 
    subject = f"hi {names}, this is Sheikh's Program, using a google sheet file!"
    body = "Welcome to our server! We are very pleased to have you here. Make sure to reply on this email with your positive feedback\nBest Regards,\nTeam Dream Servers"

    msg = f"To:{names}\nSubject:{subject}\n\n{body}"
    #this will use only Name of each person instead of full name, it will PERSONALIZED the email
    try:
        emaill.sendmail(your_email_address,[email_address], msg)
        print(f"Email is sent to {names}")
    except Exception as error:
        print(f"Not Executed, error:\n {error}")


emaill.quit()