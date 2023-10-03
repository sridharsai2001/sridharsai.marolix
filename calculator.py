def add(*args):
    result = sum(args)
    return result

def subtract(*args):
    result = args[0] - sum(args[1:]) 
    return result

def multiply(*args):
    result = 1
     for num in args:
        result *= num
    return result

def divide(*args):
    if 0 in args[1:]:
        return "Division by zero is not allowed"
    result = args[0]
    for num in args[1:]:
        result /= num
    return result

while True:
    print("Options:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '0' to end the program")
    
    user_input = input(": ")
    
    if user_input == "0":
        break
    elif user_input in ("1", "2", "3", "4"):
        num_input = input("Enter numbers separated by spaces: ")
        num_list = [float(x) for x in num_input.split()]
        
        if user_input == "1":
            print("Result:", add(*num_list))
        elif user_input == "2":
            print("Result:", subtract(*num_list))
        elif user_input == "3":
            print("Result:", multiply(*num_list))
        elif user_input == "4":
            result = divide(*num_list)
            if isinstance(result, str):
                print(result)
            else:
                print("Result:", result)
        else:
            print("Invalid input")
    else:
        print("Invalid input")
