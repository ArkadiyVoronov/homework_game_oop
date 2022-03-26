"""Главный файл с логикой и запуском игры."""

import sys

from mylib.BasicHero import Hero
from mylib.BasicEvent import GenerateEvent


monster_counter = 0


def valid_number(number: str) -> str:
    """Валидация ввода при 1 или 2."""
    while True:
        if number == "1" or number == "2":
            return number
        else:
            number = input("Введите 1 или 2")


def valid_number2(number: str) -> str:
    """Валидация ввода при 1 или 2 или 3."""
    while True:
        if number == "1" or number == "2" or number == "3":
            return number
        else:
            number = input(
                "Для выбора введите:\n"
                "\n1 - выбрать sword"
                "\n2 - выбрать bow"
                "\n3 - выбрать magic book"
            )


def battle(monster: dict, hero: Hero) -> bool:
    """Встретили монстра."""
    global monster_counter
    name, damage, attack, monster_hp = "", "", "", ""
    for key, value in monster.items():
        if key == "name":
            name = value
        elif key == "type_damage":
            damage = value
        elif key == "attack":
            attack = value
        else:
            monster_hp = value

    print(f"Приготовься, будет БОЙ!\n"
          f"Перед тобой {name}, у него сила удара:{attack} и жизней:{monster_hp}")
    input_number = input("1 - Начать бой\n2 - Убежать\n")
    if input_number == "2":
        return True
    else:
        while hero.hp > 0 and monster_hp > 0:
            weapon_attack = False
            improve_weapon = 0
            input_number = input("1 - Выбрать оружие 2 - Убежать\n")
            input_number = valid_number(input_number)
            if input_number == "2":
                return True
            else:
                while weapon_attack is False:
                    input_number_weapon = input(
                        f"\n1 - выбрать"
                        f" {hero.sword}"
                        f"\n2 - выбрать {hero.bow} "
                        f"(стрел {hero.arrow})"
                        f"\n3 - выбрать "
                        f"{hero.magic_book}"
                        f"\n"
                    )
                    input_number_weapon = valid_number2(input_number_weapon)
                    weapon_attack = hero.get_attack_weapon(input_number_weapon)
                    if weapon_attack:
                        weapon_name = hero.get_name_weapon(input_number_weapon)
                        if weapon_name == "bow" and hero.arrow == 0:
                            print(
                                f"Количество стрел = {hero.arrow}, "
                                "вам нужно поменять оружие"
                            )
                            weapon_attack = False
                            continue
                        improve_weapon = hero.improve_weapon(weapon_name)
                    else:
                        print("Такого оружия у вас нет")
                        continue
                dodge = hero.dodge_attack(damage)
                if dodge:
                    hero.minus_hp(0)
                    monster_hp = monster_hp - (weapon_attack + improve_weapon)
                else:
                    hero.minus_hp(attack)
                    monster_hp = monster_hp - (weapon_attack + improve_weapon)
                if weapon_name == "bow":
                    hero.arrow -= 1
            if hero.hp > 0:
                monster_counter += 1
                print(f"Убито монстров {monster_counter}\n")
                return True
            else:
                if hero.totem:
                    print("Вы ПРОИГРАЛИ бой")
                    input_number = input("1 - Использовать тотем 2 - умереть\n")
                    input_number = valid_number(input_number)
                    if input_number == "1":
                        hero.name = hero.totem["nickname"]
                        hero.race = hero.totem["race"]
                        hero.hp = hero.totem["hp"]
                        hero.bow = hero.totem["bow"]
                        hero.magic_book = hero.totem["magic_book"]
                        hero.sword = hero.totem["sword"]
                        hero.arrow = hero.totem["arrows"]
                        hero.totem = None
                        print("Тотем сработал\n")
                        return True
                    else:
                        return False
                else:
                    return False


def choice_race() -> str:
    """Выбирает расу."""
    print("Введите число 1, 2 или 3 для выбора расы:")
    list_race = ["Warrior", "Mage", "Hunter"]
    while True:
        try:
            race = int(input("1. Warrior\n" "2. Mage\n" "3. Hunter\n"))
        except ValueError:
            print("Нужно ввести число 1, 2 или 3 для выбора расы")
            continue
        if race in [1, 2, 3]:
            return list_race[race - 1]
        else:
            print("Нужно ввести число 1, 2 или 3 для выбора расы")


def get_item(action: dict, hero: Hero) -> bool:
    """Событие нахождения item."""
    for k, v in action.items():
        if k in ["sword", "magic_book", "bow", "arrows"]:
            print(f"Вы нашли новый {k} {v} с атакой ")
            input_number = input(f"1 - Взять {k} c атакой {v}\n" f"2 - Пройти мимо\n")
            input_number = valid_number(input_number)
            if input_number == "1":
                if action.get("sword", False):
                    hero.sword = action
                    return True
                elif action.get("bow", False):
                    hero.bow = action
                    return True
                elif action.get("magic_book", False):
                    hero.magic_book = action
                    return True
                else:
                    hero.arrow += v
                    return True
            else:
                return False
        elif k in "apple":
            print(f"Вы нашли яблочко на {v}")
            hero.use_heal(v)
            return True
        else:
            input_number = input(f"Вы нашли {k}\n1 - Взять 2 - пройти мимо\n")
            input_number = valid_number(input_number)
            if input_number == "1":
                hero.totem = {"nickname": hero.name,
                              "hp": hero.hp,
                              "bow": hero.bow,
                              "sword": hero.sword,
                              "arrows": hero.arrow,
                              "magic_book": hero.magic_book,
                              "race": hero.race
                              }
                return True
            else:
                return False


def game() -> None:
    """Происходит процесс игры."""
    hero = Hero(name="Грегор")
    race = choice_race()
    class_race = hero.get_race(race)
    print(f"Персонаж создан:\n{hero.name} - {class_race} готов к приключениям!")
    while monster_counter < 10 and hero.hp > 0:
        event = GenerateEvent()
        action = event.get_event
        if action.get("name", False):
            fight = battle(action, hero)
            if fight:
                print(hero)
            else:
                print("Вы убежали\n")
                print(hero)
        else:
            get_item(action, hero)
    print("ПОБЕДА!")
    sys.exit()


if __name__ == "__main__":
    game()
