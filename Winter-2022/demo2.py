#Write a Python program to print all the prime numbers between 100 to 200.[7]

for i in range(100 , 201):
    if i > 1:
        factor = 0
        for j in range(1 , i+1):
            if i % j == 0:
                factor += 1
        if factor == 2 :
            print(i , end=" ")        