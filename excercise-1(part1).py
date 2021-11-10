dictationary = {"Abnegation": "Renouncing any belief or doctrine", "Aggrandize": "An enhanced wealth, status or power",
                "Alacrity": "Eagerness", "Anachronistic": "Chronologically misplaced","Beguile":"Influencing someone in a deceptive manner"}

print(dictationary)

print("Enter a word:")
word = input()
print("The meaning of ", word, "is", dictationary.get(word))

print("Enter a second word:")
word2 = input()
print("The meaning of", word2, "is", dictationary.get(word2))

print("Enter a third word:")
word3 = input()
print("The meaning of", word3, "is", dictationary.get(word3))

print("Enter a fourth word:")
word4 = input()
print("The meaning of", word4, "is", dictationary.get(word4))

print("Enter a fifth word:")
word5 = input()
print("The meaning of", word5, "is", dictationary.get(word5))
