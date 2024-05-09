def count_triplets(arr):
    n = len(arr)
    count = 0

    for i in range(n - 2):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] == arr[k] or arr[j] + arr[k] == arr[i] or arr[i] + arr[k] == arr[j]:
                    count += 1

    return count

# Example usage:
arr = [3,2,4]
result = count_triplets(arr)
print("Number of triplets:", result)
