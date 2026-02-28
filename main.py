contacts = {}

print("Contacts Manager Created!")

# Add Contact
def addContact(name, num, email):
    if num in contacts:
        print("Contact already exists with this number!")
        return
    contacts[num] = {
        "name": name,
        "email": email
    }
    print("Added successfully!")


# Delete Contact (by phone or name)
def delContact():
    choice = input("Delete by Phone (p) or Name (n)? ").lower()

    if choice == 'p':
        num = input("Enter Mobile No: ")
        if num in contacts:
            del contacts[num]
            print("Deleted successfully!")
        else:
            print("Not Found")

    elif choice == 'n':
        name = input("Enter Name: ")
        found = False
        for num, info in list(contacts.items()):
            if info["name"].lower() == name.lower():
                del contacts[num]
                print("Deleted successfully!")
                found = True
        if not found:
            print("Not Found")
    else:
        print("Invalid choice")


# Search Contact
def searchContact():
    choice = input("Search by Phone (p) or Name (n)? ").lower()

    if choice == 'p':
        num = input("Enter Mobile No: ")
        if num in contacts:
            info = contacts[num]
            print("\nContact Found:")
            print(f"Name: {info['name']}")
            print(f"Phone: {num}")
            print(f"Email: {info['email']}")
        else:
            print("Not Found")

    elif choice == 'n':
        name = input("Enter Name: ")
        found = False
        for num, info in contacts.items():
            if info["name"].lower() == name.lower():
                print("\nContact Found:")
                print(f"Name: {info['name']}")
                print(f"Phone: {num}")
                print(f"Email: {info['email']}")
                found = True
        if not found:
            print("Not Found")
    else:
        print("Invalid choice")


# Display All Contacts
def displayContacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\nAll Contacts:")
    print("-" * 30)
    for num, info in contacts.items():
        print(f"{info['name']} - {num}")
    print("-" * 30)


# Main Loop
while True:
    cmd = input("\nAdd:add | Delete:del | Search:search | Display:all | Exit:exit\nMode: ").lower()

    match cmd:
        case 'add':
            name = input("Name: ")
            num = input("Mobile No: ")
            email = input("Email: ")
            addContact(name, num, email)

        case 'del':
            delContact()

        case 'search':
            searchContact()

        case 'all':
            displayContacts()

        case 'exit':
            print("Exited!")
            break

        case _:
            print("Invalid command!")