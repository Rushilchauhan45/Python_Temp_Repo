#Write a Python function to calculate factorial of a number (use function + loop).[7]


#user-defined function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact    



num = int(input("Enter a number to calculate its factorial: "))
fact_num = factorial(num)

print(f"The factorial of {num} is {fact_num}")