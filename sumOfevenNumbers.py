# calculate the sum of all even numbers in the list

num = int(input("Enter the size of your list:"))
numbers = list()

try:
 for i in range(num):
    numbers.append(int(input(f"Enter any number {i+1}:")))

except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit() 

print("your new list is:", numbers)
even_numbers = list()

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        
        
if even_numbers:
    print("List of even numbers is:", even_numbers)
else:
    print("There are no even numbers in the list.")