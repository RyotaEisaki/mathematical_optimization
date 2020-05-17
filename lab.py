l=100
a=0
b=0

# l_=32.3
# a_=79.2
# b_=-107.9

l_=31.0
a_=51.1
b_=-83.1

if l>l_:
    L=(l-l_)/5
    L1=l-L
    L2=l-L*2
    L3=l-L*3
    L4=l-L*4
    L5=l-L*5
else:
    L=(l_-l)/5
    L1=l+L
    L2=l+L*2
    L3=l+L*3
    L4=l+L*4
    L5=l+L*5
print("L")
print("value:", L)
print(L1)
print(L2)
print(L3)
print(L4)
print(L5)

if a>a_:
    A=(a-a_)/5
    A1=a-A
    A2=a-A*2
    A3=a-A*3
    A4=a-A*4
    A5=a-A*5
else:
    A=(a_-a)/5
    A1=a+A
    A2=a+A*2
    A3=a+A*3
    A4=a+A*4
    A5=a+A*5
print("A")
print("value:", A)
print(A1)
print(A2)
print(A3)
print(A4)
print(A5)

if b>b_:
    B=(b-b_)/5
    B1=b-B
    B2=b-B*2
    B3=b-B*3
    B4=b-B*4
    B5=b-B*5
else:
    B=(b_-b)/5
    B1=b+B
    B2=b+B*2
    B3=b+B*3
    B4=b+B*4
    B5=b+B*5
print("B")
print("value:", B)
print(B1)
print(B2)
print(B3)
print(B4)
print(B5)