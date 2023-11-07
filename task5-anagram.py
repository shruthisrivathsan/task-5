#takes input of two strings

str1 = input()
str2 = input()

# every character in str 1 is checked 
for char in str1:
    if char in str2: #if character is in str2
        print(char, end ="") #prints characters
        