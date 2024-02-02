"""
Grokking Python:
https://kirbyurner.medium.com/grokking-python-9f96140c1e07?sk=d1ec6762e753d5c79106faf1669fcb04
(friend link)

Python's Rib Cage:
https://kirbyurner.medium.com/pythons-rib-cage-e4ff16cf3a74?sk=3e59d2356de6a13b42c9cf61d4d6a308
(friend link)
"""

class Dog:
    """
    the Dog type
    """

    def __init__(self, nm):
        "A dog is born..."
        self.name = nm
        self.stomach = [ ] # born with an empty stomach

    def __add__(self: Dog, other: Dog):  # type annotations!
        "Combine names for the new doggie"
        return Dog(self.name + other.name)
        
    def eat(self, food):
        "Add a food to my stomach"
        self.stomach.append(food)

    def __repr__(self):
        "Repper -- represent me"
        return f"Dog named {self.name}"