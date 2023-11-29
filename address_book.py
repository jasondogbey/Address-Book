class Contact:
    def __init__(self, name, phone, address):
        self.name = name
        self.phone = phone
        self.address = address
    
class AddressBook():
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, address):
        newcontact = Contact(name, phone, address)
        self.contacts.append(newcontact)
        print('Contact added!')
    
    def find_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    
    def update_contact(self, name, updated_phone, updated_address):
        contact = self.find_contact(name)
        if contact:
            contact.phone = updated_phone
            contact.address = updated_address
            print('Contact updated!')

    def remove_contact(self, name):
        contact = self.find_contact(name)
        if contact:
            self.contacts.remove(contact)
            print('Contact removed.')
        else:
            print('Contact was not found.')
        
    def print_all_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}, Address: {contact.address}")
            
# Example usage:
address_book = AddressBook()

# Adding contacts
address_book.add_contact("John Doe", "123-456-7890", "123 Main St")
address_book.add_contact("Jane Smith", "987-654-3210", "456 Oak Ave")

# Finding and updating a contact
address_book.update_contact("John Doe", "999-999-9999", "789 Elm St")

# Removing a contact
address_book.remove_contact("Jane Smith")

# Getting all contacts
all_contacts = address_book.print_all_contacts()