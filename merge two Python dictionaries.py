def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Make a copy of the first dictionary
    
    for key, value in dict2.items():
        if key in merged_dict:
            # If the key already exists in the merged dictionary, update the value
            if isinstance(merged_dict[key], dict) and isinstance(value, dict):
                # Recursively merge nested dictionaries
                merged_dict[key] = merge_dicts(merged_dict[key], value)
            else:
                merged_dict[key] = value
        else:
            # If the key doesn't exist in the merged dictionary, add it
            merged_dict[key] = value
    
    return merged_dict

# Example dictionaries to merge
dict1 = {'a': 1, 'b': 2, 'c': {'x': 10, 'y': 20}}
dict2 = {'b': 3, 'c': {'y': 30, 'z': 40}, 'd': 4}

merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)
