from pokemon import Charmander, Bulbasaur, Squirtle
from stack_adt import ArrayStack
from queue_adt import CircularQueue


class PokeTeam:

    def __init__(self):
        self.name = None
        self.team = None
        self.battle_mode = None
        self.limit = 6

    def __correct_team_given(self, charmanders: int, bulbasaurs: int, squirtles: int) -> bool:
        if charmanders < 0 or bulbasaurs < 0 or squirtles < 0:
            return False
        else:
            return (charmanders + bulbasaurs + squirtles) <= self.limit

    def __inputs_are_integers(self, c, b, s) -> bool:
        if c.isdigit() and b.isdigit() and s.isdigit():
            return True
        else:
            return False


    def __assign_team(self, name: str, charmanders: int, bulbasaurs: int, squirtles: int) -> None:
        self.name = name
        i = 0
        j = 0
        k = 0
        if self.battle_mode == 0:
            self.team = ArrayStack(charmanders + bulbasaurs + squirtles)
            while i < squirtles:
                self.team.push(Squirtle())
                i += 1
            while j < bulbasaurs:
                self.team.push(Bulbasaur())
                j += 1
            while k < charmanders:
                self.team.push(Charmander())
                k += 1
        elif self.battle_mode == 1:
            self.team = CircularQueue(charmanders + bulbasaurs + squirtles)
            while k < charmanders:
                self.team.append(Charmander())
                k+=1
            while j < bulbasaurs:
                self.team.append(Bulbasaur())
                j+=1
            while i < squirtles:
                self.team.append(Squirtle())
                i+=1



    def choose_team(self, name: str, battle_mode: int) -> None:
        if battle_mode != 0 and battle_mode != 1:
            raise ValueError("Input for battle_mode can only be 0 or 1!")
        else:
            self.battle_mode = battle_mode
        print("Trainer " + name + "! Choose your team as C B S\nwhere C is the number of Charmanders\n B is the number of Bulbasaurs\n S is the number of Squirtles")
        try:
            c, b, s = input("->").split()
        except ValueError:
            print("Value is incorrect, please try again")
            c, b, s = input("->").split()
        else:
            while self.__inputs_are_integers(c, b, s) == False or self.__correct_team_given(int(c), int(b), int(s)) == False:
                print("Value is incorrect, please try again")
                c, b, s = input("->").split()
            print("Team Assigned: " + name)
            self.__assign_team(name, int(c), int(b), int(s))




    def __str__(self):
        return str(self.team)

#p1 = PokeTeam()
#p1.choose_team("James", 0)
#print(p1.team.array[0])
#print(p1.team.array[1])
#print(p1.team.array[2])
#print(p1.team.serve())
#print(p1)

p1 = PokeTeam()
p1.choose_team("James", 0)
print(p1)

#p1 = CircularQueue(6)
#p1.array[0] = "Hello"
#p1.array[5] = "World"
#p1.front = 5
#p1.rear = 1
#print(p1)




