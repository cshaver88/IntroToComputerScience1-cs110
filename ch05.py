###1.
###def compare(a, b):
## #   """
##  #    >>> compare(5, 4)
##   #   1
##    #  >>> compare(7, 7)
##     # 0
##      #>>> compare(2, 3)
###      -1
## #     >>> compare(42, 1)
##  #    1
##   # """
##    #if a>b:
##     #   return 1
##    #elif a==b:
##     #   return 0
##    #else:
##     #   return -1
##    
##
##
##
###2
###def hypotenuse(a, b):
## #   """
##  #    >>> hypotenuse(3, 4)
##   #   5.0
##    #  >>> hypotenuse(12, 5)
##     # 13.0
##      #>>> hypotenuse(7, 24)
###      25.0
## #     >>> hypotenuse(9, 12)
##  #    15.0
##   # """
##    #c2=(a**2+b**2)
##    #c=c2**.5
##    #return c
##
##
###3
##def slope(x1, y1, x2, y2):
##    """
##      >>> slope(5, 3, 4, 2)
##      1.0
##      >>> slope(1, 2, 3, 2)
##      0.0
##      >>> slope(1, 2, 3, 3)
##      0.5
##      >>> slope(2, 4, 1, 2)
##      2.0
##      >>> slope(6, 1, 1, 6)
##      -1.0
##    """
##    m=float(y1-y2)/float(x1-x2)
##    if abs(m-0)<.000001:
##        m=float(0)
##    return m 
##    
##
##def intercept(x1, y1, x2, y2):
##    """
##      >>> intercept(1, 6, 3, 12)
##      3.0
##      >>> intercept(6, 1, 1, 6)
##      7.0
##      >>> intercept(4, 6, 12, 8)
##      5.0
##    """
##    m=slope(x1, y1, x2, y2)
##    b=y1-m*x1
##    return b
##
##
##result=intercept(6, 1, 1, 6)
##print abs(result)
##    
##
###4
###def is_even(n):
## #   """
##  #      >>> is_even(0, 2, 4, 6, 8)
##   #     True
##   #     >>> is_even(1, 3, 5, 7, 9)
##    #    False
##    #"""
##    #is_even(n)
    
##4
##def is_even(n):
##    """
##    >>> is_even(332)
##    True
##    >>> is_even(15)
##    False
##    >>> is_even(450)
##    True
##    >>> is_even(64)
##    True
##    """
##    result=n%2
##    if n%2==0:
##        return True
##    else:
##        return False        


######5
##def is_odd(n):
##    """
##    >>> is_odd(24)
##    False
##    >>> is_odd(23)
##    True
##    >>> is_odd(75)
##    True
##    >>> is_odd(220)
##    False
##    """
##    result=n%2
##    if n%2==0:
##        return False
##    else:
##        return True
##
######5 part 2
##def is_even(n):
##    """
##    >>> is_even(332)
##    True
##    >>> is_even(15)
##    False
##    >>> is_even(450)
##    True
##    >>> is_even(64)
##    True
##    """
##    result=n%2
##    if n%2==0:
##        return True
##    else:
##        return False
##
##def is_odd(n):
##    """
##    >>> is_odd(24)
##    False
##    >>> is_odd(23)
##    True
##    >>> is_odd(75)
##    True
##    >>> is_odd(220)
##    False
##    """
##    return not is_even(n)

##def is_factor(f, n):
##    """
##    >>> is_factor(3, 12)
##    True
##    >>> is_factor(5, 12)
##    False
##    >>> is_factor(7, 14)
##    True
##    >>> is_factor(2, 14)
##    True
##    >>> is_factor(7, 15)
##    False
##    """
##    result=n%f==0
##    if n%f==0:
##        return True
##    else:
##        return False

##
##def is_multiple(m, n):
##    """
##    >>> is_multiple(12, 3)
##    True
##    >>> is_multiple(12, 4)
##    True
##    >>> is_multiple(12, 5)
##    False
##    >>> is_multiple(12, 6)
##    True
##    >>> is_multiple(12, 7)
##    False
##    """
##    result=m%n==0
##    if m%n==0:
##        return True
##    else:
##        return False


##def is_factor(f, n):
##    """
##      >>> is_factor(3, 12)
##      True
##      >>> is_factor(5, 12)
##      False
##      >>> is_factor(7, 14)
##      True
##      >>> is_factor(2, 14)
##      True
##      >>> is_factor(7, 15)
##      False
##    """
##    n%f==0
##    if n%f==0:
##        return True
##    else:
##        return False
##
##def is_multiple(m, n):
##    """
##      >>> is_multiple(12, 3)
##      True
##      >>> is_multiple(12, 4)
##      True
##      >>> is_multiple(12, 5)
##      False
##      >>> is_multiple(12, 6)
##      True
##      >>> is_multiple(12, 7)
##      False
##    """
##    x=is_factor(n, m)
##    return x    

##
##def f2c(t):
##    """
##      >>> f2c(212)
##      100
##      >>> f2c(32)
##      0
##      >>> f2c(-40)
##      -40
##      >>> f2c(36)
##      2
##      >>> f2c(37)
##      3
##      >>> f2c(38)
##      3
##      >>> f2c(39)
##      4
##    """
##    result=(t-float(32))*5/9
##    return int(round(result))
####
def c2f(t):
    """
      >>> c2f(0)
      32
      >>> c2f(100)
      212
      >>> c2f(-40)
      -40
      >>> c2f(12)
      54
      >>> c2f(18)
      64
      >>> c2f(-48)
      -54
    """
    result=float(t)*9/5+32
    return int(round(result))

if __name__ == '__main__':
    import doctest
    doctest.testmod()


