# count vowels in a string

word = input("Enter any string:")
vowels = "aeiouAEIOU"
count = 0

for letter in word:
    if letter in vowels:
        count += 1
        
        
        
print(count, "vowels")