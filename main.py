from level_dict import level_dict
from hero import Hero
level_dict = level_dict()


if __name__ ==  "__main__":
    try:
        hero = Hero(input("Введите имя нового героя:\n"))
        print(f"У нас новый герой - {hero.name}")

        while True:
            try:
                input_data = input()
                if input_data.lower() in ("stop", "стоп"):
                    quit("Игра окончена")
                if input_data.isalnum():
                    hero.add_experience(int(input_data))
            except ValueError:
                print()
                continue

    except KeyboardInterrupt:
        quit("Игра завершена")
