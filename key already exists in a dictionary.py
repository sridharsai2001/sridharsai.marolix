def check_key(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_check = 'b'
if check_key(my_dict, key_to_check):
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
