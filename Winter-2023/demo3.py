'''
Write Python code to print pattern using nested loop (user input rows).[7]
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1

'''
rows = int(input("Enter number of rows: "))

for i in range(1 , rows + 1):
    for j in range(1 , i +1):
        if (i+j)%2 == 0:
            print("1" , end=" ")
        else:
            print("0" , end=" ")
    print()             
