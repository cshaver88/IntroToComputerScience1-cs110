##def fibonacci(n):
##    if n == 0 or n == 1:
##        return 1
##    else:
##        return fibonacci(n-1) + fibonacci(n-2)
##
##
##print fibonacci(35)



##
##def swap(x, y):      # incorrect version
##     print  "before swap statement: id(x):", id(x), "id(y):", id(y)
##     x, y = y, x
##     print  "after swap statement: id(x):", id(x), "id(y):", id(y)
##
##a, b = 0, 1
##print  "before swap function call: id(a):", id(a), "id(b):", id(b)
##swap(a, b)
##print  "after swap function call: id(a):", id(a), "id(b):", id(b)
##
##print a
##print b








##
##def encapsulate(val, seq):
##     """
##          >>> encapsulate("a", (1, 2, 3, 4))
##          ('a',)
##          >>> encapsulate("1", (1, 2, 3, 4))
##          ('1',)
##          >>> encapsulate("a", [1, 2, 3, 4])
##          ['a']
##          >>> encapsulate("1", [1, 2, 3, 4])
##          ['1']
##          >>> encapsulate(1, (1, 2, 3, 4))
##          (1,)
##          >>> encapsulate(1, [1, 2, 3, 4])
##          [1]
##          >>> encapsulate("a", "bt")
##          'a'
##     """
##     if type(seq) == type(""):
##        return str(val)
##     if type(seq) == type([]):
##        return [val]
##     return (val,)
##
##
##
##
##
##
##
##def insert_in_middle(val, seq):
##     """
##          >>> insert_in_middle(1, (1, 2, 3, 4))
##          (1, 2, 1, 3, 4)
##          >>> insert_in_middle(1, [1, 2, 3, 4])
##          [1, 2, 1, 3, 4]
##          >>> insert_in_middle("hi", "cups")
##          'cuhips'
##          >>> insert_in_middle("cups", "hi")
##          'hcupsi'
##     """
##     middle = len(seq)/2
##     return seq[:middle] + encapsulate(val, seq) + seq[middle:]
##
##
##
##
##
##
##def make_empty(seq):
##     """
##      >>> make_empty([1, 2, 3, 4])
##      []
##      >>> make_empty(('a', 'b', 'c'))
##      ()
##      >>> make_empty("No, not me!")
##      ''
##     """
##     if type(seq) == type(""):
##          return str()
##     if type(seq) == type([]):
##          return []
##     else:
##          return ()
##
##
##
##
##def insert_at_end(val, seq):
##     """
##      >>> insert_at_end(5, [1, 3, 4, 6])
##      [1, 3, 4, 6, 5]
##      >>> insert_at_end('x', 'abc')
##      'abcx'
##      >>> insert_at_end(5, (1, 3, 4, 6))
##      (1, 3, 4, 6, 5)
##     """
##     return seq[:] + encapsulate(val, seq)
##
##
##
##
##def insert_in_front(val, seq):
##     """
##      >>> insert_in_front(5, [1, 3, 4, 6])
##      [5, 1, 3, 4, 6]
##      >>> insert_in_front(5, (1, 3, 4, 6))
##      (5, 1, 3, 4, 6)
##      >>> insert_in_front('x', 'abc')
##      'xabc'
##     """
##     front = encapsulate(val, seq)
##     return front + seq[:]
##
##
##
##
##def index_of(val, seq, start=0):
##     """
##      >>> index_of(9, [1, 7, 11, 9, 10])
##      3
##      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
##      3
##      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
##      6
##      >>> index_of('y', 'happy birthday')
##      4
##      >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
##      1
##      >>> index_of(5, [2, 3, 4])
##      -1
##      >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
##      -1
##     """
##     index = 0
##     for elem in seq:
##          if elem == val and start <= index:
##               return index
##          index += 1
##     return -1
##     
##          
##
##
##
##
##def remove_at(index, seq):
##     """
##      >>> remove_at(3, [1, 7, 11, 9, 10])
##      [1, 7, 11, 10]
##      >>> remove_at(5, (1, 4, 6, 7, 0, 9, 3, 5))
##      (1, 4, 6, 7, 0, 3, 5)
##      >>> remove_at(2, "Yomrktown")
##      'Yorktown'
##     """
##     count = 0
##     new = make_empty(seq)
##     while count < len(seq):
##          if count != index:
##               new += encapsulate(seq[count], new)
##          if count == index:
##               count += 1
##               continue
##          count += 1
##     return new
##
##     
##
##
##
##
##def remove_val(val, seq):
##     """
##      >>> remove_val(11, [1, 7, 11, 9, 10])
##      [1, 7, 9, 10]
##      >>> remove_val(15, (1, 15, 11, 4, 9))
##      (1, 11, 4, 9)
##      >>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
##      ('who', 'when', 'where', 'why', 'how')
##     """
##     new = make_empty(seq)
##     index = index_of(val, seq, start=0)
##     count = remove_at(index, seq)
##     return count
##
##
##
##
##
##
##
##def remove_all(val, seq):
##     """
##      >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
##      [1, 7, 9, 10, 2]
##      >>> remove_all('i', 'Mississippi')
##      'Msssspp'
##     """
##     new = remove_val(val, seq)
##     for elem in new:
##          new = remove_val(val, new)
##     return new
##
##
##
##
##def count(val, seq):
##     """
##      >>> count(5, (1, 5, 3, 7, 5, 8, 5))
##      3
##      >>> count('s', 'Mississippi')
##      4
##      >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
##      2
##     """
##     count = 0
##     for elem in seq:
##          if elem == val:
##               count += 1
##     return count
##
##
##
##def reverse(seq):
##     """
##      >>> reverse([1, 2, 3, 4, 5])
##      [5, 4, 3, 2, 1]
##      >>> reverse(('shoe', 'my', 'buckle', 2, 1))
##      (1, 2, 'buckle', 'my', 'shoe')
##      >>> reverse('Python')
##      'nohtyP'
##     """
##     index = len(seq) - 1
##     new = make_empty(seq)
##     for elem in seq:
##          new += encapsulate(seq[index], new)
##          index -= 1
##     return new
##          
##     
##     
##
##

