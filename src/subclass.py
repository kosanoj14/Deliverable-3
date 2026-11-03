# Here we make the warrior and mage subclasses

class warrior():
    """Represents the warrior subclass in the game"""
    def __init__(self, armour : int = 5):
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