def givemaxmin(a):
    a.sort()
    dic = {"Min":a[0], "Max":a[-1]}
    return(dic)

array = [1,3,65416,
         71,911,9,1791,]

print("Min of array: ",givemaxmin(array))