from raw_generator import GenerateHumanoid
from random import randint


class GenerateHumanoidRace(GenerateHumanoid):

    def __init__(self, race="human", gender="male"):
        super().__init__()
        gender_dict = {"male": True, "man": True, "boy": True, "female": False, "woman": False, "girl": False}
        self.race = race
        self.gender = gender_dict[gender]
        human_male_name = ["Adelbert", "Albrecht", "Berthold", "Bruno", "Dieter", "Ditrich", "Eckhardt", "Felix",
                           "Gottfried", "Gotfryd", "Gustav", "Hans", "Heinz", "Johan", "Konrad", "Leopold", "Magnus",
                           "Otto", "Otton", "Pieter", "Rudiger", "Siegfried", "Tytus", "Ulrich", "Waldemar", "Wolfgang"]
        human_female_name = ["Alexa", "Alfrida", "Beatrix", "Bianka", "Carlott", "Elfrida", "Elise", "Gabrielle",
                             "Gretchen", "Hanna", "Ilsa", "Klara", "Jarla", "Ludmilla", "Mathilde", "Regina",
                             "Solveig", "Theodora", "Urlike", "Wertha"]
        elf_male_name = ["Aluthol", "Amendil", "Angram", "Cavindel", "Dolwen", "Eldillor", "Falandar", "Farnoth",
                         "Gildiril", "Harrond", "Imhol", "Larandar", "Laurenor", "Mellion", "Mormacar", "Ravandil",
                         "Torendil", "Urdithane", "Valahuir", "Yavandir"]
        elf_female_name = ["Alane", "Altronia", "Davandrel", "Eldril", "Eponia", "Fanriel", "Filamir", "Gallina",
                           "Halion", "Iludil", "Ionor", "Lindara", "Lorandra", "Maruviel", "Pelgrana", "Siluvaine",
                           "Tallana", "Ulliana", "Vivandrel", "Yuviel"]
        dwarf_male_name = ["Bardin", "Brokk", "Dimzad", "Durak", "Garil", "Gottri", "Grundi", "Hargin", "Imrak",
                           "Kargun", "Jotunn", "Magnar", "Mordrin", "Nargond", "Orzad", "Ragnar", "Snorri",
                           "Storri", "Thingrim", "Urgrim"]
        dwarf_female_name = ["Anika", "Asta", "Astrid", "Berta", "Birgit", "Dagmar", "Elsa", "Erika", "Franziska",
                             "Greta", "Hunni", "Ingrid", "Janna", "Karin", "Petra", "Sigrid", "Sigrun", "Silma",
                             "Thylda", "Ulla"]
        halfling_male_name = ["Adam", "Albert", "Alfred", "Axel", "Carl", "Edgar", "Hugo", "Jakob", "Ludo", "Max",
                              "Niklaus", "Oskar", "Paul", "Ralf", "Rudi", "Theo", "Thomas", "Udo", "Viktor", "Walter"]
        halfling_female_name = ["Agnes", "Alice", "Elena", "Eva", "Frida", "Greta", "Hanna", "Heidi", "Hilda", "Janna",
                                "Karin", "Leni", "Marie", "Petra", "Silma", "Sophia", "Susi", "Theda", "Ulla", "Wanda"]

        self.weapon = ["1H-weapon"]
        if self.race == "human":
            if gender:
                self.name = human_male_name[randint(0, len(human_male_name) - 1)]
            elif gender is False:
                self.name = human_female_name[randint(0, len(human_female_name) - 1)]
            else:
                print("Incorrect gender has been chosen!")
            self.__human()
        elif self.race == "elf":
            if gender:
                self.name = elf_male_name[randint(0, len(elf_male_name) - 1)]
            elif gender is False:
                self.name = elf_female_name[randint(0, len(elf_female_name) - 1)]
            else:
                print("Incorrect gender has been chosen!")
            self.__elf()
        elif self.race == "dwarf":
            if gender:
                self.name = dwarf_male_name[randint(0, len(dwarf_male_name) - 1)]
            elif gender is False:
                self.name = dwarf_female_name[randint(0, len(dwarf_female_name) - 1)]
            else:
                print("Incorrect gender has been chosen!")
            self.__dwarf()
        elif self.race == "halfling":
            if gender:
                self.name = halfling_male_name[randint(0, len(halfling_male_name) - 1)]
            elif gender is False:
                self.name = halfling_female_name[randint(0, len(halfling_female_name) - 1)]
            else:
                print("Incorrect gender has been chosen!")
            self.__halfling()
        else:
            print("Generation Fail")

    def __start_wounds(self):
        vitality_roll = randint(1, 10)
        if self.race == "human":
            start_wounds = {1: 10, 2: 10, 3: 10, 4: 11, 5: 11, 6: 11, 7: 12, 8: 12, 9: 12, 10: 13}
            return start_wounds[vitality_roll]
        elif self.race == "elf":
            start_wounds = {1: 9, 2: 9, 3: 9, 4: 10, 5: 10, 6: 10, 7: 11, 8: 11, 9: 11, 10: 12}
            return start_wounds[vitality_roll]
        elif self.race == "dwarf":
            start_wounds = {1: 11, 2: 11, 3: 11, 4: 12, 5: 12, 6: 12, 7: 13, 8: 13, 9: 13, 10: 14}
            return start_wounds[vitality_roll]
        elif self.race == "halfling":
            start_wounds = {1: 8, 2: 8, 3: 8, 4: 9, 5: 9, 6: 9, 7: 10, 8: 10, 9: 10, 10: 11}
            return start_wounds[vitality_roll]

    def __start_movment(self):
        if self.race == "human":
            return 4
        elif self.race == "elf":
            return 5
        elif self.race == "dwarf":
            return 3
        elif self.race == "halfling":
            return 4

    def __human(self):
        self.weapon_skills = 20 + randint(2, 20)
        self.ballistic_skills = 20 + randint(2, 20)
        self.strength = 20 + randint(2, 20)
        self.toughness = 20 + randint(2, 20)
        self.agility = 20 + randint(2, 20)
        self.intelligence = 20 + randint(2, 20)
        self.will_power = 20 + randint(2, 20)
        self.fellowship = 20 + randint(2, 20)
        self.attacks = 1
        self.wounds = self.__start_wounds()
        self._strength_bonus()
        self._toughness_bonus()
        self.movement = self.__start_movment()
        self.armor()

    def __elf(self):
        self.weapon_skills = 20 + randint(2, 20)
        self.ballistic_skills = 30 + randint(2, 20)
        self.strength = 20 + randint(2, 20)
        self.toughness = 20 + randint(2, 20)
        self.agility = 30 + randint(2, 20)
        self.intelligence = 20 + randint(2, 20)
        self.will_power = 20 + randint(2, 20)
        self.fellowship = 20 + randint(2, 20)
        self.attacks = 1
        self.wounds = self.__start_wounds()
        self._strength_bonus()
        self._toughness_bonus()
        self.movement = self.__start_movment()
        self.armor()

    def __dwarf(self):
        self.weapon_skills = 30 + randint(2, 20)
        self.ballistic_skills = 20 + randint(2, 20)
        self.strength = 20 + randint(2, 20)
        self.toughness = 30 + randint(2, 20)
        self.agility = 10 + randint(2, 20)
        self.intelligence = 20 + randint(2, 20)
        self.will_power = 20 + randint(2, 20)
        self.fellowship = 10 + randint(2, 20)
        self.attacks = 1
        self.wounds = self.__start_wounds()
        self._strength_bonus()
        self._toughness_bonus()
        self.movement = self.__start_movment()
        self.armor()

    def __halfling(self):
        self.weapon_skills = 10 + randint(2, 20)
        self.ballistic_skills = 30 + randint(2, 20)
        self.strength = 10 + randint(2, 20)
        self.toughness = 10 + randint(2, 20)
        self.agility = 30 + randint(2, 20)
        self.intelligence = 20 + randint(2, 20)
        self.will_power = 20 + randint(2, 20)
        self.fellowship = 30 + randint(2, 20)
        self.attacks = 1
        self.wounds = self.__start_wounds()
        self._strength_bonus()
        self._toughness_bonus()
        self.movement = self.__start_movment()
        self.armor()

    def __str__(self):
        presentation = f"Name: {self.name}  Type: {self.race}    Weapons: {self.weapon}\n"\
            f"=========================================   Armor head: {self.head}          Total head resist: {self.toughness_bonus+self.head}\n" \
                       f"| WS | BS |  S |  T | Ag | Int| WP | Fel|   Armor right hand: {self.right_hand}    Total right hand resist: {self.toughness_bonus+self.right_hand}\n"\
            f"| {self.weapon_skills} | {self.ballistic_skills} | {self.strength} | {self.toughness} | {self.agility} " \
            f"| {self.intelligence} | {self.will_power} | {self.fellowship} |   Armor left hand: {self.left_hand}     Total left hand resist: {self.toughness_bonus+self.left_hand}\n" \
            f"=========================================   Armor corpse: {self.corpse}        Total corpse resist: {self.toughness_bonus+self.corpse}\n"\
            f"|  A |  W | SB | TB |  M | Mag| IP | FP |   Armor right leg: {self.right_leg}     Total right leg resist: {self.toughness_bonus+self.right_leg}\n"\
            f"|  {self.attacks} | {self.wounds} |  {self.strength_bonus} |  {self.toughness_bonus} |  {self.movement} |"\
            f"  {self.magic} |  {self.insane_points} |  {self.fate_point} |   Armor left leg: {self.left_leg}      Total left leg resist: {self.toughness_bonus+self.left_leg}\n"\
            f"=========================================   Hit points: {self.wounds} |   |   |   |   |   |   |   |   |\n"
        return presentation


x = GenerateHumanoidRace("human", "man")
print(x)
x = GenerateHumanoidRace("elf", "man")
print(x)
x = GenerateHumanoidRace("dwarf", "man")
print(x)
x = GenerateHumanoidRace("halfling", "man")
print(x)