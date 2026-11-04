from dice import Dice


class Weapon:
    """Make different weapons character can use."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Choose a weapon with name and damage dice"""
        self.name = name
        self.damage_dice = damage_dice
        

    def roll_damage(self):
        """Roll the damage dice and return the damage value."""
        return self.damage_dice.roll()



# Weapons
sword = Weapon("Sword", Dice(8))
carrot_arrow = Weapon("Carrot Arrow", Dice(6))
husky_hammer = Weapon("Husky Hammer", Dice(12))
stabber_knife = Weapon("Stabber Knife", Dice(4))
potato_bomb = Weapon("Potato Bomb", Dice(20))
frozen_salmon = Weapon("Frozen Salmon", Dice(6))
tactical_flip_flop = Weapon("Tactical Flip-Flop", Dice(4))
nokia_ultra = Weapon("Nokia Ultra", Dice(20))

