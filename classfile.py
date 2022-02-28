import json

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