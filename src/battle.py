from item import *
from subclass import *


class Battle:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def play_round(self):
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulate_battle(self):
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()

        if self.enemy.is_alive:
            print(f"{self.enemy.name} won!!!")
            return self.enemy.name

        print(f"{self.hero.name} won!!!")
        return self.hero.name


enemy = Warrior("Jon", weapon=potato_bomb)
hero = Mage("Jonas", weapon=potato_bomb)

battle = Battle(hero, enemy)
battle.simulate_battle()