def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    input_char = input("Enter the character to count: ")

    if len(input_char) != 1:
        print("Please enter only one character.")
    else:
        result = count_occurrences(input_string, input_char)
        print(f"The character '{input_char}' occurs {result} times in the string.")
