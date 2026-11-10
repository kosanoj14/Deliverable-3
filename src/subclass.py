# Here we make the warrior and mage subclasses

# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from character import Character
from item import Weapon


class Warrior(Character):
    """Represents the warrior subclass in the game"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None, armour: int = 5) -> None:
        """Initialise the warrior with superclass attributes + armour"""
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self._armour = armour

    def take_damage(self, damage: int) -> None:
        """Reduces incoming damage by armour value before applying it"""
        effective_damage = max(damage - self.armour, 0)
        super().take_damage(effective_damage)
    
    def __repr__(self) -> str:
        """Returns class info formatted"""
        return f"Subclass: Warrior. {super().__repr__()}"

    @property
    def armour(self) -> int:
        """Makes armour read-only"""
        return self._armour


class Mage(Character):
    """Represents the mage subclass in the game"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None, max_mana: int = 30) -> None:
        """Initialise the mage with superclass attributes + mana"""
        super().__init__(name=name, hp_max=hp_max, damage=damage, weapon=weapon)
        self._mana = max_mana
        self.max_mana = max_mana

    def attack(self, target: Character) -> None:
        """Attacks target and deals double damage if mage has more than 10 mana"""
        base_damage = self.calculate_damage()
        
        if self._mana >= 10:
            self._mana -= 10
            target.take_damage(base_damage * 2)
        else:
            self._mana = min(self._mana + 5, self.max_mana)
            target.take_damage(base_damage)

    def __repr__(self) -> str:
        """Returns class info formatted"""
        return f"Subclass: Mage. {super().__repr__()}"

    @property
    def mana(self) -> int:
        """Makes current mana read-only"""
        return self._mana