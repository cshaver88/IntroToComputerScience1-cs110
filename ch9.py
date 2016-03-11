##lst = ['spam!', 'one', ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
##for i in range(len(lst)):
##    print len(lst[i]),
##
##
##
##    


##"""
##    >>> a_list[3]
##    42
##    >>> a_list[6]
##    'Ni!'
##    >>> len(a_list)
##    8
##"""
##

####a_list = [0, 1, 2, 42, 4, 5, 'Ni!', 7]


##for i in range(len(a_list)):
##        print a_list[i]

##
##
##"""
##  >>> b_list[1:]
##  ['Stills', 'Nash']
##  >>> group = b_list + c_list
##  >>> group[-1]
##  'Young'
##"""
##
##b_list = [0, 'Stills', 'Nash']
##c_list = ['Young']
##
##for i in range(len(b_list)):
##        print 





##"""
##  >>> 'war' in mystery_list
##  False
##  >>> 'peace' in mystery_list
##  True
##  >>> 'justice' in mystery_list
##  True
##  >>> 'oppression' in mystery_list
##  False
##  >>> 'equality' in mystery_list
##  True
##"""
##
##mystery_list = ['peace', 'justice', 'equality']
##for i in mystery_list:
##    print


##
##"""
##  >>> range(a, b, c)
##  [5, 9, 13, 17]
##"""
##
##
##a = 5
##b = 18
##c = 4
##
##

##this = ['I', 'am', 'not', 'a', 'crook']
##that = ['I', 'am', 'not', 'a', 'crook']
##print "Test 1: %s" % (this is that)
##that = this
##print "Test 2: %s" % (this is that)

##"""
##  >>> 13 in junk
##  True
##  >>> del junk[4]
##  >>> junk
##  [3, 7, 9, 10, 17, 21, 24, 27]
##  >>> del junk[a:b]
##  >>> junk
##  [3, 7, 27]
##"""
##
##junk = [3, 7, 9, 10, 13, 17, 21, 24, 27]
##a = 2
##b = 7


##
##"""
##  >>> nlist[2][1]
##  0
##  >>> nlist[0][2]
##  17
##  >>> nlist[1][1]
##  5
##"""
##
##nlist = [[0, 1, 17], [0, 5], [1, 0]]
####
##
##message = "this??and??that"
##
##
##"""
##  >>> import string
##  >>> string.split(message, '??')
##  ['this', 'and', 'that']
##"""
##




##
##def add_vectors(u, v):
##    """
##      >>> add_vectors([1, 0], [1, 1])
##      [2, 1]
##      >>> add_vectors([1, 2], [1, 4])
##      [2, 6]
##      >>> add_vectors([1, 2, 1], [1, 4, 3])
##      [2, 6, 4]
##      >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
##      [13, -4, 13, 5]
##    """
##    result = []
##    for i in range(0, len(u)):
##        result = result + [u[i]+v[i]]
##    return result    
##
##

##def scalar_multiply(s, v):
##    """
##      >>> scalar_multiply(5, [1, 2])
##      [5, 10]
##      >>> scalar_multiply(3, [1, 0, -1])
##      [3, 0, -3]
##      >>> scalar_multiply(7, [3, 0, 5, 11, 2])
##      [21, 0, 35, 77, 14]
##    """
##    result = []
##    for i in range(0, len(v)):
##        result = result + [s * v[i]]
##    return result

##
##def dot_product(u, v):
##    """
##      >>> dot_product([1, 1], [1, 1])
##      2
##      >>> dot_product([1, 2], [1, 4])
##      9
##      >>> dot_product([1, 2, 1], [1, 4, 3])
##      12
##      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
##      0
##    """
##    result = 0
##    for i in range(0, len(u)):
##        result += (u[i] * v[i])
##    return result
####
##def add_row(matrix):
##    """
##      >>> m = [[0, 0], [0, 0]]
##      >>> add_row(m)
##      [[0, 0], [0, 0], [0, 0]]
##      >>> n = [[3, 2, 5], [1, 4, 7]]
##      >>> add_row(n)
##      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
##      >>> n
##      [[3, 2, 5], [1, 4, 7]]
##    """
##    import copy
##    copy.deepcopy(matrix)
##    new_matrix = [0] * len(matrix[0])
##    anything = matrix + [new_matrix]
##    return anything
##
##    
##
##    
##def add_column(matrix):
##    """
##      >>> m = [[0, 0], [0, 0]]
##      >>> add_column(m)
##      [[0, 0, 0], [0, 0, 0]]
##      >>> n = [[3, 2], [5, 1], [4, 7]]
##      >>> add_column(n)
##      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
##      >>> n
##      [[3, 2], [5, 1], [4, 7]]
##    """
##    import copy
##    copy.deepcopy(matrix)
##    new_matrix = []
##    for i in matrix:
##        new_matrix += [i + [0]]
##    return new_matrix


