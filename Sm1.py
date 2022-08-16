def upper1(a):
    y=""
    for i in a:
        if (i>="A" and i<="Z"):
            y=y+chr(ord(i)+32)
        else:
            y=y+i
    return y
def lower1(a):
    y=""
    for i in a:
        if(ord(i)>=65 and ord(i)<=90):
            y=y+chr(ord(i)+32)
        else:
            y=y+i
    return y
a=ord("A")
b=ord("Z")
def capitalize1(x):
    d=ord(x[0])
    if not(a<=d<=b):
        x=chr(d-32)+x[1:]
    return x
def count1(x):
    b=0
    c=len(x)
    for i in x:
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=90 and ord(i)<=122):
            b=b+1
        elif (ord(i)>=48 and ord(i)<=58):
            b=b+1
    return b
def swapcase1(x):
    a=""
    b=""
    c=0
    d=len(x)
    for i in x:
        if (ord(i)>=65 and ord(i)<=90):
            i=chr(ord(i)+32)
            a=a+i
        elif (ord(i)>=90 and ord(i)<=122):
            i=chr(ord(i)-32)
            b=b+i
        else:
            c=c+i
    print (a,b)
def isupper1(x):
    a=0
    b=len(x)
    for i in x:
        if i>="A" and i<="Z":
            a=a+1
    if b==a:
        return True
    else:
        return False
def islower1(x):
    a=0
    b=len(x)
    for i in x:
        if ord(i)>=97 and ord(i)<=122:
            a=a+1
    if b==a:
        return True
    else:
        return False
def isalpha1(x):
    a=0
    b=len(x)
    for i in x:
        if ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122:
            a=a+1
    if b==a:
        return True
    else:
        return False
def count2(x):
    a=0
    b=len(x)
    for i in x:
        a=a+1
    return a
def isdigit(x):
    a=0
    b=len(x)
    for i in x:
        if ord(i)>=48 and ord(i)<=58:
            a=a+1
    if b==a:
        return True
    else:
        return False
def isalnum(x):
    a=0
    b=len(x)
    for i in x:
        if ord(i)>=65 and ord(i)<=122 or ord(i)>=48 and ord(i)<=58:
            a=a+1
    if b==a:
        return True
    else:
        return False





