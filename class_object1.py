class college:
    clg_name="st.vincent pallotti college"

    def __init__(self,name,age,depname):
        self.name=name
        self.age=age
        self.depname=depname
    def display(self):
        print("student name:",self.name)
        print("student age:",self.age)
        print("student department:",self.depname)
        print("student college name:",college.clg_name)


student1=college("nishant",24,"IT")
student2=college("nitesh",25,"EE")
student1.display()
student2.display()
