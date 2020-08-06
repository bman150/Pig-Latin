print ("Pig Latin Translator")


pig = "ay"

original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = original[0]
    new_word = word + first + pig
    new_word = new_word[1:]
    print(new_word)
else:
    print ("empty")
