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
class Student(People):  # дочерний класс

    def __init__(self, name, age, view):
        People.__init__(self, name, age)
        super().__init__(name, age)
        self.view = view

    def eating_fastfood(self):
        print(self.name, 'eating')

    def print(self):
        print('aaaaaaaaaaaa')


student1 = Student('beka', 20, 0)

student1.eating_fastfood()
student1.print()
people2.print()
People.print(student1)
print(Student.mro())


class Teach(Student):
    def print(self):
        super().print()
        Student.print(self)
        People.print(self)

    def __str__(self):...






beka = Teach('beka', 20, 0)

beka.print()
print(Teach.mro())

print(beka)