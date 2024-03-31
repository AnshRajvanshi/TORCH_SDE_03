import json

# Function to load contacts from file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to save contacts to file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts[name] = (phone, email)
    print("Contact added successfully!")

# Function to view the contact list
def view_contacts(contacts):
    if contacts:
        print("Contact List:")
        for name, (phone, email) in contacts.items():
            print(f"Name: {name}, Phone: {phone}, Email: {email}")
    else:
        print("Contact list is empty.")

# Function to edit a contact
def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        print(f"Editing contact: {name}")
        phone = input("Enter the new phone number (press Enter to keep existing): ")
        email = input("Enter the new email address (press Enter to keep existing): ")
        if phone:
            contacts[name] = (phone, contacts[name][1])
        if email:
            contacts[name] = (contacts[name][0], email)
        print("Contact edited successfully!")
    else:
        print("Contact not found.")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main function
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. Add new contact")
        print("2. View contacts")
        print("3. Edit contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
