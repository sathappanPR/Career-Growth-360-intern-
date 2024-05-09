# a = [10,5,3,6,9,7,25]

# ans = 40
# first = 0
# second = 1
# answer = False
# for i in range(len(a)):
#     for j in range(0,len(a)):
#         if first < len(a) and second < len(a) :  # Check if indices are within bounds
#             if a[first] + a[j] + a[second] == ans:
                
#                 b = a[first]
#                 c = a[j]
#                 d = a[second]
#                 answer = True
                
            
#     second += 1
#     first += 1
    
# if answer:
#     print(f"{c} + {b} + {d}== {ans}")
# else:
#     print("no")

a = [4,5,6,9,3,5,8,2,1,8,6,5,9,232]
ans = 240
out = False

for first in range(len(a)):
    for second in range(len(a)):
        for i in range(len(a)):
            if (first != second 
                and first != i
                and second != i
                and a[first]+ a[second]+ a[i] == ans):
                out = True
                b = a[first]
                c = a[second]
                d = a[i]

if out:
    print(f"{c} + {b} + {d}== {ans}")
else:
    print("no")