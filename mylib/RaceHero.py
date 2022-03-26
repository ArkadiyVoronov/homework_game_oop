"""Абстрактная фабрика по созданию классов героя."""

from abc import ABC, abstractmethod
import random
from typing import Any


class ObjectRace(ABC):
    """Абстрактная раса."""

    @abstractmethod
    def skill_dodge(self, race: str, enemy: str) -> None:
        """Уклонение от атак."""
        pass

    @abstractmethod
    def choice_race(self) -> None:
        """Выбор расы."""
        pass

    @abstractmethod
    def skill_improve_weapon(self, race: str, weapon: str) -> None:
        """Классовые оружия."""
        pass


class Warrior(ObjectRace):
    """Абстрактный класс Warrior."""

    def skill_dodge(self, race: str, enemy: str) -> Any:
        """Абстрактный метод уклонения от атак."""
        skill = [True, False]
        if enemy == "melee":
            dodge = random.choice(skill)
            return dodge
        else:
            return False

    def choice_race(self) -> str:
        """Абстрактный метод выбора расы."""
        return "Warrior"

    def skill_improve_weapon(self, race: str, weapon: str) -> int:
        """Абстрактный метод классового оружия."""
        attack = 0
        if race == f"{self.choice_race()}" and weapon == "sword":
            attack += 5
            return attack
        else:
            return 0


class Mage(ObjectRace):
    """Абстрактный класс Mage."""

    def skill_dodge(self, race: str, enemy: str) -> Any:
        """Абстрактный метод уклонения от атак."""
        skill = [True, False]
        if enemy == "spell_shot":
            dodge = random.choice(skill)
            return dodge
        else:
            return False

    def choice_race(self) -> str:
        """Абстрактный метод выбора расы."""
        return "Mage"

    def skill_improve_weapon(self, race: str, weapon: str) -> int:
        """Абстрактный метод классового оружия."""
        attack = 0
        if race == f"{self.choice_race()}" and weapon == "magic_book":
            attack += 5
            return attack
        else:
            return 0


class Hunter(ObjectRace):
    """Абстрактный класс Hunter."""

    def skill_dodge(self, race: str, enemy: str) -> Any:
        """Абстрактный метод уклонения от атак."""
        skill = [True, False]
        if enemy == "long_shot":
            dodge = random.choice(skill)
            return dodge
        else:
            return False

    def choice_race(self) -> str:
        """Абстрактный метод выбора расы."""
        return "Hunter"

    def skill_improve_weapon(self, race: str, weapon: str) -> int:
        """Абстрактный метод классового оружия."""
        attack = 0
        if race == f"{self.choice_race()}" and weapon == "bow":
            attack += 5
            return attack
        else:
            return 0


class RaceFactory(ABC):
    """Фабрика по созданию абстрактного класса."""

    @abstractmethod
    def create_race(self) -> None:
        """Абстрактный метод создания класса."""
        pass


class WarriorFactory(RaceFactory):
    """Конкретная фабрика класса Warrior."""

    def create_race(self) -> Warrior:
        """Метод создания класса."""
        return Warrior()


class MageFactory(RaceFactory):
    """Конкретная фабрика класса Mage."""

    def create_race(self) -> Mage:
        """Метод создания класса."""
        return Mage()


class HunterFactory(RaceFactory):
    """Конкретная фабрика класса Hunter."""

    def create_race(self) -> Hunter:
        """Метод создания класса."""
        return Hunter()
