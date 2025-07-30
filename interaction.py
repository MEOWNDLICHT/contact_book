from contact_book import ContactBook



def greet():
    print('\nWelcome to the Contact Book Program!')
    print('This program simulates a real contact book wherein you can add, delete, search for contact info, and get the contact of all the people in your contact book.\n')
    print('To start, here are the list of things you can do in this program:')
    commands = ['stop', 'add_user', 'delete_user', 'update_contact_info', 'get_contact_info', 'get_contact_list']
    commands = [' '.join(command.split('_')) for command in commands]

    for number, command in enumerate(commands, start=0):
        print(number, command.capitalize())
    print()


def prompts():
    contact_book = ContactBook()

    while True:
        print('--------------------------------------------------------------------------------------')
        action = input('\nWhat do you want to do? (pick a number) -> ')
        
        match action:
            case '0':
                print('\nThis program will now stop its functions.')
                print('Thank you for using this contact book!\n')
                break

            case '1':
                print('Please enter the name, phone number, and email of your contact.')
                print('\nADDING CONTACT')
                contact_book.add_contact(str(input('Name: ')), str(input('Phone number: ')), str(input('Email: ')))
                print('\nSUCCESSFULY ADDED!')
                print('--------------------------------------------------------------------------------------')

            case '2':
                print('Please enter the name.')
                print('\nDELETING CONTACT')
                contact_book.delete_contact(str(input('Name: ')))
                print('\nSUCCESSFULY DELETED!')
                print('--------------------------------------------------------------------------------------')

            case '3':
                print('Please enter the name, field, and new_value you want to assign to the field.')
                print('\nUPDATING CONTACT')
                contact_book.update_contact(str(input('Name: ')), str(input('Field: ')), str(input('New value: ')))
                print('\nSUCCESSFUL UPDATED!')
                print('--------------------------------------------------------------------------------------')

            case '4':
                print('Please enter the name of the contact you want to know more about.')
                print('\nGETTING CONTACT INFO')
                contact_book.get_contact_info(str(input('Name: ')))
                print('--------------------------------------------------------------------------------------')

            case '5':
                print('\nGETTING LIST OF CONTACTS')
                contact_book.get_contact_list()
                print('--------------------------------------------------------------------------------------')
            case _:
                print('\nInvalid command')
        
        