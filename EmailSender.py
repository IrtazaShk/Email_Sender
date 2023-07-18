#If we want to send bulk mails, we must use any *PAID DOMAIN'S EMAIL ADDRESS*
import smtplib as S

emaill = S.SMTP("smtp.gmail.com",587)
emaill.ehlo()
emaill.starttls()

email_address = str(input("Enter your vaild email address :"))
APP_passkey = str(input("Enter your password to login :"))

#App pass key is needed, not your original password, Make sure 2FA is on then create an app pass key
#Use that pass key in the required password, email will be send successfully.
#You can delete the key after your work to make sure your account has no other access

emaill.login(email_address, APP_passkey)

#It will login into your account

subject = "Testing Email Py sender"
body = "It is Working"

#Combines these into one variable -> msg

msg = "subject:{}\n\n{}".format(subject, body)

Reciever_list = ["reciever1@gmail.com", "reciever2@gmail.com","reciever3@gmail.com"]

emaill.sendmail('sender@gmail.com',Reciever_list,msg)

#this is a built-in function and it would take 3 params(sender, recievers, message)

print("-----send main-----")
emaill.quit()

