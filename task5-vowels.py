strname = "Guvi Geeks Network Private Limited" #intialise variable strname of string data type
count = 0   #initialising variable 'count'

for char in strname:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u": #check if the vowels are in the strname
        count +=1
print(count)

