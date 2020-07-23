class People():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("self",self)
        print("正在执行构造方法init,在实例化对象时自动执行")
    def get_name(self):
        print("正在获取封装的数据, 姓名: ", self.name)
    def get_age(self):
        print("正在获取封装的数据, AGE: ", self.age)
p = People("SKQ",25)
print("p:",p)
print("名称: ", p.name)
print("年龄: ", p.age)
p.get_name()
p.get_age()
p1 = People("张三", 30)
print("名称: ", p1.name)
print("年龄: ", p1.age)