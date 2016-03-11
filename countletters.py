##import string
##
##def myreplace(old, new, s):
##    """
##        >>> myreplace(',', ';', 'this, that, and, some, other, thing')
##        'this; that; and; some; other; thing'
##        >>> myreplace(' ', '**', 'Words will now be separated by stars.')
##        'Words**will**now**be**separated**by**stars.'
##    """
##    return new.join(s.split(old))
##
##
##
##
##
##def cleanword(word):
##    """
##      >>> cleanword('what?')
##      'what'
##      >>> cleanword('"now!"')
##      'now'
##      >>> cleanword('?+="word!,@$()"')
##      'word'
##    """
##    new = ""
##    for char in word:
##        if char in string.lowercase:
##            new += char
##        elif char == " ":
##            new += char
##        elif char in string.uppercase:
##            new += char
##        else:
##            new += " "
##    return new
##            
##
##
##def has_dashdash(s):
##    """
##      >>> has_dashdash('distance--but')
##      True
##      >>> has_dashdash('several')
##      False
##      >>> has_dashdash('critters')
##      False
##      >>> has_dashdash('spoke--fancy')
##      True
##      >>> has_dashdash('yo-yo')
##      False
##    """
##    if "--" in s:
##        return True
##    return False
##
##
##def extract_words(s):
##    """
##      >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
##      ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
##      >>> extract_words('she tried to curtsey as she spoke--fancy')
##      ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
##    """
##    new = s.lower()
##    new=cleanword(new)
##    new = new.split()
##    return new
##    
##
##
##
##def wordcount(word, wordlist):
##    """
##      >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
##      ['now', 2]
##      >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
##      ['is', 4]
##      >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
##      ['time', 1]
##      >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
##      ['frog', 0]
##    """
##    count = 0
##    for elem in wordlist:
##        if elem == word:
##            count += 1
##    return [word, count]
##
##
##
##def wordset(wordlist):
##    """
##      >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
##      ['is', 'now', 'time']
##      >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
##      ['I', 'a', 'am', 'is']
##      >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
##      ['a', 'am', 'are', 'be', 'but', 'is', 'or']
##    """
##    new = ""
##    for elem in wordlist:
##        if elem not in new:
##            new += " "+ elem
##    return sorted(new.split())
##            
##
##
##
##    
##
##
##def longestword(wordset):
##    """
##      >>> longestword(['a', 'apple', 'pear', 'grape'])
##      5
##      >>> longestword(['a', 'am', 'I', 'be'])
##      2
##      >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
##      34
##    """
##    count = 0
##    for elem in wordset:
##        count = len(elem)
##    return count
##
##
##


##def sort_fruits():
##    infile = open('unsorted_fruits.txt', 'r')
##    text = infile.read()
##    infile.close()
##    newlist = text.split('\n')
##    for index in range(len(newlist)):
##        minindex = index
##        minlet = newlist[index]
##        for index2 in range(index, len(newlist)):
##            if newlist[index2]< minlet:
##                minlet = newlist[index2]
##                minindex = index2
##            temp = newlist[index]
##            newlist[index] = newlist[minindex]
##            newlist[minindex] = temp
##    outfile = open('sorted_fruits.txt', 'w')
##    for elem in newlist:
##        if elem == "":
##            continue
##        outfile.write(elem + '\n')
##    outfile.close
##    
##sort_fruits()
##        
##        




from sys import argv



##
##
####lst = argv[1:]
####mean = 0
####for elem in lst: 
####    mean += float(elem)
####print mean / len(lst)
####    
##




##lst = argv[1:]
##median = 0
##if len(lst) % 2 == 0:
##    low = (len(lst) / 2) - 1
##    high = (len(lst) / 2)
##    median = (float(lst[low]) + float(lst[high])) / 2
##    print median
##if len(lst) % 2 != 0:
##    middle = len(lst) / 2
##    median = lst[middle]
##    print median





def display(i):
    if i == 10: return 'LF'
    if i == 13: return 'CR'
    if i == 32: return 'SPACE' 
    return chr(i)

infile = argv[1]
story = open(infile, 'r')
text = story.read()
story.close()

counts = 128 * [0]

for letter in text:
    counts[ord(letter)] += 1

outfile = open(infile.replace(".txt", "") + '.dat', 'w')
outfile.write("%-12s%s\n" % ("Character", "Count"))
outfile.write("=================\n")

for i in range(len(counts)):
    if counts[i]:
        outfile.write("%-12s%d\n" % (display(i), counts[i]))

outfile.close()




##if __name__ == '__main__':
##    import doctest
##    doctest.testmod()
