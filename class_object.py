class person:
    #All classes have a function called __init__(),...
    #..which is always executed when the class is being initiated....
    #necessary to do when the object is being created.

    #The __init__() function is called automatically every time..
    #...the class is being used to create a new object.

    #The self parameter is a reference to the current instance of the class,..
    #...and is used to access variables that belong to the class.
    def __init__(self,name,age):   #initialize method
        self.name=name    #self.name instance variable
        self.age=age    # self.age instance variable
    def student1(age):
        print(self.age)
    def student2(name):
        print(self.name)

p=person(24,"nishant")
print(p.name)
print(p.age)

