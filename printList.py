# print list with its index
num = int(input("Enter the size of your list:"))
numbers = list()

try:
 for i in range(num):
    numbers.append(int(input(f"Enter any number {i+1}:")))

except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit() 

print("your new list is:", numbers)

for number in numbers:
    print(f"Number at index {numbers.index(number)} is {number}")