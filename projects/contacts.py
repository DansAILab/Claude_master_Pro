import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CONTACTS_FILE = os.path.join(SCRIPT_DIR, "contacts.json")


def count_contacts(contacts):
    return len(contacts)


def load_contacts(file_path=CONTACTS_FILE):
    """Return the saved contacts as a dict, or an empty dict if none/invalid."""
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, "r") as contacts_file:
            data = json.load(contacts_file)
    except (json.JSONDecodeError, OSError):
        # File is corrupt or unreadable — start with an empty contact list
        # rather than crashing.
        print(f"Warning: could not read {file_path}. Starting with no contacts.")
        return {}
    if not isinstance(data, dict):
        print(f"Warning: {file_path} did not contain valid contacts. Starting empty.")
        return {}
    return data


def save_contacts(contacts, file_path=CONTACTS_FILE):
    """Write the contacts dict to disk as JSON."""
    with open(file_path, "w") as contacts_file:
        json.dump(contacts, contacts_file, indent=2)


if __name__ == "__main__":
    contacts = load_contacts()
    print(f"You currently have {count_contacts(contacts)} contact(s) saved.")

    while True :
        user_input = input("add, view, delete or quit? ")

        if user_input == "add":
            name = input ("what is the name of the contact?")
            number = input ("what is the phone number of the contact?")
            contacts[name] = number
            save_contacts(contacts)

        elif user_input == "view":
            name = input ("what is the name of the contact you are looking for?")
            if name in contacts :
                print (f"{name}'s phone number is {contacts[name]}")
            else: print (f"{name} is not in your contacts.")

        elif user_input == "delete":
            name = input ("what is the name of the contact you want to delete?")
            if name in contacts :
                del contacts[name]
                save_contacts(contacts)
            else: print (f"{name} is not in your contacts.")

        elif user_input == "quit":
            break
        else:
            print("Invalid input. Please enter 'add', 'view', 'delete', or 'quit'.")
