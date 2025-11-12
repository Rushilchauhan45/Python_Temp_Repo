#Write a program to print 100 Fibonacci numbers in file “Myfibonacci.csv”.
#[7 Marks]

import csv

def fibonacci(num):
    fibonacci_series = [0,1 ]
    for i in range (2 , num):
        fibonacci_series.append(fibonacci_series[i-1] + fibonacci_series[i-2])
    return fibonacci_series 


fib_Series = fibonacci(100)

with open("Myfibonacci.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Index" , "Fibonacci Number"])

    for i , num in enumerate(fib_Series):
        writer.writerow([i , num])