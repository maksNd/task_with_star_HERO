def level_dict(max_level: int = 10) -> dict:
    """Возвращает словарь с данными об уровне, здоровье и опыте
    в формате {i: {"level": i,
                   "health": присваиваемое значение здоровья при достижении текущего уровня,
                   "experience": граничное значение опыта для текущего уровня}
    """
    level_dict = {}

    level, health, experience = 1, 100, 15  # начальные данные

    for i in range(1, max_level + 1):

        """Количество HP округляется до последнего ноля в большую сторону"""
        while health % 10 != 0:
            health += 1

        level_dict[i] = {"level": i, "health": int(health), "experience": experience}

        """Количество опыта для перехода на следующий уровень"""
        experience *= 2

        """Количество HP растет на 50% от прошлого значения"""
        health += health / 2

    return level_dict


if __name__ == "__main__":
    print(level_dict())
