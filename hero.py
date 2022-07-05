from level_dict import level_dict
level_dict = level_dict()

class Hero:
    def __init__(self, name):
        self.level_dict = level_dict
        self.name = name
        self._level = 1
        self._health = 100
        self.experience = 0
        self._experience_border = 15

    def add_experience(self, experience_points):
        """добавляет опыт, при этом уровень и здоровье пересчитываются"""
        self.experience += experience_points

        while self.experience > self._experience_border:
            if self.level == len(self.level_dict):
                break
            self.__reach_next_level()
            print(f"Герой достиг уровня {self.level}\n")

        print(f"Текущий уровень героя - {self.level}\n"
              f"Текущее здоровье героя - {self.health}\n"
              f"Текущий опыт героя - {self.experience}\n")

    @property
    def level(self) -> int:
        """возвращает уровень, это целое число"""
        return self._level

    @property
    def health(self) -> int:
        """возвращает здоровье, это целое число"""
        return self._health

    def __reach_next_level(self):

        self._level += 1
        self._health += int(self._health / 2)
        self._experience_border *= 2

        while self._health % 10 != 0:
            self._health += 1
