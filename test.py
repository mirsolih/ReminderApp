import json
from datetime import datetime, date
from unicodedata import name 
import operator

class MyObject:
    def __init__(self, people, licenses):
        self.people = people
        self.licenses = licenses

    def load_people(self, filename):
        with open(filename, 'r') as file:
            data = json.loads(file.read())
        
        self.people = data['people']

    def print_info_people(self):
        print(self.people)

    def load_licenses(self, filename):
        with open(filename, 'r') as file:
            data = json.loads(file.read())

        self.licenses = data['licenses']
        

    def print_info_licenses(self):
        print(self.licenses)

today = date.today()
today = datetime.strftime(today, "%d.%m.%Y")


MyObject.load_people(MyObject,'test.json')

#person.print_info_people(person)

#print(str(person))

print("-------------------------------")


MyObject.load_licenses(MyObject, 'test.json')

to =[]



#print(person.people[0]["admins"][1]['email'])

k=0
for i in MyObject.licenses:
    for j in MyObject.people:
        if (i["exp_date"] == today):
            print("Found")
            #print(j["name"])
            if operator.contains(j["group"],i["group"]):
                print(i["name"])
                print(j["name"])
                to.append(j["email"]) 
print(to)
#licenses.print_info_licenses(licenses)

