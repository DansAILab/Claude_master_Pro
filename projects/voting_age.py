


age = input("What is your age? ")

try: 
    age = int(age)

    if age >= 18:
        print("You are eligible to vote.")
    else:
        print(" you CANT VOTE, you are not old enough")

except ValueError: 
    print("that is not a number")