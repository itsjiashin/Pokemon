from pokemon_base import PokemonBase
from poke_team import PokeTeam
from pokemon import Charmander, Bulbasaur, Squirtle
from stack_adt import ArrayStack

class Battle:

    def set_mode_battle(self, player_one:str, player_two:str) -> int:
        t1 = PokeTeam()
        t1.choose_team(player_one, 0)
        print("")
        t2 = PokeTeam()
        t2.choose_team(player_two, 0)
        print("")
        result = self.__conduct_combat(t1, t2, 0)
        return result

    def rotating_mode_battle(self, player_one: str, player_two: str) -> int:
        t1 = PokeTeam()
        t1.choose_team(player_one, 1)
        print("")
        t2 = PokeTeam()
        t2.choose_team(player_two, 1)
        print("")
        result = self.__conduct_combat(t1, t2, 1)
        return result

    def __conduct_combat(self, team1: PokeTeam, team2: PokeTeam, battle_mode: int) -> int:
        Team1 = team1.team
        Team2 = team2.team
        while Team1.is_empty() == False and Team2.is_empty() == False:
            if battle_mode == 0:
                Team1Pokemon = Team1.pop()
                Team2Pokemon = Team2.pop()
            else:
                Team1Pokemon = Team1.serve()
                Team2Pokemon = Team2.serve()
            Team1PokemonClass = Team1Pokemon.get_poke_class()
            Team2PokemonClass = Team2Pokemon.get_poke_class()
            if Team1Pokemon.get_speed() > Team2Pokemon.get_speed():
                AttackDamage = Team1Pokemon.get_attack_damage()*Team1Pokemon.TYPE_EFFECTIVENESS[Team2PokemonClass]
                Team2Pokemon.defend(AttackDamage)
            elif Team2Pokemon.get_speed() > Team1Pokemon.get_speed():
                AttackDamage = Team2Pokemon.get_attack_damage()*Team2Pokemon.TYPE_EFFECTIVENESS[Team1PokemonClass]
                Team1Pokemon.defend(AttackDamage)
            elif Team1Pokemon.get_speed() == Team2Pokemon.get_speed():
                AttackDamagePokemon1 = Team1Pokemon.get_attack_damage()*Team1Pokemon.TYPE_EFFECTIVENESS[Team2PokemonClass]
                AttackDamagePokemon2 = Team2Pokemon.get_attack_damage()*Team2Pokemon.TYPE_EFFECTIVENESS[Team1PokemonClass]
                Team1Pokemon.defend(AttackDamagePokemon2)
                Team2Pokemon.defend(AttackDamagePokemon1)

            if Team1Pokemon.is_fainted() == False and Team2Pokemon.is_fainted() == False:
                Team1Pokemon.lose_hp(1)
                Team2Pokemon.lose_hp(1)
                if Team1Pokemon.is_fainted() == True and Team2Pokemon.is_fainted() == False:
                    Team2Pokemon.level_up()
                    if battle_mode == 0:
                        Team2.push(Team2Pokemon)
                    else:
                        Team2.append(Team2Pokemon)
                elif Team1Pokemon.is_fainted() == False and Team2Pokemon.is_fainted() == True:
                    Team1Pokemon.level_up()
                    if battle_mode == 0:
                        Team1.push(Team1Pokemon)
                    else:
                        Team1.append(Team1Pokemon)
                elif Team1Pokemon.is_fainted() == False and Team2Pokemon.is_fainted() == False:
                    if battle_mode == 0:
                        Team1.push(Team1Pokemon)
                        Team2.push(Team2Pokemon)
                    else:
                        Team1.append(Team1Pokemon)
                        Team2.append(Team2Pokemon)
            elif Team1Pokemon.is_fainted() == True and Team2Pokemon.is_fainted() == False:
                Team2Pokemon.level_up()
                if battle_mode == 0:
                    Team2.push(Team2Pokemon)
                else:
                    Team2.append(Team2Pokemon)
            elif Team1Pokemon.is_fainted() == False and Team2Pokemon.is_fainted() == True:
                Team1Pokemon.level_up()
                if battle_mode == 0:
                    Team1.push(Team1Pokemon)
                else:
                    Team1.append(Team1Pokemon)

        if Team1.is_empty() == True and Team2.is_empty() == True:
            resultOfBattle = 0
        elif Team1.is_empty() == False and Team2.is_empty() == True:
            resultOfBattle = 1
        elif Team1.is_empty() == True and Team2.is_empty() == False:
            resultOfBattle = 2

        return resultOfBattle








p1 = Battle()
#print(p1.rotating_mode_battle("James", "Charles"))
print(p1.set_mode_battle("James","Charles"))













