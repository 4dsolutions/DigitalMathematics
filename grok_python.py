"""
Grokking Python:
https://kirbyurner.medium.com/grokking-python-9f96140c1e07?sk=d1ec6762e753d5c79106faf1669fcb04
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

    def eat(self, food):
        "Add a food to my stomach"
        self.stomach.append(food)

    def __repr__(self):
        "Repper -- represent me"
        return f"Dog named {self.name}"