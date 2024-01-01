def outer():
    x=3
    def inner():
        y=4
        result=x+y
        print("print x:",x)
        return result
    return inner   #this is not returning function { () is not there.}
a=outer()
#print("a:",a) #print the referance ex <function outer.<locals>.inner at 0x0000028B781D3940>
#print("a.__name__:",a.__name__)   #it will print inner

print("a():",a())   #-----  this access directly inner() function
# we cannot call inner() function.

#This technique is called as closure
"""output:
a: <function outer.<locals>.inner at 0x000001C730073940>
a.__name__: inner
print x: 3
a(): 7

"""
