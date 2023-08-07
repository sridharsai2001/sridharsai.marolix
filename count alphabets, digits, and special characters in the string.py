def count_characters(string):
    alphabets = digits = special_chars = 0

    for char in string:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special_chars += 1

    return alphabets, digits, special_chars


input_string = "Hello123!@#"
result = count_characters(input_string)
print(f"Alphabets: {result[0]}")
print(f"Digits: {result[1]}")
print(f"Special characters: {result[2]}")
