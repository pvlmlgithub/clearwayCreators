import smtplib,ssl


def send_mail(message,receiver) :
    host = "smtp.gmail.com"
    port = 465

    username = "pradeepacharya626@gmail.com"
    password = "zqip jczd pzew culp"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server :
        server.login(username,password)
        server.sendmail(username,receiver,message)

