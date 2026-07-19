


age = input("What is your age? ")

# Try to convert the input to a number and check voting eligibility;
# if the input isn't a valid number, int() raises ValueError and we handle it below
try:
    age = int(age)

    if age >= 18:
        print("You are eligible to vote.")
    else:
        print(" you CANT VOTE, you are not old enough")

except ValueError: 
    print("that is not a number")