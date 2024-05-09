def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    rotated_array = arr[k:] + arr[:k]

    return rotated_array
original_array = [1, 2, 3, 4, 5]
k = 2

result = rotate_array(original_array, k)
print("Original Array:", original_array)
print(f"Rotated Array by {k} positions:", result)
