##def func(lst):
##    if len(lst) == 1:
##        return lst[0]
##    mintail = func(lst[1:])
##    if mintail > lst[0]:
##        return lst[0]
##    else:
##        return mintail
##        
##print func([2, 3, 1, 4])



##def findminindex(lst):
##    minindex = 0
##    for i in range(len(lst)):
##        if lst[minindex] > lst[i]:
##            minindex = i
##    return minindex
##        
##        
##
##
##def change(lst):
##    minindex = findminindex(lst)
##    i = minindex
##    temp = lst[minindex]
##    while i > 0:
##        lst[i] = lst[i-1]
##        i -= 1
##    lst[0] = temp
##    return lst
##
##
##
##lst = [3, 2, 6, 0, 7, 1]
##print lst
##lst = change(lst)
##print lst


##def magvec(lst):
##    vec = 0
##    for elem in lst:
##        mag = elem ** elem
##        vec += mag
##    return vec ** 0.5
##
##def minmagindex(mat):
##    minindex = 0
##    for index in range(len(mat)):
##        new = magvec(mat[index])
##        if new < magvec(mat[minindex]):
##            minindex = index
##    return minindex
##        
##        
##    
##
##
##
##mat = [[50, 60, 70], [1, -4, 2], [20, 30, 40]]
##print minmagindex(mat)



def func(num):
    num1 = 0
    num2 = 1
    if num>=0:
        print num1,
    if num>= 1:
        print num2,
    for i in range(3, num +1):
        num3 = num1+num2
        print '!' + str(num3)
        num1=num2
        print "@" + str(num1)
        num2= num3
        print "#" + str(num2)
        print "$" + str(num3)
    print


func(6)



















