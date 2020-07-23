class Dog:
    '''
        表示狗的类
    '''

    def __init__(self, name, age):
        self.hidden_name = name
        self.hidden_age = age

    def say_hello(self):
        print('大家好，我是 %s' % self.hidden_name)

    def get_name(self):
        '''
            get_name()用来获取对象的name属性
        '''
       #print('用户读取了属性')
        return self.hidden_name

    def set_name(self, name):
        print('用户修改了属性')
        self.hidden_name = name

    def get_age(self):
        return self.hidden_age

    def set_age(self, age):
        if age > 0:
            self.hidden_age = age


d = Dog('旺财', 8)

#d.say_hello()

# 调用setter来修改name属性
d.set_name('小黑')
d.set_age(-10)

#.say_hello()
#print(d.get_age())
