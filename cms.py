import json

# File to store contact information
CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")

def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(name, phone, email):
    contacts = load_contacts()
    if name in contacts:
        contacts[name] = {'phone': phone, 'email': email}
        save_contacts(contacts)
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    print("Welcome to the Contact Management System!")

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            update_contact(name, phone, email)
        elif choice == '4':
            print("Thank you for using the Contact Management System!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
