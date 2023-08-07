import re

def sum_of_integers_in_string(input_string):
 
    integer_matches = re.findall(r'-?\d+', input_string)

   
    sum_of_integers = sum(map(int, integer_matches))

    return sum_of_integers


input_str = "The sum of 1, 2, and 3 is 6."
result = sum_of_integers_in_string(input_str)
print("Sum of integers in the string:", result)  # Output: 12 (1 + 2 + 3 + 6)
