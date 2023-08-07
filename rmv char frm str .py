def remove_character_using_list_comprehension(input_string, character_to_remove):
    return ''.join([char for char in input_string if char != character_to_remove])


input_str = "Hello, World!"
character_to_remove = ","
result_str = remove_character_using_list_comprehension(input_str, character_to_remove)
print(result_str) 
