class GenerateHumanoid(object):

    def __init__(self):
        self.weapon_skills = 0
        self.ballistic_skills = 0
        self.strength = 0
        self.toughness = 0
        self.agility = 0
        self.intelligence = 0
        self.will_power = 0
        self.fellowship = 0
        self.attacks = 0
        self.wounds = 0
        self.strength_bonus = None
        self.toughness_bonus = None
        self.movement = 0
        self.magic = 0
        self.insane_points = 0
        self.fate_point = 0
        self._strength_bonus()
        self._toughness_bonus()
        self.head = None
        self.left_hand = None
        self.right_hand = None
        self.corpse = None
        self.left_leg = None
        self.right_leg = None
        self.weapon = None

    def _strength_bonus(self):
        if len(str(self.strength)) >= 2:
            self.strength_bonus = int(str(self.strength)[0])
        else:
            self.strength_bonus = 0

    def _toughness_bonus(self):
        if len(str(self.toughness)) >= 2:
            self.toughness_bonus = int(str(self.toughness)[0])
        else:
            self.toughness_bonus = 0

    def armor(self):
        self.head = 0
        self.left_hand = 0
        self.right_hand = 0
        self.corpse = 0
        self.left_leg = 0
        self.right_leg = 0
