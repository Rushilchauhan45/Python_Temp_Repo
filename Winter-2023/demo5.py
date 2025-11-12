'''
Write a Python program to read marks of students from 
“student_marks.csv”. Find average, maximum, and minimum marks from data. (File contains 100 records).
'''

import csv

marks = []

with open('student_marks.csv' , 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for i in reader:
        marks.append(int(i[1]))  

avg_marks = sum(marks) / len(marks)
max_marks = max(marks)
min_marks = min(marks)       

print(f"Average Marks: {avg_marks}")
print(f"Maximum Marks: {max_marks}")
print(f"Minimum Marks: {min_marks}")