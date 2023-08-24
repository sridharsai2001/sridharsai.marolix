def sum_dictionary_values(dictionary):
    total_sum = 0
    for value in dictionary.values():
        total_sum += value
    return total_sum

# Example dictionary
example_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# Calculate and print the sum of values in the dictionary
result = sum_dictionary_values(example_dict)
print("Sum of dictionary values:", result)
