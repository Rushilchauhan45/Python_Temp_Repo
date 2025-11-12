#Explain the conversion of list to dictionary in Python.
# [7 marks]

# Dictonary --> Key And Value Pair

#method 1: Using dict() function
list1 = [(1,'a'),('b', 2),('c', 3), (4,'d')]
dict1 = dict(list1)
print("List:", list1)

#method 2 : two seprate list 

key = ["name" , "age" , "city"]
value = ["Alice" , 25 , "New York"]

dict2 = dict(zip(key , value))
print("Dictionary:", dict2)