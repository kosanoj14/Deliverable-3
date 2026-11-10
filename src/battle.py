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

        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"{winner.name} won the battle!!!")
        return winner.name