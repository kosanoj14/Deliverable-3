import random


class Dice:
    """Bulding av dice generator, that randomly roll av dice."""


    def __init__(self, sides: int = 6) -> None:
        """The default is 6 sides for det dice, but the player can choose.
        It must be at least 2"""
        if sides < 2:
            raise ValueError("A dice must hav at least 2 sides")
        self.sides = sides


    def roll(self):
        """Roll the dice and return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)


    def __repr__(self):
        """Representation of the dice"""
        return f"Dice(sides={self.sides})"
    

    def __call__(self):
        """Allow the dice to be calles like a function."""
        return self.roll()
