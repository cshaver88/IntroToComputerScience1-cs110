## Cayla Shaver
## These functions do many different things but they all revolve around string utilities and
## basic functions that are all used with strings.


## 1. Returns the number of occurrences of character c in string s.

def numOccur(s, c):
    """
    >>> numOccur('mississippi', 'i')
    4
    >>> numOccur('puppy', 'p')
    3
    >>> numOccur('shoes', 's')
    2
    >>> numOccur('banana', 'b')
    1
    >>> numOccur('silly', 'z')
    0
    """
    count = 0
    for elem in s:
        if elem == c:
            count += 1
    return count

 

## 2. Returns the index of the last occurrence of character c in string s
## or -1 if c does not occur in s.
 

def lastOccur(s, c):
    """
    >>> lastOccur('hello', 'h')
    0
    >>> lastOccur('mississippi', 'i')
    10
    >>> lastOccur('banana', 'n')
    4
    >>> lastOccur('erudite', 'z')
    -1
    >>> lastOccur('puppy', 'u')
    1
    """
    index = 0
    lastoccur = -1
    for elem in s:
        if elem == c:
            lastoccur = index
        index += 1    
    return lastoccur


### 3. Returns the index of the last occurrence of the character that most frequently occurs
### in string s or -1 if s is the empty string.


def lastOccurMostFreqChar(s):
    """
    >>> lastOccurMostFreqChar('')
    -1
    >>> lastOccurMostFreqChar('hello')
    3
    >>> lastOccurMostFreqChar('banana')
    5
    >>> lastOccurMostFreqChar('erudite')
    6
    >>> lastOccurMostFreqChar('puppy')
    3
    """
    mostfreq = -1
    mostchar = ''
    for elem in s:
        freq = numOccur(s, elem)
        if freq > mostfreq:
            mostfreq = freq
            mostchar = elem
    return lastOccur(s, mostchar)
            
      
        
        



### 4. Returns a new string that is equivalent to string s1 with string s2 inserted at index pos.
### Returns empty string if pos is negative or pos > length of s.

def insert(s1, s2, pos):
    """
    >>> insert('', 'world!', 0)
    'world!'
    >>> insert('world!', 'hello ', 0)
    'hello world!'
    >>> insert('jack and', ' jill', 9)
    ''
    >>> insert('jill', 'jack', 1)
    'jjackill'
    >>> insert('jack', 'jill', 2)
    'jajillck'
    >>> insert('jack', 'jill', -1)
    ''
    """
    newstr = ""
    index = 0
    if s1 == "":
        newstr += s2
    if pos > len(s1):
        return ""
    if pos < 0:
        return ""
    for elem in s1:
        if index == pos:
            newstr += s2
        newstr += elem
        index += 1
    return newstr
    



### 5. Returns a new string that is equivalent to string s with the character at pos replaced
### with character c. Returns empty string if pos is negative or pos > length of s.

def replace(s, pos, c):
    """
    >>> replace('hello,', 5, 'o')
    'helloo'
    >>> replace('hello', 3, 'o')
    'heloo'
    >>> replace('goodbye', 5, 'd')
    'goodbde'
    >>> replace('cat', 0, 'm')
    'mat'
    >>> replace('made', 1, ' ')
    'm de'
    >>> replace('made', -1, 'a')
    ''
    >>> replace('made', 5, 'a')
    ''
    """
    newstr = ""
    index = 0
    if pos > len(s):
        return ''
    if pos < 0:
        return ''
    for elem in s:
        if pos == index:
            newstr += c
        else:
            newstr += elem
        index += 1
    return newstr
    


### 6. Returns a new string consisting of the characters of string s from pos1 to pos2-1 inclusive.
### Returns the empty string if there is no valid slice beginning at pos1 and ending at pos2-1.

