# Develop Python program to create CSV file that contain five entries along with header (serial number, name, birth_date and city).
# [7 marks]
import csv

header = ['serial_number ' , 'name' , 'birth_date' , 'city']

data = [
[1 , 'ram' , '01-01-2000' , 'india'],
[2 , 'jenice' , '02-02-2001' , 'usa'],
[3 , 'sara' , '03-03-2002' , 'uk'],
[4 , 'mike' , '04-04-2003' , 'canada'],
[5 , 'linga' , '05-05-2004' , 'china']
]

with open('student_data.csv' , 'w' , newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print("CSV file created successfully.")    

