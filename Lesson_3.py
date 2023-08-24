# инкапсуляция
# 1 капсула
# 2 уровни защиты
# 3 публичный,приватный,скрытый

# сделать все атрибуты скрытыми
# изучить что такое декаратор property
# и применить его на все атрибуты


class Bank:
    def __init__(self, name, age, money, password):
        self.__name = name
        self.__age = age
        self.__money = money
        self.__passw = password

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def money(self):
        return self.__money

    @property
    def password(self):
        return self.__passw

    def pname(self):
        print(self.name, self.money)

    def __ppas(self):
        print(self.password)


beka = Bank('бека', 20, 0, '12345678987543')

beka.pname()
print(beka.age)
print(beka.password)

