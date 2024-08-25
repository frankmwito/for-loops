# iterate over a dictionary and print each key-value pair

my_dict = {
    "name" : "Frank",
    "age" : 22,
    "city" : "Nairobi",
    "occupation": "Test Automation Engineer"
}

for key, value in my_dict.items():
    print(f" key: {key}, Value: {value}")