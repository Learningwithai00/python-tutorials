##Demonstrate polymorphism with a Bird class and its child Parrot class.

class Bird:
    def fly(self):
        print("Some birds can fly")

class Parrot(Bird):
    def fly(self):
        print("Parrots can fly")

# Example
bird = Bird()
bird.fly()

parrot = Parrot()
parrot.fly()
