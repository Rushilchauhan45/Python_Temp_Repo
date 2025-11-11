#Write a Python program to create a tuple, access elements, slice, and try modifying one element.[7]

#Create tuple
tuple1 = (10, 20, 30, 40, 50)
print("Created Tuple:", tuple1)

#Access Elements
print("3rd index of Tuple:" , tuple1[3])

#Slice Tuple
print("Tuple Slicing From 2 to 4:", tuple1[2:5])

'''
#Try Modifying one element
=>Tuples in Python are immutable, meaning once created, their elements cannot be changed, added, or deleted.
=>When we try to modify an element using indexing (e.g., my_tuple[2] = 100), Python raises a TypeError.
=>This immutability makes tuples memory-efficient and secure for fixed data that should not be altered.
'''