class PlayerCharacter():
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        if PlayerCharacter.membership:
            print('Is membership')

    def shout(self):
        print(f'My name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

p1 = PlayerCharacter('Bob', 23)
print(p1.adding_things(2, 3))

# p1.shout()
# print(p1.name)
# print(p1.age)
# print(p1.membership)