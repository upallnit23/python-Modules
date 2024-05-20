contacts = []

def add_contact(contacts, name, pnum, email):
    contacts.append({"name": name, "phone": pnum, "email": email})
    
def remove_contact(contacts, name):
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            return contacts.pop(i)
    return None

def display_contact(contacts):
    for contact in contacts:
        print(f"Name:{contact["name"]}, Phone: {contact["phone"]}, Email: {contact["email"]}")


