# CONTACT BOOK PROGRAM
"""A contact book program that can store and pull data from a json file."""


import json


class ContactBook:

    def __init__(self):
        try:
            with open("contacts.json", "r") as contact_book:
                self.contacts = json.load(contact_book)
        except json.JSONDecodeError:
            print("\nThe file contains nothing yet... Please add a person in the contact list.")
            print("Use the add_contact method, and input the ff values in the parameters: name, phone number, email.\n")
            self.contacts = {}


    def get_contact_list(self):
        print("\nThe full list of contacts: ")
        n = 0
        for name, info in self.contacts.items():
            n += 1
            print(f"{n}. Name: {name}, Phone number: {info['Phone number']}, Email: {info['Email']}")
        print(f"\nThe total number of people in the Contact Book is: {n}\n")


    def search_info(self, name_to_search):
        print(f"\nYou searched for '{name_to_search}':\n")
        n = 0
        
        for name, info in self.contacts.items():
            if name.lower() == name_to_search.lower():
                n += 1
                print(f"{n}. Phone number: {info['Phone number']}, Email: {info['Email']}")
        print(f"\nThe total number of people that matched your search: {n}\n")


    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {
            "Phone number": phone_number,
            "Email" : email
        }

        with open("contacts.json", "w") as save_data:
            json.dump(self.contacts, save_data)
        
        print(f"\nThe contact information of '{name}' has been successfuly added to the Contact Book!\n")


    def delete_contact(self, name):
        if name in self.contacts:
            self.contacts.pop(name)

        with open("contacts.json", "w") as delete_data:
            json.dump(self.contacts, delete_data)

        print(f"\nThe contact information of '{name}' has been deleted from the Contact Book.\n")