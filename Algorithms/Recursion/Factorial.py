def Factorial(number):

    if number == 0:
        return 0
    elif number ==1:
        return 1
    else:
        return (number*Factorial(number-1))




number = int(input("Enter Number : "))

print("Factorial of ", number , " = ",Factorial(number))
