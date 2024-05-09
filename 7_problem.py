def sep(a):
    low = 0
    mid = 0
    high = len(a)-1

    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    
    print(a)

numbers_list = [2, 0, 1, 2, 1, 0, 2, 0, 1]
sep(numbers_list)

print("Separated list:", sep(numbers_list))


# def separate_0_1_2(numbers):
#     low, mid, high = 0, 0, len(numbers) - 1

#     while mid <= high:
#         if numbers[mid] == 0:
#             numbers[low], numbers[mid] = numbers[mid], numbers[low]
#             low += 1
#             mid += 1
#         elif numbers[mid] == 1:
#             mid += 1
#         else:
#             numbers[mid], numbers[high] = numbers[high], numbers[mid]
#             high -= 1

# # Example usage:
# numbers_list = [2, 0, 1, 2, 1, 0, 2, 0, 1]
# separate_0_1_2(numbers_list)

# print("Separated list:", numbers_list)
