"""Класс героя, его описание, и доступные ему методы."""

from .RaceHero import WarriorFactory, MageFactory, HunterFactory
from typing import Any


class Hero:
    """Характеристики героя."""

    def __init__(self, name: str) -> None:
        """Конструктор класса герой."""
        self.name = name
        self.race = None
        self.hp = 10
        self.bow = None
        self.arrow = 0
        self.magic_book = None
        self.sword = {"sword": 10}
        self.totem = None

    def use_heal(self, apple: int) -> int:
        """Герой пополняет здоровье яблоком."""
        self.hp += apple
        return self.hp

    def get_name_weapon(self, num: str) -> Any:
        """Метод для выбора оружия."""
        if num == "1":
            if self.sword is None:
                return False
            else:
                for k, v in self.sword.items():
                    return k
        elif num == "2":
            if self.bow is None:
                return False
            else:
                for k, v in self.bow.items():
                    return k
        else:
            if self.magic_book is None:
                return False
            else:
                for k, v in self.magic_book.items():
                    return k

    def get_attack_weapon(self, num: str) -> Any:
        """Герой выбирает доступное оружие."""
        if num == "1":
            if self.sword is None:
                return False
            else:
                return self.sword["sword"]
        elif num == "2":
            if self.bow is None:
                return False
            else:
                return self.bow["bow"]
        else:
            if self.magic_book is None:
                return False
            else:
                return self.magic_book["magic_book"]

    def minus_hp(self, attack: int) -> int:
        """Герой получает урон во время боя."""
        self.hp -= attack
        return self.hp

    def get_race(self, my_race: str) -> str:
        """Позволяет выбрать класс героя."""
        list_race = {
            "Warrior": WarriorFactory,
            "Mage": MageFactory,
            "Hunter": HunterFactory,
        }
        factory_race = list_race[my_race]()
        race = factory_race.create_race()
        self.race = race.choice_race()
        return self.race

    def dodge_attack(self, enemy: str) -> Any:
        """Способность позволяет уклониться от атак."""
        list_race = {
            "Warrior": WarriorFactory,
            "Mage": MageFactory,
            "Hunter": HunterFactory,
        }
        factory_race = list_race[self.race]()
        race = factory_race.create_race()
        return race.skill_dodge(self.race, enemy)

    def improve_weapon(self, weapon: str) -> int:
        """Способность улучшает классовое оружие."""
        list_race = {
            "Warrior": WarriorFactory,
            "Mage": MageFactory,
            "Hunter": HunterFactory,
        }
        factory_race = list_race[self.race]()
        race = factory_race.create_race()
        return race.skill_improve_weapon(self.race, weapon)

    def __str__(self):
        """Печатает актуальные данные героя."""
        return f'Герой "{self.name}"' f'\nКласс "{self.race}"' f"\n{self.hp} здоровье"
