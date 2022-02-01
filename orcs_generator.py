from raw_generator import GenerateHumanoid
from random import randint


class GenerateOrc(GenerateHumanoid):

    def __init__(self, orc_kind="orc"):
        super().__init__()
        self.orc_kind = orc_kind
        orcs_name = ["Wraog", "Xarpug", "Gorgo", "Piggu", "Frug", "Dugorim", "Fudhagh", "Durzol", "Gorlag", "Ohulhug",
                     "Orgug", "Woggha" "Umurn", "Braugh", "Jughragh", "Mug", "Nogugh", "Xurl", "Torgan", "Ghamborz",
                     "Mazhug", "Surgha", "Ushamph", "Olmthu", "Umruigig", "Sarfu", "Routhu", "Sogorim", "Oomigig",
                     "Cubub"]
        self.name = orcs_name[randint(0, len(orcs_name)-1)]
        self.weapon = ["chopper"]
        if orc_kind == "orc":
            self.orc()
        elif orc_kind == "black":
            self.black_orc()
        elif orc_kind == "wild":
            self.wild_orc()
        else:
            print("Generation Fail")

    def orc(self):
        self.weapon_skills = 35
        self.ballistic_skills = 35
        self.strength = 35
        self.toughness = 45
        self.agility = 25
        self.intelligence = 25
        self.will_power = 30
        self.fellowship = 20
        self.attacks = 1
        self.wounds = 12
        self._strength_bonus()
        self._toughness_bonus()
        self.movement = 4

        self.armor()
        self.head += 1
        self.left_hand += 1
        self.right_hand += 1
        self.corpse += 3
        self.left_leg += 0
        self.right_leg += 0

        self.weapon.append("wooden shield")
        alternative_weapon = ["dagger", "bow"]
        self.weapon.append(alternative_weapon[randint(0, len(alternative_weapon) - 1)])

    def black_orc(self):
        self.weapon_skills = 42
        self.ballistic_skills = 30
        self.strength = 44
        self.toughness = 45
        self.agility = 26
        self.intelligence = 26
        self.will_power = 40
        self.fellowship = 25
        self.attacks = 1
        self.wounds = 13
        self._strength_bonus()
        self._toughness_bonus()
        self.movement = 4

        self.armor()
        self.head += 5
        self.left_hand += 3
        self.right_hand += 3
        self.corpse += 5
        self.left_leg += 3
        self.right_leg += 3

        self.weapon.append("wooden shield")
        alternative_weapon = ["1H-weapon", "2H-weapon"]
        self.weapon.append(alternative_weapon[randint(0, len(alternative_weapon) - 1)])

    def wild_orc(self):
        self.weapon_skills = 35
        self.ballistic_skills = 35
        self.strength = 38
        self.toughness = 45
        self.agility = 25
        self.intelligence = 24
        self.will_power = 30
        self.fellowship = 20
        self.attacks = 1
        self.wounds = 12
        self._strength_bonus()
        self._toughness_bonus()
        self.movement = 4
        self.toughness_bonus += 2

        self.armor()
        self.head += 0
        self.left_hand += 0
        self.right_hand += 0
        self.corpse += 0
        self.left_leg += 0
        self.right_leg += 0

        alternative_weapon_1 = ["wooden shield", "dagger"]
        alternative_weapon_2 = ["bow", "spear"]
        self.weapon.append(alternative_weapon_1[randint(0, len(alternative_weapon_1) - 1)])
        self.weapon.append(alternative_weapon_2[randint(0, len(alternative_weapon_2) - 1)])

    def sneak_level(self):
        self.name += " 'sneak'"
        self.weapon_skills += 10
        self.ballistic_skills += 20
        self.strength += 10
        self.toughness += 10
        self.agility += 20
        self.intelligence += 10
        self.will_power += 15
        self.attacks += 1
        self.wounds += 4
        self._strength_bonus()
        self._toughness_bonus()
        if self.orc_kind == "wild":
            self.toughness += 2

        self.armor()
        self.head += 0
        self.left_hand += 1
        self.right_hand += 1
        self.corpse += 1
        self.left_leg += 0
        self.right_leg += 0

        alternative_weapon = ["crossbow", "bow"]
        self.weapon.append(alternative_weapon[randint(0, len(alternative_weapon) - 1)])

    def brute_level(self):
        self.name += " 'brute'"
        self.weapon_skills += 20
        self.ballistic_skills += 10
        self.strength += 15
        self.toughness += 15
        self.agility += 15
        self.will_power += 15
        self.fellowship += 10
        self.attacks += 1
        self.wounds += 6
        self._strength_bonus()
        self._toughness_bonus()
        if self.orc_kind == "wild":
            self.toughness += 2

        self.armor()
        self.head += 0
        self.left_hand += 1
        self.right_hand += 1
        self.corpse += 3
        self.left_leg += 0
        self.right_leg += 0

        alternative_weapon = ["flail", "2H-weapon"]
        self.weapon.append(alternative_weapon[randint(0, len(alternative_weapon) - 1)])

    def chief_level(self):
        self.name += " 'chief'"
        self.weapon_skills += 30
        self.ballistic_skills += 20
        self.strength += 20
        self.toughness += 20
        self.agility += 35
        self.intelligence += 15
        self.will_power += 20
        self.fellowship += 20
        self.attacks += 2
        self.wounds += 8
        self._strength_bonus()
        self._toughness_bonus()
        if self.orc_kind == "wild":
            self.toughness += 2

        if self.orc_kind == "orc":
            self.armor()
            self.head += 3
            self.left_hand += 3
            self.right_hand += 3
            self.corpse += 3
            self.left_leg += 3
            self.right_leg += 3

        if self.orc_kind != "wild":
            self.weapon.remove("wooden shield")
        self.weapon.insert(1, "steel shield")
        alternative_weapon = ["flail", "2H-weapon"]
        self.weapon.append(alternative_weapon[randint(0, len(alternative_weapon) - 1)])

    def __str__(self):
        presentation = f"Name: {self.name}  Type: {self.orc_kind}    Weapons: {self.weapon}\n"\
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

# orc = GenerateOrc("orc")
# orc.sneak_level()
# print(orc)
# orc = GenerateOrc("orc")
# orc.brute_level()
# print(orc)
# orc = GenerateOrc("orc")
# print(orc)
# orc = GenerateOrc("orc")
# orc.chief_level()
# print(orc)
# orc = GenerateOrc("black")
# orc.chief_level()
# print(orc)
# orc = GenerateOrc("wild")
# orc.chief_level()
# print(orc)
