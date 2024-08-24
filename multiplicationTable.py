# print multiplication table of a given number

try:
    num = int(input("Enter any number from 1 to 12:"))
    
    if num > 12 or num < 1:
     print("Enter the number again")
    else:
        for i in range(1,13):
             print(f"{i} * {num} = {num*i}")
             
except ValueError:
    print("Invalid input! Please enter a numeric value between 1 and 12.")

