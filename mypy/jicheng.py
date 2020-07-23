class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def exam(self):
        print("%s Examing" %(self.name))
class MathStudent(Student):
    def exam(self):
        #Student.exam(self)
        super(MathStudent,self).exam()
        print("math's%s is examing" %(self.name))
m1 = MathStudent("SUMMER",20)
print(m1)
print(m1.name,m1.age)
m1.exam()