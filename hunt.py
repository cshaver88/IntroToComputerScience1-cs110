##Huntington's Disease Program
##Created By:  Cayla Shaver
##This program takes the user's information and determines the liklihood of the user developing Huntington's Disease.
##To use this program just enter the information that the page asks you for and the program will generate the results.



##This function returns the user's information they put into the textboxes within the page. The input from the user is used to calculate the probability of them, according to their DNA, developing Huntington's Disease.
def get_input():
    first=raw_input("Please enter your first name: ")
    last=raw_input("Please enter your last name: ")
    dna=raw_input("Please enter your DNA: ")
    return (first, last, dna)



##This function looks at the DNA that is entered by the user and counts the number of repeats of CAG, and returns the number of repeats; starting at the beginning of the string and stopping when the CAG is no longer repeated.
def countCAG(dna):
    """
    >>> countCAG("CAGTAC")
    1
    >>> countCAG("CAGCAGCAGCAGCAT")
    4
    >>> countCAG("CAGCAGCAGACT")
    3
    >>> countCAG("CAGCAGCATCAACTGACCAGCAGGCAGCAGCAGCAGCAGCAG")
    2
    >>> countCAG("CAGCAGCAGCAGCAGGATATG")
    5
    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGTACCAGCAGCAGCAT")
    12
    >>> countCAG("TACCAGCAGACT")
    0
    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAG")
    9
    >>> countCAG("CAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCAGCATCATTACACTCAGCAGCAGCAGCAGCAGCAGCAGCAG")
    15
    """
    index = 0
    count = 0
    end = 3
    while index <= len(dna):
        if dna[index:end] == "CAG":
            count += 1
            index += 3
            end += 3
        else:
            return count
    return count

##This function looks at the returned number of CAG repeats and evaluates the number and returns the correct prediction dependent on the size of the number of CAG repeats.
def prediction(numCAG):
    """
    >>> prediction(70)
    ('Full Penetrance', 'Affected')
    >>> prediction(40)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(32)
    ('Intermediate', 'Unaffected')
    >>> prediction(2)
    ('Normal', 'Unaffected')
    >>> prediction(42)
    ('Full Penetrance', 'Affected')
    >>> prediction(38)
    ('Reduced Penetrance', 'Somewhat Affected')
    >>> prediction(29)
    ('Intermediate', 'Unaffected')
    >>> prediction(15)
    ('Normal', 'Unaffected')
    """
    if numCAG <= 26:
        return 'Normal', 'Unaffected'
    elif 27 <= numCAG <= 35:
        return 'Intermediate', 'Unaffected'
    elif 36 <= numCAG <= 40:
        return 'Reduced Penetrance', 'Somewhat Affected'
    else:
        return 'Full Penetrance', 'Affected'



    ##_main_##
(firstname, lastname, DNA) = get_input()

print "Patient's Name: ", lastname, ',', firstname
print "DNA Sequence: ", DNA
print "Number Of CAG Repeats: ", countCAG(DNA)
print "Risk Of Infection: ", prediction(countCAG(DNA))














if __name__ == '__main__':
    import doctest
    doctest.testmod()
