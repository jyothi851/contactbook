# Contact Book (CLI)

contacts = []

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add Contact
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("✅ Contact added successfully!")

    # View Contacts
    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\n----- Contact List -----")
            for contact in contacts:
                print(f"Name : {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print("-" * 25)

    # Search Contact
    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\n✅ Contact Found")
                print(f"Name : {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                found = True
                break

        if not found:
            print("❌ Contact not found.")

    # Delete Contact
    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == delete_name.lower():
                contacts.remove(contact)
                print("✅ Contact deleted successfully!")
                found = True
                break

        if not found:
            print("❌ Contact not found.")

    # Exit
    elif choice == "5":
        print("Thank you for using the Contact Book!")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 5.")