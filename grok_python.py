"""
Grokking Python:
https://kirbyurner.medium.com/grokking-python-9f96140c1e07?sk=d1ec6762e753d5c79106faf1669fcb04
(friend link)

Python's Rib Cage:
https://kirbyurner.medium.com/pythons-rib-cage-e4ff16cf3a74?sk=3e59d2356de6a13b42c9cf61d4d6a308
(friend link)

In this more advanced version, we study inheritance
"""

class Animal:

    def __init__(self, nm):
        "An animal is born..."
        self.name = nm
        self.stomach = [ ] # born with an empty stomach
        
    def eat(self, food):
        "Add a food to my stomach"
        self.stomach.append(food)

    def __repr__(self):
        "Repper -- represent me"
        return f"a {type(self).__name__} named {self.name}"
    
    def __add__(self, other):  
        "Combine names for the new animal of self type"
        return type(self)(self.name + other.name)

class Cat(Animal):
    """
    the Cat type
    """  
    def meow(self, n):
        return "Meow! " * n
    
class Dog(Animal):
    """
    the Dog type
    """
    def bark(self, n):
        return "Meow! " * n


if __name__ == "__main__":
    rover = Dog("Rover")
    kitty = Cat("Kitty")
    print(rover)
    print(kitty)
    rover.eat(kitty)
    print(rover.stomach)
    rover.eat(rover)
    print(rover.stomach)
