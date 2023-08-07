def is_vowel_or_consonant(character):
    character = character.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
       if character.isalpha():
        if character in vowels:
            return "Vowel" 
        else:
            return "Consonant"
    else:
        return "Not a valid alphabet character"
character_to_check = 'A'
result = is_vowel_or_consonant(character_to_check)
print(f"The character '{character_to_check}' is a {result}.")