##def add_matrices(m1, m2):
##    """
##      >>> a = [[1, 2], [3, 4]]
##      >>> b = [[2, 2], [2, 2]]
##      >>> add_matrices(a, b)
##      [[3, 4], [5, 6]]
##      >>> c = [[8, 2], [3, 4], [5, 7]]
##      >>> d = [[3, 2], [9, 2], [10, 12]]
##      >>> add_matrices(c, d)
##      [[11, 4], [12, 6], [15, 19]]
##      >>> c
##      [[8, 2], [3, 4], [5, 7]]
##      >>> d
##      [[3, 2], [9, 2], [10, 12]]
##    """
##    result = []
##    for i in range(0, len(m1)):
##        result = result + [add_vectors(m1[i], m2[i])]
##    return result
##


##
##
##def scalar_mult(s, m):
##    """
##      >>> a = [[1, 2], [3, 4]]
##      >>> scalar_mult(3, a)
##      [[3, 6], [9, 12]]
##      >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
##      >>> scalar_mult(10, b)
##      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
##      >>> b
##      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
##    """
##    result = []
##    for i in range(0, len(m)):
##        result = result + [scalar_multiply(s, m[i])]
##    return result
##    



##def row_times_column(m1, row, m2, column):
##    """
##      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
##      19
##      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
##      22
##      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
##      43
##      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
##      50
##    """
##    result = 0
##    for i in range(len(m1[0])):
##        result += dot_product([m1[row][i]], [m2[i][column]])
##    return result
##
##
##
##
##
##
##
##
##def matrix_mult(m1, m2):
##    """
##      >>> matrix_mult([[1, 2], [3,  4]], [[5, 6], [7, 8]])
##      [[19, 22], [43, 50]]
##      >>> matrix_mult([[1, 2, 3], [4,  5, 6]], [[7, 8], [9, 1], [2, 3]])
##      [[31, 19], [85, 55]]
##      >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
##      [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
##    """
##    result = []
##    for i in range(len(m1)):
##        temp = []
##        for x in range(len(m1)):
##            temp += [row_times_column(m1, i, m2, x)]
##        result += [temp]
##    return result
##   




##def only_evens(numbers):
##    """
##      >>> only_evens([1, 3, 4, 6, 7, 8])
##      [4, 6, 8]
##      >>> only_evens([2, 4, 6, 8, 10, 11, 0])
##      [2, 4, 6, 8, 10, 0]
##      >>> only_evens([1, 3, 5, 7, 9, 11])
##      []
##      >>> only_evens([4, 0, -1, 2, 6, 7, -4])
##      [4, 0, 2, 6, -4]
##      >>> nums = [1, 2, 3, 4]
##      >>> only_evens(nums)
##      [2, 4]
##      >>> nums
##      [1, 2, 3, 4]
##    """
##    result = []
##    for i in range(len(numbers)):
##        if numbers[i] % 2 == 0:
##            result = result + [numbers[i]]
##    return result
##        


    


##def only_odds(numbers):
##    """
##      >>> only_odds([1, 3, 4, 6, 7, 8])
##      [1, 3, 7]
##      >>> only_odds([2, 4, 6, 8, 10, 11, 0])
##      [11]
##      >>> only_odds([1, 3, 5, 7, 9, 11])
##      [1, 3, 5, 7, 9, 11]
##      >>> only_odds([4, 0, -1, 2, 6, 7, -4])
##      [-1, 7]
##      >>> nums = [1, 2, 3, 4]
##      >>> only_odds(nums)
##      [1, 3]
##      >>> nums
##      [1, 2, 3, 4]
##    """
##    result = []
##    for i in range(len(numbers)):
##        if numbers[i] % 2 != 0:
##            result = result + [numbers[i]]
##    return result



##def multiples_of(num, numlist):
##    """
##        >>> multiples_of(3, [2, 6, 9, 15])
##        [6, 9, 15]
##        >>> multiples_of(2, [2, 6, 9, 10])
##        [2, 6, 10]
##        >>> multiples_of(7, [2, 21, 35, 10])
##        [21, 35]
##        >>> multiples_of(5, [12, 15, 2, 10])
##        [15, 10]
##    """
##    result = []
##    for i in range(len(numlist)):
##        if numlist[i] % num == 0:
##            result = result + [numlist[i]]
##    return result

##
##import string
##
##song = "123456789"
##
##print string.split(song)
##
##
##print string.join(song)
##
##
##
##print string.join(string.split(song))





import string

def replace(s, old, new):
    """
      >>> replace('Mississippi', 'i', 'I')
      'MIssIssIppI'
      >>> s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
      >>> replace(s, 'om', 'am')
      'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!'
      >>> replace(s, 'o', 'a')
      'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'
    """
    return string.join(string.split(s, old), new)
    

    
            




















if __name__ == '__main__':
    import doctest
    doctest.testmod()
