import smtplib,ssl

host = "smtp.gmail.com"
port = 465

username = "pradeepacharya626@gmail.com"
password = "zqip jczd pzew culp"

context = ssl.create_default_context()

receiver = "pradeepacharya626@gmail.com"            # you can use another email

# use \ to create subject
msg = """ \
Subject : hii
how are you"""

with smtplib.SMTP_SSL(host,port,context=context) as server :
    server.login(username,password)
    server.sendmail(username,receiver,msg)