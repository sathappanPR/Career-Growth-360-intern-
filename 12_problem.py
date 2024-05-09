# def count_frequencies(N, arr, P):
#     # Initialize a dictionary to store frequencies
#     freq_dict = {}

#     # Count frequencies of each element in the array
#     for num in arr:
#         if num in freq_dict:
#             freq_dict[num] += 1
#         else:
#             freq_dict[num] = 1

#     # Initialize a list to store the output
#     output = []

#     # Generate the output based on frequencies
#     for i in range(0, P + 1):
#         if i in freq_dict:
#             output.append(freq_dict[i])
#         else:
#             output.append(0)

#     return output

# # Example usage
# N = 5
# arr = [2, 3, 2, 3, 5,0,0]
# P = 5
# result = count_frequencies(N, arr, P)
# print(result)

a = [ 1,2,2,3,5,6,6,10]

dec = {}

for num in a:
    if num in dec:
        dec[num] += 1
    else:
        dec[num] = 1

new = []

for i in range(0,11):
    if i in dec:
        new.append(dec[i])
    else:
        new.append(0)

print(new)

print(len(a))