def substring(s, pos1, pos2):
    """
    >>> substring('cat', 0, 3)
    'cat'
    >>> substring('hello', 0, 2)
    'he'
    >>> substring('mississippi', 3, 8)
    'sissi'
    >>> substring('puppy', 1, 5)
    'uppy'
    >>> substring('jack and jill', 0, -1)
    ''
    >>> substring('shoes', -1, 0)
    ''
    """
    newstr = ""
    index = 0
    if pos2 < pos1:
        return ''
    if pos1 < 0:
        return ''
    for elem in s:
        if index >= pos1 and index <= pos2 -1:
            newstr += elem
        index += 1
    return newstr



### 7. Returns a new string that is equivalent to string s * n, where * is the string repetition
### operator.

def repeatStr(s, n):
    """
    >>> repeatStr('hello', 0)
    ''
    >>> repeatStr('cat', 2)
    'catcat'
    >>> repeatStr('bye', 5)
    'byebyebyebyebye'
    >>> repeatStr(' ', 1)
    ' '
    >>> repeatStr('bobby', 1)
    'bobby'
    >>> repeatStr('hi', 0)
    ''
    """
    newstr = ''
    count = 1
    while count <= n:
        if n == 0:
            return ''
        newstr += s
        count += 1
    return newstr
    








### 8. Returns an integer that is the integer equivalent of the string s.
### Assumes that s is the string version of a valid integer. Ex: str2int("106 ") -> 106

def str2int(s):
    """
    >>> str2int('-1000092')
    -1000092
    >>> str2int('-100')
    -100
    >>> str2int('10')
    10
    >>> str2int('47')
    47
    >>> str2int('7564')
    7564
    >>> str2int('0')
    0
    >>> str2int('-1')
    -1
    """
    neg = False
    newstr = ''
    if s[0] == '-':
        newstr = substring(s, 1, len(s))
        neg = True
    else:
        newstr = s
    start = len(newstr)
    index = 0
    for elem in newstr:
        start -= 1
        new = (ord(elem)-48) * 10**start
        index += new
    if neg == True:
        index = index * -1
    return index





### 9. Returns a string that is the string equivalent of valid integer i.
### Ex: int2str(-12) -> "-12 "

def int2str(i):
    """
    >>> int2str(-1000092)
    '-1000092'
    >>> int2str(-100)
    '-100'
    >>> int2str(10)
    '10'
    >>> int2str(47)
    '47'
    >>> int2str(7564)
    '7564'
    >>> int2str(0)
    '0'
    >>> int2str(-1)
    '-1'
    """
    strng = ''
    index = len(strng)
    newstr = ''
    if i == 0:
        return '0'
    if i < 0:
        i *= -1
        newstr += '-'
    while i > 0:
        strng += chr(i % 10 + 48)
        i = i / 10        
    for elem in strng:
        index -= 1
        newstr += strng[index]
    return newstr
        









### 10. Returns a new list whose elements are each of the characters in string s as ordered in s

def string2list(s):
    """
    >>> string2list ('hello')
    ['h', 'e', 'l', 'l', 'o']
    >>> string2list ('bye')
    ['b', 'y', 'e']
    >>> string2list ('puppy')
    ['p', 'u', 'p', 'p', 'y']
    >>> string2list ('string')
    ['s', 't', 'r', 'i', 'n', 'g']
    >>> string2list ('')
    []
    """
    newlst = []
    index = 0
    for elem in s:
        newlst += s[index]
        index += 1
    return newlst











### 11. Returns a new string whose characters are each of elements of lst as order in lst

def list2string(lst):
    """
    >>> list2string (['h', 'e', 'l', 'l', 'o'])
    'hello'
    >>> list2string (['b', 'y', 'e'])
    'bye'
    >>> list2string (['p', 'u', 'p', 'p', 'y'])
    'puppy'
    >>> list2string (['c', 'a', 't'])
    'cat'
    >>> list2string (['', ''])
    ''
    """
    newstr = ''
    index = 0
    for elem in range(len(lst)):
        newstr += lst[index]
        index += 1
    return newstr










