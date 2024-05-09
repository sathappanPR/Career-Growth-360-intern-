def find_missing_number(arr):
    n = len(arr) + 1  # Expected length of the array including the missing number
    expected_sum = n * (n + 1) // 2  # Sum of the first n natural numbers
    print(expected_sum)
    actual_sum = sum(arr)  # Sum of the elements in the given array
    print(actual_sum)
    missing_number = expected_sum - actual_sum
    return missing_number

# Example usage:
my_array = [1, 2, 4, 6, 3, 7, 9]
missing_number = find_missing_number(my_array)

print(f"The missing number is: {missing_number}")
