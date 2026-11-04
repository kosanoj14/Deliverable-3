# Here we make the warrior and mage subclasses

# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage

    def take_damage(self, damage) -> None:
        """Modifies the hp of the character, lowering it by the damage amount, it cant go negative"""
        self._hp -= damage
        self._hp = max(self._hp, 0)

    def heal(self, heal_amount) -> None:
        """Modifies the hp of the character, increasing it by the heal_amount, it cant go above the max_hp"""
        self._hp += heal_amount
        self._hp = min(self._hp, self.hp_max)

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """read-only property that checks if the character is alive(True) or dead(False)"""
        return self._hp > 0


class warrior(Character):
    """Represents the warrior subclass in the game"""
    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, armour : int = 5) -> None:
        """
        Initialise the subclass
        
        Args:
            Armour (int): Reduces the damage taken (default = 5)
        """
        super().__init__(name=name, hp_max=hp_max, damage=damage)
        self._armour = armour

    def take_damage(self, damage) -> None:
        """Makes the character take damage and accounts for armour"""
        self._hp -= max(damage - self._armour, 0)
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





