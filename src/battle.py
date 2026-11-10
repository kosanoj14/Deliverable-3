from item import *
from subclass import *


class Battle:
    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> str:
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        if self.enemy.is_alive:
            print(f"{self.enemy.name} won!!!")
        else:
            print(f"{self.hero.name} won!!!")
        


enemy = Warrior("Jon", weapon=potato_bomb)
hero = Mage("Jonas")

battle = Battle(hero, enemy)
battle.simulate_battle()