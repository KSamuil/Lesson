# ооп - обьктно ориентированное прог.
# CLASS , Method

q = 1
p = '1'
l = True
q1=1.21
q2=[],{},()
# print(type(p))

def p1(l):
    return l

print(p1(1))


class People: #родительский класс
    # свойства
    body=True
    head=1
    # все функции в классе называются методами

    # магический метод
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'age:{self.age} \n' \
               f'name is {self.name}\n'

    def __len__(self):
        return len(f'{self.name} {self.age}')

    def print(self):
        print(self.name,self.age,self.body)

people=People('beka',20)

people2=People('Ерлан',15)

# people.print()
# people2.print()

print(people2)

print(len(people2))