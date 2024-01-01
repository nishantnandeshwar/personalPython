y=10
def inner():
    x=4
    global y
    y=y+1
    print("print x:",x)
    print("y=",y)

print("print y:",y)
inner()
