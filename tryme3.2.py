def new_line():
    print

def three_lines():
    new_line()
    new_line()
    new_line()
    print

def nine_lines():
    three_lines()
    three_lines()
    three_lines()
    print

def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

print "A"
new_line()
print "B"
three_lines()
print"C"
nine_lines()
print "D"
clear_screen()
