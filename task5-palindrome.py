str = input()
new_str = ""

for char in str:
    new_str = char + new_str
print(new_str)

if str == new_str:
    print("Is a palindrome")
else:
    print("Not a palindrome")