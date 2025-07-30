# CONTACT BOOK PROGRAM

import json


class ContactBook:
    def __init__(self):
        try:
            with open("contacts.json", "r") as contact_book:
                self.contacts = json.load(contact_book)
        except json.JSONDecodeError:
            self.contacts = {}
        except FileNotFoundError:
            with open("contacts.json", "r") as contact_book:
                self.contacts = json.load(contact_book)
        

    def save_changes(self):
        with open("contacts.json", "w") as save_data:
            json.dump(self.contacts, save_data, indent=4)



    def get_contact_list(self):
        print("\nThe full list of contacts: ")
        n = 0
        for name, info in self.contacts.items():
            n += 1
            print(f"{n}. Name: {name}, Phone number: {info['Phone number']}, Email: {info['Email']}")
        print(f"\nThe total number of people in the Contact Book is: {n}\n")

    def get_contact_info(self, name_to_search: str):
        print(f"\nYou searched for '{name_to_search}':\n")
        n = 0
        
        for name, info in self.contacts.items():
            if name.lower() == name_to_search.lower():
                n += 1
                print(f"{n}. Phone number: {info['Phone number']}, Email: {info['Email']}")
        print(f"\nThe total number of people that matched your search: {n}\n")



    def add_contact(self, name: str, phone_number: str, email: str):
        self.contacts[name] = {
            "Phone number": phone_number,
            "Email" : email
        }
        self.save_changes()
        
    def delete_contact(self, name: str):
        if name in self.contacts:
            self.contacts.pop(name)
        self.save_changes()

    def update_contact(self, name: str, data_to_update: str, new_value: str):
        if name not in self.contacts:
            print('Contact not found.')
        else:
            self.contacts[name][data_to_update] = new_value
        self.save_changes()