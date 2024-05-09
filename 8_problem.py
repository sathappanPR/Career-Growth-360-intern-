# def find_uncommon_numbers(array1, array2):
#     set1 = set(array1)
#     set2 = set(array2)
    
#     uncommon_numbers = list(set1.symmetric_difference(set2))

#     return uncommon_numbers

# array1 = [1, 2, 3, 4, 5]
# array2 = [1, 2, 3, 4, 5]

# result = find_uncommon_numbers(array1, array2)

# if len(result) != 0:
#     print("Uncommon numbers:", result)
# else:
#     print("no")

def find_uncommon_numbers_with_index(array1, array2):
    set1 = set(array1)
    set2 = set(array2)

    uncommon_numbers = list(set1.symmetric_difference(set2))

    for number in uncommon_numbers:
        index1 = array1.index(number) if number in array1 else None
        index2 = array2.index(number) if number in array2 else None

        print(f"Number {number} - Index in array1: {index1}, Index in array2: {index2}")

array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

find_uncommon_numbers_with_index(array1, array2)

