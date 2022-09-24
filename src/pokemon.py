from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    NAME = "Charmander"
    DEFENCE = 4
    TYPE_EFFECTIVENESS = {"WATER": 0.5, "GRASS": 2, "FIRE": 1}

    def __init__(self):
        PokemonBase.__init__(self, 7, "FIRE")

    def get_speed(self) -> int:
        return 8 + self.get_level()

    def get_attack_damage(self) -> int:
        return 6 + self.get_level()

    def get_defence(self) -> int:
        return Charmander.DEFENCE

    def defend(self, damage: int) -> None:
        if self.get_hp() < 0:
            raise ValueError("HP must be above 0!")
        elif damage > self.get_defence():
            self.lose_hp(damage)
        else:
            self.lose_hp(damage//2)

    def get_poke_name(self) -> str:
        return Charmander.NAME

    def __str__(self) -> str:
        return "{}'s health = {} and level = {}".format(self.get_poke_name(), self.get_hp(), self.get_level())


class Bulbasaur(PokemonBase):
    NAME = "Bulbasaur"
    ATTACK = 5
    DEFENCE = 5
    TYPE_EFFECTIVENESS = {"WATER": 2, "GRASS": 1, "FIRE": 0.5}

    def __init__(self):
        PokemonBase.__init__(self, 9, "GRASS")

    def get_speed(self) -> int:
        return 7 + (self.get_level()//2)

    def get_attack_damage(self) -> int:
        return Bulbasaur.ATTACK

    def get_defence(self) -> int:
        return Bulbasaur.DEFENCE

    def defend(self, damage: int) -> None:
        if self.get_hp() < 0:
            raise ValueError("HP must be above 0!")
        elif damage > (self.get_defence()+5):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage//2)

    def get_poke_name(self) -> str:
        return Bulbasaur.NAME

    def __str__(self) -> str:
        return "{}'s health = {} and level = {}".format(self.get_poke_name(), self.get_hp(), self.get_level())


class Squirtle(PokemonBase):
    NAME = "Squirtle"
    SPEED = 7
    TYPE_EFFECTIVENESS = {"WATER": 1, "GRASS": 0.5, "FIRE": 2}

    def __init__(self):
        PokemonBase.__init__(self, 8, "WATER")

    def get_speed(self) -> int:
        return Squirtle.SPEED

    def get_attack_damage(self) -> int:
        return 4 + (self.get_level()//2)

    def get_defence(self) -> int:
        return 6 + (self.get_level())

    def defend(self, damage: int) -> None:
        if self.get_hp() < 0:
            raise ValueError("HP must be above 0!")
        elif damage > (self.get_defence()*2):
            self.lose_hp(damage)
        else:
            self.lose_hp(damage//2)

    def get_poke_name(self) -> str:
        return Squirtle.NAME

    def __str__(self) -> str:
        return "{}'s health = {} and level = {}".format(self.get_poke_name(), self.get_hp(), self.get_level())






