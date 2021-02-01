def Fibonacci(number):
    cache={}
    if number in cache:
        return cache[number]
    elif number<2:
        cache[number] = number
        return cache[number]
    else:
        cache[number] = Fibonacci(number-1) + Fibonacci(number-2)
        return cache[number]



number = int(input("Enter Number : "))

print("Fibonacci of ", number , " = ",Fibonacci(number))