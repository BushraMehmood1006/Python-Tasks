# Write a nested for loop that prints a multiplication table for numbers from 1 to 5.

for i in range(1,6):
    print("Table of ", i)
    for j in range (1,11):
        print ( i , "*", j, "=", i*j )