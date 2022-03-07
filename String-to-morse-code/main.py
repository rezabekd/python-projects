import json

with open("morse_code.json") as data:
    morse_dictionary = json.load(data)

encrypt_morse = input("Enter text to encrypt: ").lower()
input_morse = []

try:
    for letter in encrypt_morse:
        input_morse.append(morse_dictionary[letter])
except KeyError:
    print("You can't encrypt space between words or symbols.")
else:
    print(f"Your encrypted word is: {input_morse}")
