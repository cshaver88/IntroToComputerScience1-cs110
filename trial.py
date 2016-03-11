def millions(num):
    return str(num/1000000)

def thousands(num):
    thou=num%1000000/1000
    thoustr=str(thou)
    if thou<=99:
        thoustr="0" +thoustr
    if thou<10:
        thoustr="0" + thoustr
    return thoustr

def last3dig(num):
    last3=num%1000
    last3str=str(last3)
    if last3<=99:
        last3str="0" +last3str
    if last3<10:
        last3str= "0" + last3str
    return last3str

def get_input():
    int9 = input("Enter an integer of up to 9 digits: ")
    return int9

def print_nums(original_num, numString):
    print "The 7-9 digit integer you entered is: ", original_num
    print "Your integer formatted with commas is: ", numString

int9dig = get_input()
numStr = millions(int9dig) + ','
numStr = numStr+thousands(int9dig) + ','
numStr = numStr+last3dig(int9dig)
print_nums(int9dig, numString)
