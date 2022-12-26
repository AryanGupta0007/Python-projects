
import pandas as pd
from email.message import EmailMessage
import ssl
import smtplib
content = pd.read_excel("")
# print(content)
names = content['name'].values.tolist()
emails = content["email"].values.tolist()
password = "" #   please enter the generated password here
subject = "Testing software" #  Please enter the subject here
username = " " #  please leave this string empty 
em = EmailMessage()
email_Sender = "" #  please enter your email here
context = ssl.create_default_context()    
len_names = len(names)

em['From'] = email_Sender

for no in range(0,len_names):
    username = str(names[no])
    user_email = str(emails[no])
    body = f"""Hi {username} this is a test maiaiail""" # please enter the body of e mail here

    em['To'] = user_email
    em['Subject'] = subject
    em.set_content(body) 
    with smtplib.SMTP_SSL(host = 'smtp.gmail.com',port = 465,context = context) as smtp:
        smtp.login(email_Sender,password)
        smtp.sendmail(email_Sender,user_email,em.as_string()) 
    del em['To']
    del em['Subject']    
