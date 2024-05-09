# # pair of sums
# a = [6,0,3,4,5,6]
# ans = 10
# first = 1
# for i in range(0,len(a)):
#     for j in range(0,len(a)):  
#         if a[first] + a[i] == ans:
#             print(f"{a[i]} + {a[first]} == {ans}")
#             break
#     first += 1 
# else:
#      print("there is no pair values")    

a = [8, 0, 4, 2, 5, 6]
ans = 10
first = 0
answer = False
for i in range(len(a)):
    for j in range(len(a)):
        if first < len(a) and i < len(a) and a[first] != a[j]:  # Check if indices are within bounds
            print(j)
            if a[first] + a[j] == ans:
                print(j)
                b = a[first]
                c = a[j]
                answer = True
                
            break

    first += 1

if answer:
    print(f"{c} + {b} = {ans}")
else:
    print("no")