### 12. Returns a new string that contains all the characters of string s sorted in ascending order.
### String s is converted to a list, sorted using selection sort, then converted back to a
### string and returned.
###Assumes s is a printable string, ie: characters have ASCII values between 32 and 255
### inclusive.

def sortStr(s):
    """
    >>> sortStr('helloeoruuivdworlkd sidoaepkmkjfla')
    ' aadddeeefhiijkkkllllmooooprrsuuvw'
    >>> sortStr('helloworld')
    'dehllloorw'
    >>> sortStr('goodbye')
    'bdegooy'
    >>> sortStr('racecar')
    'aaccerr'
    >>> sortStr('')
    ''
    >>> sortStr('cat')
    'act'
    >>> sortStr('alsdhgfohiwoejrhwkejfhiswhfiwuef')
    'adeeeffffghhhhhiiijjkloorssuwwww'
    >>> sortStr('hellogoodbyeeveryone')
    'bdeeeeeghllnoooorvyy'
    >>> sortStr('zzzxxyyyypppjsjsmnmnmnmn')
    'jjmmmmnnnnpppssxxyyyyzzz'
    >>> sortStr('9876543210')
    '0123456789'
    >>> sortStr('*&;</:^%">[]-$= #,@!')
    ' !"#$%&*,-/:;<=>@[]^'
    >>> sortStr('!@#$%^&*0987654321')
    '!#$%&*0123456789@^'
    >>> sortStr('ZXCVBNMASDFqwertyuiopasdfghjklzxcvbnmGHJKLQWERTYUIOP')
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    """
    lst = string2list(s)
    for index in range(len(lst)):
        minindex = index
        minlet = lst[index]
        for index2 in range(index, len(lst)):
            if lst[index2] < minlet:
                minlet = lst[index2]
                minindex = index2
        temp = lst[index]
        lst[index] = lst[minindex]
        lst[minindex] = temp
    return list2string(lst)

        
    
    











### 13. Returns a new string containing all the characters of s sorted in ascending order,
### employing a bucket sort with one bucket for each character O(n).
### Assumes s is a printable string, ie: characters have ASCII values between 32 and 255 inclusive.

def sortStr2(s):
    """
    >>> sortStr2('helloeoruuivdworlkd sidoaepkmkjfla')
    ' aadddeeefhiijkkkllllmooooprrsuuvw'
    >>> sortStr2('helloworld')
    'dehllloorw'
    >>> sortStr2('goodbye')
    'bdegooy'
    >>> sortStr2('racecar')
    'aaccerr'
    >>> sortStr2('')
    ''
    >>> sortStr2('cat')
    'act'
    >>> sortStr2('alsdhgfohiwoejrhwkejfhiswhfiwuef')
    'adeeeffffghhhhhiiijjkloorssuwwww'
    >>> sortStr2('hellogoodbyeeveryone')
    'bdeeeeeghllnoooorvyy'
    >>> sortStr2('zzzxxyyyypppjsjsmnmnmnmn')
    'jjmmmmnnnnpppssxxyyyyzzz'
    >>> sortStr2('9876543210')
    '0123456789'
    >>> sortStr2('*&;</:^%">[]-$= #,@!')
    ' !"#$%&*,-/:;<=>@[]^'
    >>> sortStr2('!@#$%^&*0987654321')
    '!#$%&*0123456789@^'
    >>> sortStr2('ZXCVBNMASDFqwertyuiopasdfghjklzxcvbnmGHJKLQWERTYUIOP')
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    """
    bucket = [0] * 255
    newstr = ''
    for elem in s:
        bucket[ord(elem)] += 1
    for index in range(len(bucket)):
        newstr += chr(index) * bucket[index]
    return newstr
    











if __name__ == '__main__':
    import doctest
    doctest.testmod()
