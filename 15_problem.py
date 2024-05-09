a = [1, 2, 3, 4, 5]
ans = 10
out = False

for first in range(len(a)): 
    for second in range(len(a)): 
        for third in range(len(a)): 
            for i in range(len(a)): 
            
                if (
                    first != second
                    and first != third
                    and first != i
                    and second != third
                    and second != i
                    and third != i
                    and a[first] + a[second] + a[third] + a[i] == ans
                ):
                    
                    print(first,"first")
                    print(third,"third")
                    print(second,"second")
                    print(i,"i")
                    out = True
                    b = a[first]
                    c = a[second]
                    d = a[third]
                    e = a[i]

if out:
    print(f"{b} + {c} + {d} + {e} = {ans}")
else:
    print("no")
