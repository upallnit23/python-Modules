import cmanager

#Task 1: Contact List Manager

contacts = []
while True:
    print("Contacts List")
    print("Choose a - add, b - remove, c - display contacts, d - exit")
    choice = input("Enter a, b, c  or d ")
    if choice == "a":
        name = input("Enter name: ")
        pnum = input("Enter phone number: ")
        email = input("Enter email address: ")
        cmanager.add_contact(contacts, name, pnum, email)
    elif choice == "b":
        cmanager.display_contact(contacts)
    elif choice == "c":
        name = input("Enter search name:")
        if name is not None:
            cmanager.remove_contact(contacts, name)
            print("f{name} was deleted. ")
        else:
            print("f{name} was not found in contacts. ")
    if choice == "d":
            exit()
    
