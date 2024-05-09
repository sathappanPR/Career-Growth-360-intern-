a = [5,6,9,7,5,3]
b = [6,9,7,15]
count = 0
for first in range(len(a)):
    for second in range(len(b)):
        if (a[first] == b[second]):
            count += 1

print(count)