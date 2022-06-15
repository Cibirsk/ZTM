class Cat():
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

kit = Cat('Kit', 3)
got = Cat('Got', 4)
katy = Cat('Katy', 5)


def oldest_cat(*args):
    return max(args)
       

print(f'The oldest cat is {oldest_cat(kit.age, got.age, katy.age)} ')