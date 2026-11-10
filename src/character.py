# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from item import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage dealt when character attacks unarmed (default = 10)
            weapon (Weapon, optional): Equipped weapon.
        """
        self.name = name
        self._hp = hp_max  # _hp indicates private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def calculate_damage(self) -> int:
        """Calculates damage output depending on whether a weapon is equipped"""
        if self.weapon is not None:
            return self.weapon.roll_damage()
        return self.damage

    def take_damage(self, damage: int) -> None:
        """Modifies the hp of the character, lowering it by the damage amount, it cant go negative"""
        self._hp -= damage
        self._hp = max(self._hp, 0)

    def heal(self, heal_amount: int) -> None:
        """Modifies the hp of the character, increasing it by the heal_amount, it cant go above hp_max"""
        self._hp += heal_amount
        self._hp = min(self._hp, self.hp_max)

    def attack(self, target: "Character") -> None:
        """Attack and deal damage to target character"""
        damage_dealt = self.calculate_damage()
        target.take_damage(damage_dealt)

    def introduce(self) -> None:
        """Prints an introduction for the character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property that checks if the character is alive (True) or dead (False)"""
        return self._hp > 0
    