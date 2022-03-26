"""Абстрактная фабрика по созданию монстров."""

from abc import ABC, abstractmethod
import random


class Enemy(ABC):
    """Абстрактный класс игрового противника."""

    @abstractmethod
    def damage(self) -> dict:
        """Метод атаки."""
        pass


class Ogre(Enemy):
    """Абстрактный класс огров."""

    def damage(self) -> dict:
        """Создаем данные монстра."""
        indicators = {
            "name": "Орк",
            "type_damage": "melee",
            "attack": random.randint(6, 8),
            "hp": random.randint(6, 10),
        }
        return indicators


class Skeleton(Enemy):
    """Абстрактный класс скелетов."""

    def damage(self) -> dict:
        """Создаем данные монстра."""
        indicators = {
            "name": "Скелет",
            "type_damage": "long_shot",
            "attack": random.randint(6, 8),
            "hp": random.randint(6, 10),
        }
        return indicators


class Goblin(Enemy):
    """Абстрактный класс гоблинов."""

    def damage(self) -> dict:
        """Создаем данные монстра."""
        indicators = {
            "name": "Гоблин",
            "type_damage": "spell_shot",
            "attack": random.randint(6, 8),
            "hp": random.randint(6, 10),
        }
        return indicators


class EnemyFactory(ABC):
    """Абстрактная фабрика игрового противника."""

    @abstractmethod
    def create_enemy(self) -> None:
        """Создание абстрактного продукта."""
        pass


class OgreFactory(EnemyFactory):
    """Конкретная фабрика игрового противника."""

    def create_enemy(self) -> Ogre:
        """Создание монстра."""
        return Ogre()


class SkeletonFactory(EnemyFactory):
    """Конкретная фабрика игрового противника."""

    def create_enemy(self) -> Skeleton:
        """Создание монстра."""
        return Skeleton()


class GoblinFactory(EnemyFactory):
    """Конкретная фабрика игрового противника."""

    def create_enemy(self) -> Goblin:
        """Создание монстра."""
        return Goblin()
