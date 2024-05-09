a = 432
b = [
    335, 501 ,170 ,725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492,
    996 ,943, 828, 437, 392, 605, 903 ,154, 293, 383, 422, 717, 719, 896,
    448, 727, 772, 539, 870, 913, 668, 300 ,36, 895, 704, 812, 323 ,334
]
found = False

for i in b:
    if a == i:
       found = True
       break

if found:
    print(f"{a} value found")

else:
    print("not found")

# my_array = [1, 2, 3, 4, 5]

# element_to_search = 3

# try:
#     index = my_array.index(element_to_search)
#     print(f"{element_to_search} found at index {index}.")
# except ValueError:
#     print(f"{element_to_search} not found in the array.")
