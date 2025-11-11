#Write a Python function to convert string into upper case and find length of string.[7]

#user-defined function
def convertUPPER_and_Length(String1):
        uppercase = String1.upper()
        length = len(String1)
        return uppercase , length


# step-1: input string from user
String = input("Enter a string: ")#string input from user
uppercase1 , length1 = convertUPPER_and_Length(String) 

#upper() is convert string to upper case from lowercase
print("Upper Case Of String:" ,uppercase1)
print("Length of String :" , length1)


'''
#Builtin Pyuthon Fucntion method
String = input("Enter a string: ")#string input from user

print("Upper Case Of String:" ,String.upper())
print("Length of String :" , len(String))


'''
