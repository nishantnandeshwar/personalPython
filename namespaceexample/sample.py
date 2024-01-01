def outer():
    msg="hi Nishant"
    def inner():
        print("print msg:",msg)
        x=21
        return x
    return inner  
a=outer()
print("a:",a()) 
#print("a.__name__:",a.__name__)  

#print("a():",a())  
