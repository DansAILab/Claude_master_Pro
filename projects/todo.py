
chores = [] 
while True:
    user_input = input("Would you like to add, view or quit the list? ").lower()

    if user_input == "add": 
        item = input("What would you like to add? ")
        chores.append(item)
    
    elif user_input == "view":
        print(chores)
    
    elif user_input == "quit":
        break

    else:
        print("Invalid input. Please enter 'add', 'view', or 'quit'.") 


