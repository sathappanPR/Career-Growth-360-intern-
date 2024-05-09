a = [1,2,-3,4,5,6,1]
a.sort()
length = len(a)
ans = False

for first in range(length):
    for second in range(length):
        for third in range(length):
            if (a[first] != a[second]
                and a[first] != a[third]
                and a[second] != a[third]
                and a[first] + a[second] +a[third] == 0):
                ans = True

if ans:
    print("yes")
else:
    print("no")