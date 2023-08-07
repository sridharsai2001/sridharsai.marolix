def remove_repeated_characters(input_string):
    unique_chars = []
    for char in input_string:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

# Example usage:
input_str = "abbcccddddeeeee"
result_str = remove_repeated_characters(input_str)
print(result_str)  # Output: "abcde"
