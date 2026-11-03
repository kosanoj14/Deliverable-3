# Here we make the warrior and mage subclasses

class warrior:
    """Represents the warrior subclass in the game"""
    def __init__(self, armour : int = 5) -> None:
        """
        Initialise the subclass
        
        Args:
            Armour (int): Reduces the damage taken (default = 5)
        """
        self._armour = armour

    @property
    def armour(self) -> int:
        """Makes the armour into a property so it is read-only"""
        return self._armour

class mage:
    """Represents the mage subclass in the game"""
    def __init__(self, max_mana : int = 30) -> None:
        """
        Initialise the subclass

        Args:
            Mana_max (int): Creates the mana resurce, which the mage uses to cast spells (default = 30)
        """
        self._mana = max_mana
        self.max_mana = max_mana