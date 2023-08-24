def remove_key(dictionary, key_to_remove):
    if key_to_remove in dictionary:
        del dictionary[key_to_remove]
        print(f"Key '{key_to_remove}' has been removed from the dictionary.")
    else:
        print(f"Key '{key_to_remove}' not found in the dictionary.")

# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print("Original dictionary:", my_dict)

key_to_remove = input("Enter the key to remove: ")

remove_key(my_dict, key_to_remove)

print("Updated dictionary:", my_dict)
