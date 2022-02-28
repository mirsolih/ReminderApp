import smtplib 
from email.message import EmailMessage 

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to


    user = "alertnoreply1999@gmail.com"
    msg['from'] = user
    password = "jyzbeaurtacoeflq"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def checking(licenses, today, to):
    for i in licenses.licenses:
        if(i["exp_date"] == today):
            print("found")
            if __name__ == '__main__':
                body = "Hey please update the license " + i["name"] + " it will be expired on "+ i["exp_date"]
                subject = "Update " + i["name"] + " license"
                print(subject, body, to)
                #functions.email_alert(subject, body, to)
                break
        else:
            print("No license has to be updated")