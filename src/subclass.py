# Here we make the warrior and mage subclasses

# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from character import Character


class warrior(Character):
    """Represents the warrior subclass in the game"""
    def __init__(self, armour : int = 5) -> None:
        """
        Initialise the subclass
        
        Args:
            Armour (int): Reduces the damage taken (default = 5)
        """
        self._armour = armour

    def take_damage(self, damage) -> None:
        """Makes the character take damage and accounts for armour"""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage
        
        self._hp -= damage - self.armour
        self._hp = max(self._hp, 0)

    def class_text(self) -> str:
        """Writes the class info"""
        sc_txt = "Subclass: Warrior. "
        Class_txt = super().__str__()
        return sc_txt + Class_txt
 
    @property
    def armour(self) -> int:
        """Makes the armour into a property so it is read-only"""
        return self._armour

class mage(Character):
    """Represents the mage subclass in the game"""
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, max_mana : int = 30) -> None:
        """
        Initialise the subclass

        Args:
            Mana_max (int): Creates the mana resurce, which the mage uses to cast spells (default = 30)
        """
        super().__init__(name=name, hp_max=hp_max, damage=damage)
        self._mana = max_mana
        self.max_mana = max_mana

    def attack(self, target) -> None:
        """Attacks the target and does double damage if the mage har more than 10 mana"""
        if self._mana > 10:
            self._mana -= 10
            target.take_damage(self.damage * 2)
        else:
            target.take_damage(self.damage)
            self._mana += 5

    def class_text(self) -> str:
            """Writes the class info"""
            sc_txt = "Subclass: Mage. "
            Class_txt = super().__str__()
            return sc_txt + Class_txt





