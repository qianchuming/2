class Students:
    #类的初始化
    def __init__(self, name, xuehao, phone):
        self.name = name
        self.xuehao = xuehao
        self.phone = phone
    #类的一种方法
    def print_phone(self):
        print("{name}的电话号码是{phone}".format(name=self.name, phone=self.phone))
#类的实例化，从抽象到个例
s1 = Students('lisi','02','5879666')
s2 = Students('wangwu','03','898989')
#类的方法调用
s1.print_phone()
s2.print_phone()
#类的属性访问
s2.name