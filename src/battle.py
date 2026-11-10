
from subclass import Warrior, Mage

class Battle:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def play_round(self):
        self.hero.attack(self.enemy)
        if enemy.is_alive() == True:
            self.enemy.attack(self.hero)
        else:
            pass
        

    def simulate_battle(self):
        while self.hero.is_alive() and self.enemy.is_alive():
            self.play_round()

        if self.enemy.is_alive() == True:
            return print(f"{self.enemy.name} won!!!")
        else:
            return print(f"{self.hero.name} won!!!")

enemy = Warrior("Jon", "tactical_flip_flop")
hero = Mage("Jonas", "potato_bomb")

battle = Battle(hero, enemy)
print(battle)