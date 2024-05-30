contacts = {}
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")
    email = input("Enter the Email: ")
    if name in contacts:
        print("This contact already exists.")
    else:
        contacts[name] = {"phone": phone, "address": address, "Email": email}
        print("Contact added successfully.")

def delete_contact():
    name = input("Enter name: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("This contact does not exist.")

def update_contact():
    name = input("Enter name: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        address = input("Enter the new address: ")
        contacts[name]["phone"] = phone
        contacts[name]["address"] = address
        email = input("Enter the Email: ")
        print("Contact updated successfully.")
    else:
        print("This contact does not exist.")

def search_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact Found:")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Address: {contacts[name]['address']}")
        print(f"Email: {contacts[name]['Email']}")
    else:
        print("Contact not found.")

def display_contacts(contacts):
    print("\nContacts:")
    for name, contact_info in contacts.items():
        print(f"{name}: Phone: {contact_info['phone']}, Address: {contact_info['address']}, Email: {contact_info['Email']}")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Display Contacts")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        delete_contact()
    elif choice == 3:
        update_contact()
    elif choice == 4:
        search_contact()
    elif choice == 5:
        display_contacts(contacts)
    elif choice == 6:
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number (1-6)")
