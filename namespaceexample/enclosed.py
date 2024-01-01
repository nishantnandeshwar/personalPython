y=10                              #global
def outer():
    z=4                           #enclosed   it is neither local variable nor global variable
    print("inside of outer z:",z)
    def inner():
        x=4                       #local
        nonlocal z
        z=z+1
        print("x:",x)
        print("y:",y)
        print("inside of inner z:",z)
    print("outside of function z:",z)
    inner()
outer()

