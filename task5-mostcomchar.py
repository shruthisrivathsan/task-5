str = input()
comm_char = "" #create new empty string
for char in str:
    if char not in comm_char: #check if character of str is in the new string
        comm_char += char #add to new string
        print(char, end = "")