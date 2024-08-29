def display_menu():
    # creating the menu for the user to input the desired option to manipulate the address book
    print("\n\nHere's the Menu:")
    print("1. Add a new contact(s)")
    print("2. Search for a contact(s)")
    print("3. View all contact(s)")
    print("4. Update a contact(s)")
    print("5. Delete a contact(s)")
    print("6. Exit")

def add_new_contact(address_book):
    # This function is going to allow the user to add a new contact by adding 3 strings: name, number, and email
    name = input("Enter the contact's name: ").strip()
    if name in address_book:
        print("This contact already exists :)")
    else:
        phonenumber = input("Enter the contact's phone number: ").strip()
        email = input("Enter the contact's email address: ").strip()
        address_book[name] = {'phone': phonenumber, 'email': email}
        print(f"Contact '{name}' added successfully!")

def search_for_contact(address_books):
    # Searches the strings to see if the inputted contact exists in the addressbook
    name = input("Enter the name of the contact to search for: ").strip()
    if name in address_books:
        print(f"\nName: {name}")
        print(f"Phone: {address_books[name]['phone']}")
        print(f"Email: {address_books[name]['email']}")
    else:
        print(f"No contact found with the name '{name}'. Please enter desired name")

def view_all_contacts(address_book):
    # Lets the user view all the contacts that were inputted by the user
    if address_book:
        print("\nAll Contacts:")
        for name, details in address_book.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
    else:
        print("No contacts in the address book.")

def updating_contact(address_book):
    # The user can update a current name string in the dictionary
    name = input("Enter the name of the contact to update: ").strip()
    if name in address_book:
        print(f"Current phone: {address_book[name]['phone']}")
        print(f"Current email: {address_book[name]['email']}")
        new_phonenumber = input(
            "Enter the new phone number; If wanting to keep same number please leave blank: ").strip()
        new_emailaddress = input(
            "Enter the new email address; If wanting to keep same email please leave blank: ").strip()

        if new_phonenumber:
            address_book[name]['phone'] = new_phonenumber
        if new_emailaddress:
            address_book[name]['email'] = new_emailaddress

        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"No contact found with the name '{name}'.")


def deleteing_contact(address_book):
    # The user can also delete a string in the dictionary which will also delete number and email
    name = input("Enter the name of the contact you would like to delete: ").strip()
    if name in address_book:
        del address_book[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    address_book = {}
    # Here is where the empty dictionary is being created
    while True:
        display_menu()
        choice = input("Enter your option please: ").strip()

        if choice == '1':
            add_new_contact(address_book)
        elif choice == '2':
            search_for_contact(address_book)
        elif choice == '3':
            view_all_contacts(address_book)
        elif choice == '4':
            updating_contact(address_book)
        elif choice == '5':
            deleteing_contact(address_book)
        elif choice == '6':
            print("Exiting the address book. See you soon :( ")
            break
        else:
            print("Invalid choice. Please try again :(")


if __name__ == "__main__":
    main()
# This code will let you add, search, view, update, and delete items in the dictionary tailored to the needs of the user
