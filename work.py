##range(10, 0, -2)
##
##range(10, 20, -1)
##


##this = ['I', 'am', 'not', 'a', 'crook']
##that = ['I', 'am', 'not', 'a', 'crook']
##print "Test 1: %s" % (this is that)
##that = this
##print "Test 2: %s" % (this is that)


n = input("Please enter a number: ")


def num(n):
    total = 0
    index = 1
    for i in range(0, n):
        total += index
        index += 1
    return total

print num(n)
