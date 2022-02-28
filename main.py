from datetime import datetime,date
import json
from unicodedata import name
import functions
from classfile import MyObject



#-------LOADING PEOPLE OBJECT-------

people = MyObject
to = []
people.load_people(people, 'data.json')
for j in people.people:
    to.append(j["email"])

#----LOADING LICENSE OBJECT------

licenses = MyObject
exp_date = []
licenses.load_licenses(licenses, 'data.json')

#-----CONVERT DATE FORMAT TO STRING--------

today = date.today()
today = datetime.strftime(today, "%d.%m.%Y")

#------CHEKING THE DATA AND SENDING THE EMAIL----

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

