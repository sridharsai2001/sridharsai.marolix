def remove_blank_spaces(input_string):
    return input_string.replace(" ", "")


original_string = "Hello,  world!  "
result_string = remove_blank_spaces(original_string)
print(result_string) 
