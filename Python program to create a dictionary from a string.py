def create_letter_count_dict(input_string):
    letter_count_dict = {}
    
    for char in input_string:
        if char.isalpha():
            char_lower = char.lower() 
            if char_lower in letter_count_dict:
                letter_count_dict[char_lower] += 1
            else:
                letter_count_dict[char_lower] = 1
    
    return letter_count_dict
sample_string = 'marolix technology'
result = create_letter_count_dict(sample_string)
print(result)
