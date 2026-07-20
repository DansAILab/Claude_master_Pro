contacts = {}

while True : 
    user_input = input("add, view, delete or quit? ")

    if user_input == "add": 
        name = input ("what is the name of the contact?")
        number = input ("what is the phone number of the contact?")
        contacts[name] = number

    elif user_input == "view": 
        name = input ("what is the name of the contact you are looking for?")
        if name in contacts :
            print (f"{name}'s phone number is {contacts[name]}") 
        else: print (f"{name} is not in your contacts.")

    elif user_input == "delete": 
        name = input ("what is the name of the contact you want to delete?")
        if name in contacts :
            del contacts[name]
        else: print (f"{name} is not in your contacts.")

    elif user_input == "quit":
        break
    else:
        print("Invalid input. Please enter 'add', 'view', 'delete', or 'quit'.")