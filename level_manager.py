class LevelManager:

    __current_level = 1

    def __init__(self, max_level: int):
        self.max_level = max_level
        self._levels_instruction = self.__create_levels_instruction()
        self._level = __current_level
        self._health = None
        self._current_experience_border = None


    def __create_levels_instruction(self) -> dict:
        """
        Возвращает словарь уровней в формате: {1 : {"level": 1,         "health": health, "experience": experience}
                                               ..: {"level": ..,        "health": health, "experience": experience}
                                        max_level: {"level": max_level, "health": health, "experience": experience}
        """

        level_dict = {}

        level, health, experience_border = 1, 100, 15  # начальные данные

        for i in range(1, self.max_level + 1):

            """Количество HP округляется до последнего ноля в большую сторону"""
            while health % 10 != 0:
                health += 1

            level_dict[i] = {"level": i, "health": int(health), "experience_border": experience_border}

            """Количество опыта для перехода на следующий уровень"""
            experience_border *= 2

            """Количество HP растет на 50% от прошлого значения"""
            health += health / 2

        return level_dict

    @property
    def level(self):
        return self._levels_instruction[1]["level"]


    def next_level(self):
        ...

    def recalculate_health(self):
        ...
