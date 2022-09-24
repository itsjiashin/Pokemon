from abc import ABC, abstractmethod


class PokemonBase(ABC):

    def __init__(self, hp: int, poke_class: str):
        if hp <= 0:
            raise ValueError("HP of pokemon created must be above 0!")

        if poke_class != "GRASS" and poke_class != "WATER" and poke_class != "FIRE":
            raise TypeError("Pokemon class is invalid!")

        self.hp = hp
        self.poke_class = poke_class
        self.level = 1

    def get_hp(self) -> int:
        return self.hp

    def get_level(self) -> int:
        return self.level

    def get_poke_class(self) -> str:
        return self.poke_class

    def is_fainted(self) -> bool:
        return self.hp <= 0

    def level_up(self) -> None:
        self.level += 1

    def lose_hp(self, lost_hp:int) -> None:
        self.hp -= lost_hp

    @abstractmethod
    def get_speed(self) -> int:
        pass

    @abstractmethod
    def get_attack_damage(self) -> int:
        pass

    @abstractmethod
    def get_defence(self) -> int:
        pass

    @abstractmethod
    def defend(self, damage: int) -> None:
        pass

    @abstractmethod
    def get_poke_name(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass













