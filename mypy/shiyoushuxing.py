class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def get_age(self):
        print("AGE IS %s" %(self.__age))
    def __get_info(self):
        print(self.name,self.age)
s = Student("SKQ",18)
#print(s.__age)
#s.get_age()
s.__get_info()