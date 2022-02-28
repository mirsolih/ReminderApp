import json
from datetime import datetime, date 

class MyObject:
    def __init__(self, people, licenses):
        self.people = people
        self.licenses = licenses

    def load_people(self, filename):
        with open('data.json', 'r') as file:
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


people = MyObject 
people.load_people(people,'test.json')

print(people.admins)

    

print("-------------------------------")

licenses = MyObject
licenses.load_licenses(licenses, 'test.json')

to =[]

for i in licenses.licenses:
    for j in people.people:
        if (i["exp_date"] == today):
            print("Found")
            if (i["group"] == j["group"]):
                to.append(j)

#licenses.print_info_licenses(licenses)

