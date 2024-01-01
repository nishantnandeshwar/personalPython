class college:
    clg_name="SVPCET"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("college:",college.clg_name)
        
        
class student(college):  #inherits from college
    def depart(self,depname):
        self.depname=depname
        print("department name:",self.depname)
        print("********************************")

s1=student("nishant",24)
s2=student("nitesh",25)
s3=student("pankaj",23)
s1.display()
s1.depart("IT")
s2.display()
s2.depart("EE")
s3.display()
s3.depart("IT")