def sort_sequence(seq):
     """
      >>> sort_sequence([3, 4, 6, 7, 8, 2])
      [2, 3, 4, 6, 7, 8]
      >>> sort_sequence((3, 4, 6, 7, 8, 2))
      (2, 3, 4, 6, 7, 8)
      >>> sort_sequence("nothappy")
      'ahnoppty'
     """
     new = make_empty(seq)
     for i in range(len(seq)):
          minindex = i
          for j in range(i, len(seq)):
               if seq[j] < seq[minindex]:
                    minindex = j
          new += encapsulate(seq[j], new)
     return new





##def flatten(nested_num_list):
##     """
##          >>> flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]])
##          [2, 9, 2, 1, 13, 2, 8, 2, 6]
##          >>> flatten([[9, [7, 1, 13, 2], 8], [7, 6]])
##          [9, 7, 1, 13, 2, 8, 7, 6]
##          >>> flatten([[9, [7, 1, 13, 2], 8], [2, 6]])
##          [9, 7, 1, 13, 2, 8, 2, 6]
##          >>> flatten([[5, [5, [1, 5], 5], 5], [5, 6]])
##          [5, 5, 1, 5, 5, 5, 5, 6]
##     """
##     newlist = []
##     for elem in nested_num_list:
##          if type(elem) == type([]):
##               newlist += flatten(elem)
##          else: 
##               newlist += [elem]
##     return newlist




##def readposint(text="Please enter a positive integer: "):
##     try:
##          num = input(text)
##          if num < 0:
##               raise Exception(" is not a positive integer. Try again.")
##          elif num == '':
##               raise Exception(" is not a positive integer. Try again.")
##          elif type(num) == type(10.00):
##               raise Exception(" is not a positive integer. Try again.")
##          else:
##               return num
##     except:
##          return readposint()
##
##
##
##
##
##print readposint()
##



def factorial(n):
     sofar = 1
     while n != 0:
          sofar *= n
          n -= 1
     return sofar


print factorial(1000)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
