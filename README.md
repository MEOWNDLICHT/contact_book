# Contact Book Simulation

This program aims to simulate a contact book via basic CRUD operations like adding, deleting, updating, and searching contacts. Everything is entirely CLI-based but there are instructions and basic how-to that users can use upon running the main.py. 

---

## Program Structure & Flow  
main.py -> interactions.py -> contact_book.py  

main.py - This layer is responsible for running the prompt and interactions layer, both of which are responsible for displaying data, to ease the overall experience of users. In general, this is the file users have to run in order to make the code work.  

interactions.py - This layer is responsible for the various displays and actions that users can see and take part in. It heavily relies on contact_book.py since that part is responsible for the logic of the program.  

contact_book.py - This layer is responsible for the proper handling of the CRUD of the program. Its purpose is to ensure that the basic operations that users can do are running properly and handled securely.  