class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)

    def search(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def delete(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                return True
        return False

    def display_all(self):
        for contact in self.contacts:
            print(f'Name: {contact.name}, Phone: {contact.phone}')

def main():
    contact_book = ContactBook()
    while True:
        print("1: Add Contact")
        print("2: Search Contact")
        print("3: Delete Contact")
        print("4: Display All Contacts")
        print("5: Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            contact_book.add(name, phone)
        elif choice == "2":
            name = input("Enter name: ")
            contact = contact_book.search(name)
            if contact:
                print(f'Name: {contact.name}, Phone: {contact.phone}')
            else:
                print("Contact not found.")
        elif choice == "3":
            name = input("Enter name: ")
            if contact_book.delete(name):
                print("Contact deleted.")
            else:
                print("Contact not found.")
        elif choice == "4":
            contact_book.display_all()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
