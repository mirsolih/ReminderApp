from datetime import datetime,date
from distutils.util import execute
import json
from unicodedata import name
import functions
from classfile import MyObject
import operator



#-------LOADING PEOPLE OBJECT-------


to = []
body = []
subject = []
MyObject.load_people(MyObject, 'data.json')

#----LOADING LICENSE OBJECT------

MyObject.load_licenses(MyObject, 'data.json')

#-----CONVERT DATE FORMAT TO STRING--------

today = date.today()
today = datetime.strftime(today, "%d.%m.%Y")

#------CHEKING THE DATA AND SENDING THE EMAIL----

for i in MyObject.licenses:
    for j in MyObject.people:
        if(i["exp_date"] == today):
            print("found")

            if operator.contains(j["group"],i["group"]):
                body="Hey please update the license " + i["name"] + " it will be expired on "+ i["exp_date"]
                subject="Update " + i["name"] + " license"
                to = j["email"]
                #print(subject, body, to)
                #exec(open( i["script"]).read())
                print(subject, body, to) 
              
                if __name__ == '__main__':                    
                    functions.email_alert(subject, body, to)
        



