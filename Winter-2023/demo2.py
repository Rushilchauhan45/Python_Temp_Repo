#Write Python program to find sum of first N numbers using while loop (user input).[4]

num = int(input("Enter a positive integer N: "))

sum = 0 
i = 1

while i<=num:
    sum = sum + i 
    i = i + 1 

print("Sum of first", num, "numbers is:", sum)