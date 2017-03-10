

class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def displayHealth(self):
        print self.name
        print self.health
        return self
#
    def walk(self):
        self.health -=1
        return self

    def run(self):
        self.health -=5
        return self


newAnimal = Animal('Bob', 100)
newAnimal.walk().run().displayHealth()
#
animal = Animal('Tom')
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health +=5
        return self

dog = Dog('Barky')
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -=10
        return self

dragon = Dragon('Puff')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()

# make sure fly doesn't work for animal1
# animal1 = Animal('Tom')
# animal1.walk().walk().walk().run().run().fly().displayHealth()
