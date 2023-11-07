str = input()
str_vowels="aeiouAEIOU" #initialise variable str_vowels with vowels

#replace the vowels in str
for char in str: 
    if char in str_vowels:
        str=str.replace(char,"")
print(str)