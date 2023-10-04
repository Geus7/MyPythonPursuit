
def count_characters(text):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

    vowel_count = 0
    consonant_count = 0
    special_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
        else:
            special_count += 1

    return vowel_count, consonant_count, special_count
paragraph = input("Enter a paragraph: ")

vowels, consonants, special = count_characters(paragraph)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
print("Number of special characters:", special)
