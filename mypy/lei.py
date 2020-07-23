class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
       # print("self:",self)
      #  print("zhixing")
    def get_name(self):
        print("zhengzaihuoqufenzhuangdeshuju xingming",self.name)
p = People("summer",25)
print("name:",p.name)
print("age:",p.age)
p.get_name()
p1= People("SKQ",26)
print("name:",p1.name)
print("age:",p1.age)
p1.get_name()
