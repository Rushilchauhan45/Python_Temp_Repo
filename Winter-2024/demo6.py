#Develop Python program to find maximum, minimum and average of given numbers using user-defined function.[7]


def min_max_avg(numbers):
    if not numbers:
        return None,None,None

    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average


num_list = [10, 20, 30, 40, 50]
minimum, maximum, average = min_max_avg(num_list)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
