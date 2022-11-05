class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

Sam = Cat(name='Sam', gender='m',age='2')
Liza = Cat(name='Liza', gender='f',age='4')
Felix = Cat(name='Felix', gender='m',age='1')

print(type(Sam))
print(Liza)
