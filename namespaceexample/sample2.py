def outer():
    x=3
    def inner():
        y=4
        nonlocal x
        x=x+1
        result=x+y
        print("print result:",result)
        print("print x:",x)
    return inner()
outer()
