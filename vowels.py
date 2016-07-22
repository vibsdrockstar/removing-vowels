vowels=("a","e","i","o","u")
message=input("Enter your message:")
new_message=""
for letter in message:
     if letter not in vowels:
       new_message+=letter
     if letter in vowels:
         print(letter,"is a vowel.")
    
