# Write a for loop that iterates over a list of numbers and prints only 
# those numbers that are divisible by 3. (e.g., [3, 6, 9, 12, 15])

numbers = [3, 5, 6, 9,10,  12, 15, 7, 34, 66]
num = []
for i in numbers:
    if i % 3 == 0:
        num.append(i)
print(num)        