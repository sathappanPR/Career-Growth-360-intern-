def shortthird(a):
    if len(a) < 3:
        print ("It is in valid")
        
    elif len(a) > 3:
        a.sort()
        print("this is the sorted array: ",a)
        print(a[3])

array=[1,2]
print(shortthird(array))