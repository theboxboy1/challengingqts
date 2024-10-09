
str = input("Enter string: ")
new_str = ""

for letter in str:
    if letter.lower() not in "aeiou":
        new_str += letter
        

print(f"New string: {new_str}")
