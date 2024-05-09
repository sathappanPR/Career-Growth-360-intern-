def find_repeating_number(numbers):
    count_dict = {}
    print(count_dict," initial")

    for num in numbers:
        if num in count_dict:
            print(count_dict," Last")
            return num  # Found the repeating number
        else:
            count_dict[num] = 1
    
    return None  # No repeating number found

# Example usage:
numbers_list = [1, 2, 3, 4, 5]  # 2 is the repeating number
result = find_repeating_number(numbers_list)

if result is not None:
    print(f"The repeating number is: {result}")
else:
    print("No repeating number found")
