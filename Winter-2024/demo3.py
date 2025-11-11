# Write a Python program to check if a string is palindrome or not.[4]


string = input("Enter a string: ")

lower_string = string.lower()
reversed_string = lower_string[::-1]#slicing to reverse the string

#check the lower string and reversed string is same or not 
if lower_string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



