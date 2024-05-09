def generate_subsets(nums):
    subsets = []
    def backtrack(start, path):
        subsets.append(path[:])  # Add a copy of the current subset to the result
        for i in range(start, len(nums)):
            path.append(nums[i])  # Include the current element in the subset
            backtrack(i + 1, path)  # Recur with the next index
            path.pop()  # Backtrack: remove the last element to explore other possibilities

    backtrack(0, [])
    return subsets

nums = [1, 2, 3]
result = generate_subsets(nums)
print(result)
