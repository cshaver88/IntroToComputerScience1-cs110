######if x<y:
######    print x, "is less than", y
######elifx>y:
######    prin
####
######def find(strng, ch, start=0):
######    ind = start
######    while ind < len(strng):
######        if strng[ind] == ch:
######            return ind
######        ind += 1
######    return -1
######
######
######
######def count_letters(string, letter):
######    count=0
######    location=0
######    while location!=-1:
######        location = find(string, letter, location+1)
######        if location != -1:
######            count += 1
######    return count
######
######
######count=count_letters("banana", "a")
######print count
######count=count_letters("mississippi", "i")
######print count
######count=count_letters("apple", "p")
######print count
######count=count_letters("pen", "e")
######print count
####
####
######STRING TOOLS. PY
####
######def reverse(s):
######    """
######      >>> reverse('happy')
######      'yppah'
######      >>> reverse('Python')
######      'nohtyP'
######      >>> reverse("")
######      ''
######      >>> reverse("P")
######      'P'
######    """
######    count=len(s)-1
######    a=""
######    while count != -1:
######        a+=s[count]
######        count -= 1
######    return a
######    
######
######def mirror(s):
######    """
######      >>> mirror("good")
######      'gooddoog'
######      >>> mirror("yes")
######      'yessey'
######      >>> mirror('Python')
######      'PythonnohtyP'
######      >>> mirror("")
######      ''
######      >>> mirror("a")
######      'aa'
######    """
######    count=0
######    b=""
######    b+=s
######    b+=reverse(s)
######    return b
######
######
######
######def remove_letter(letter, strng):
######    """
######      >>> remove_letter('a', 'apple')
######      'pple'
######      >>> remove_letter('a', 'banana')
######      'bnn'
######      >>> remove_letter('z', 'banana')
######      'banana'
######      >>> remove_letter('i', 'Mississippi')
######      'Msssspp'
######    """
######    remove=letter
######    new_word=""
######    for letter in strng:
######        if letter not in remove:
######            new_word += letter
######    return new_word
####
####
####
######palindrome word that is the same backwards and forwards
####
######def is_palindrome(s):
######    """
######      >>> is_palindrome('abba')
######      True
######      >>> is_palindrome('abab')
######      False
######      >>> is_palindrome('tenet')
######      True
######      >>> is_palindrome('banana')
######      False
######      >>> is_palindrome('straw warts')
######      True
######    """
######    count=len(s)-1
######    a=""
######    while count != -1:
######        a+=s[count]
######        count -= 1
######        if a == s:
######            return True
######        
######    return False
####    
####
####
####
####
####
######def count(sub, s):
######    """
######      >>> count('is', 'Mississippi')
######      2
######      >>> count('an', 'banana')
######      2
######      >>> count('ana', 'banana')
######      2
######      >>> count('nana', 'banana')
######      1
######      >>> count('nanan', 'banana')
######      0
######    """
######    index = 0
######    count = 0
######    while index <= len(s):
######        index += 1
######        if s[index:index + len(sub)] == sub:
######            count += 1
######    return count 
######    
####
####
####      
####    
####def remove(sub, s):
####    """
####      >>> remove('an', 'banana')
####      'bana'
####      >>> remove('cyc', 'bicycle')
####      'bile'
####      >>> remove('iss', 'Mississippi')
####      'Missippi'
####      >>> remove('egg', 'bicycle')
####      'bicycle'
####    """
####    index = 0
####    new_word = ""
####    while index <= len(s):
####        if s[index:index + len(sub)] == sub:
####            break
####        index += 1
####    new_word=s[:index] + s[index + len(sub):]    
####    return new_word
####
####   
####
####
####
####def remove_all(sub, s):
####    """
####      >>> remove_all('an', 'banana')
####      'ba'
####      >>> remove_all('cyc', 'bicycle')
####      'bile'
####      >>> remove_all('iss', 'Mississippi')
####      'Mippi'
####      >>> remove_all('eggs', 'bicycle')
####      'bicycle'
####    """
####    while True:
####        s=remove(sub, s)
####        if s==remove(sub, s):
####            break
####    return s
####        
####        
####
####
####
####
####
####
####    
######    index = 0
######    new_word = ""
######    while index <= len(s):
######        if s[index:index + len(sub)] == sub:
######            break
######        index += 1
######    new_word=s[:index] + s[index + len(sub):]    
######    return new_word
####
####
####
####
####
####
####
####
####
######
######
####
####if __name__ == '__main__':
####    import doctest
####    doctest.testmod()
####
##
##
##
##
##
##
##
##def get_input():
##    first=raw_input("Please enter your first name: ")
##    last=raw_input("Please enter your last name: ")
##    dna=raw_input("Please enter your DNA: ")
##    return (first, last, dna)
##
##
##
##
##def countCAG(dna):
##    """
##    >>> countCAG("CAGTAC")
##    1
##    >>> countCAG("CAGCAGCAGCAGCAT")
##    4
##    >>> countCAG("CAGCAGCAGACT")
##    3
##    >>> countCAG("CAGCAGCATCAACTGACCAGCAGGCAGCAGCAGCAGCAGCAG")
##    2
##    >>> countCAG("CAGCAGCAGCAGCAGGATATG")
##    5
##    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGTACCAGCAGCAGCAT")
##    12
##    >>> countCAG("TACCAGCAGACT")
##    0
##    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAG")
##    9
##    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCATCATTACACTCAGCAGCAGCAGCAGCAGCAGCAGCAG")
##    15
##    """
##    index = 0
##    count = 0
##    end = 3
##    while index <= len(dna):
##        if dna[index:end] == "CAG":
##            count += 1
##            index += 3
##            end += 3
##        else:
##            return count
##    return count
##
##
##def prediction(numCAG):
##    """
##    >>> prediction(70)
##    ('Full Penetrance', 'Affected')
##    >>> prediction(40)
##    ('Reduced Penetrance', 'Somewhat Affected')
##    >>> prediction(32)
##    ('Intermediate', 'Unaffected')
##    >>> prediction(2)
##    ('Normal', 'Unaffected')
##    >>> prediction(42)
##    ('Full Penetrance', 'Affected')
##    >>> prediction(38)
##    ('Reduced Penetrance', 'Somewhat Affected')
##    >>> prediction(29)
##    ('Intermediate', 'Unaffected')
##    >>> prediction(15)
##    ('Normal', 'Unaffected')
##    """
##    if numCAG <= 26:
##        return 'Normal', 'Unaffected'
##    elif 27 <= numCAG <= 35:
##        return 'Intermediate', 'Unaffected'
##    elif 36 <= numCAG <= 40:
##        return 'Reduced Penetrance', 'Somewhat Affected'
##    else:
##        return 'Full Penetrance', 'Affected'
##
##
##
##    ##_main_##
##(firstname, lastname, DNA) = get_input()
##
##print "Patient's Name: ", lastname, ',', firstname
##print "DNA Sequence: ", DNA
##print "Number Of CAG Repeats: ", countCAG(DNA)
##print "Risk Of Infection: ", prediction(countCAG(DNA))
##
##
##
##
##
##
##
##
##
##
##
##
##
####
####if __name__ == '__main__':
####    import doctest
####    doctest.testmod()
##
##
##
##
####
##
##
##
##
##def list_factors(num):
##    count = 5
##    factors = ""
##    while count > num:
##        if num % count == 0:
##            factors = count
##            count += 1
##        else:
##            count += 1
##            return factors
##
##
##
##num = 35
##list_factors(num)
##
##
##
##

def lowest_int(num):
    index = 2
    while (num % index !=0):
        index += 1
    return index

def prime_fact(num):
    low = lowest_int(num)
    while num != low:
        low = lowest_int(num)
        if low == num:
            print low,
            break
        print low,
        num = num/low 

prime_fact(12)





