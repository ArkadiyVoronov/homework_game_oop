"""Создание монстров и вещей."""

import random
from .Monsters import OgreFactory, SkeletonFactory, GoblinFactory
from .Items import (
    ArrowsFactory,
    SwordFactory,
    BowFactory,
    MagicBookFactory,
    TotemFactory,
    AppleFactory,
)


class GenerateEvent:
    """Класс для генерации событий."""

    @property
    def get_event(self) -> dict:
        """Вызывает фабричные методы монстров и вещей."""
        spawner_to_factory_mapping = {
            "ogre": OgreFactory,
            "skeleton": SkeletonFactory,
            "goblin": GoblinFactory,
            "apple": AppleFactory,
            "sword": SwordFactory,
            "bow": BowFactory,
            "arrows": ArrowsFactory,
            "magic_book": MagicBookFactory,
            "totem": TotemFactory,
        }

        event_type_list = [
            "arrows",
            "goblin",
            "bow",
            "ogre",
            "skeleton",
            "sword",
            "apple",
            "magic_book",
            "totem",
        ]

        spawner_type = random.choice(event_type_list)
        spawner = spawner_to_factory_mapping[spawner_type]()
        if (
            isinstance(spawner, OgreFactory)
            or isinstance(spawner, GoblinFactory)
            or isinstance(spawner, SkeletonFactory)
        ):
            event = spawner.create_enemy()
            return event.damage()

        else:
            event = spawner.create_item()
            return event.item()
