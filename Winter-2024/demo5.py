#Write a Python function to sum all the numbers in a list.[3]


def sum_of_list(numbers):
    total = 0
    for i in numbers:
        total = total + i 
    return total

num_list = [1,3,5,87,9,54]
print("Sum of the List:",sum_of_list(num_list)) 
