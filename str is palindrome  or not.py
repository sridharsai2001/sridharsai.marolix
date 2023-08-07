def is_palindrome(input_string): 
    input_string = input_string.lower()
    input_string = ''.join(char for char in input_string if char.isalnum()) 
    return input_string == input_string[::-1]
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

