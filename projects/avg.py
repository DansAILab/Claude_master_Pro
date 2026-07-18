# creatng code to output the numbers greater then the lists average

def above_average(numbers):
    average = sum(numbers) / len(numbers)
    result =[] 

    for number in numbers : 
     if number > average:
        result.append(number)

    return result 

numbers = list(range(1,21))

print("Here is the list of numbers:", numbers ) 
print ("numbers above the average are:", above_average(numbers))