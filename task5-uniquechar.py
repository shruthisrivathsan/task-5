str = input()
unique_str = "" #create new empty string

for char in str:
    if char not in unique_str: #check if each character of old string is in new string
        unique_str += char
print(unique_str)