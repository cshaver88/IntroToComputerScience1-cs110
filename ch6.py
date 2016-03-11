####def surprise(i):
####    while i>=1:
####        print i
####        i=i-1
####    print "Ta Da!"
####
####i=10
####surprise(i)
##
##
####print "produces", '\n', "this", '\n', "output."
####
##
##
##def sqrt(n):
##    approx = n/2.0
##    better = (approx + n/approx)/2.0
##    while better != approx:
##        approx = better
##        better = (approx + n/approx)/2.0
##        print better
##    return approx
##    
##sqrt(25)
##
##
##
####def print_multiples(n, high):
####    i = 1
####    while i <= high:
####        print n*i, '\t',
####        i += 1
####    print
####
####def print_mult_table(high):
####    i = 1
####    while i <= high:
####        print_multiples(i, high)
####        i += 1



##NEW HW


##def sqrt(n):
##    approx = n/2.0
##    better = (approx + n/approx)/2.0
##    while better != approx:
##        approx = better
##        better = (approx + n/approx)/2.0
##        print better
##    return approx
##     
##sqrt(25)
##
##
##def print_multiples(n, high):
##    i =1
##    while i <= high:
##        print n*i, '\t',
##        i += 1
##    print
##
##def print_mult_table(high):
##    i = 1
##    while i <= high:
##        print_multiples(i, high)
##        i += 1
##
##high=4
##print_mult_table(high)
##
##def t_num(x):
##    return (x*(x+1))/2
##t_num=count # + output
##def print_triangular_numbers(n):
##    count=0
##    t_num=0
##    while count<n:
##        count+=1
##        t_num=count + t_num
##        print count, '\t', t_num
##
##print_triangular_numbers(5)

def is_prime(x):
    """
        >>> is_prime(1)
        True
        >>> is_prime(4)
        False
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    base=int(x/2)
    count=2
    while count>=base:
        if x%base==0:
            print False
        else:
            print True
        base+=1
        count+=1
    return

        
##
##def true_false():
##    is_prime(n)
##    if base==True:
##        print False
##    else:
##        print True
##is_prime(10)
##
##
####


###6
##    def num_digits(n):
##    """
##      >>> num_digits(12345)
##      5
##      >>> num_digits(0)
##      1
##      >>> num_digits(-12345)
##      5
##    """

##
##
##def num_even_digits(n):
##    """
##      >>> num_even_digits(123456)
##      3
##      >>> num_even_digits(2468)
##      4
##      >>> num_even_digits(1357)
##      0
##      >>> num_even_digits(2)
##      1
##      >>> num_even_digits(20)
##      2
##    """
##
##
##def print_digits(n):
##    """
##      >>> print_digits(13789)
##      9 8 7 3 1
##      >>> print_digits(39874613)
##      3 1 6 4 7 8 9 3
##      >>> print_digits(213141)
##      1 4 1 3 1 2
##    """
##
##
##def sum_of_squares_of_digits(n):
##    """
##      >>> sum_of_squares_of_digits(1)
##      1
##      >>> sum_of_squares_of_digits(9)
##      81
##      >>> sum_of_squares_of_digits(11)
##      2
##      >>> sum_of_squares_of_digits(121)
##      6
##      >>> sum_of_squares_of_digits(987)
##      194
##    """
##
##


    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
