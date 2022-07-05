from level_dict import level_dict
level_dict = level_dict()

class Hero:
    def __init__(self, name):
        self.level_dict = level_dict
        self.name = name
        self._health = level_dict[1]["health"]
        self.experience = 0
        self._level = level_dict[1]["level"]

    def add_experience(self, experience_points):
        """добавляет опыт, при этом уровень и здоровье пересчитываются"""
        self.experience += experience_points

        while self.experience > self.level_dict[self.level]["experience"] - 1:
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
        self._health = self.level_dict[self.level]["health"]
