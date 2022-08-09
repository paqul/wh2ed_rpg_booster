from random import randint
# from humans_generator import GenerateHuman
from orcs_generator import GenerateOrc
from goblins_generator import GenerateGreen

amount_active_orcs = 6500

bloody_hands_clan = 2000
crushers_clan = 1500
bread_cutters_clan = 1000
ironskinz_clan = 2000


class RegimentGenerator(object):
    """
    pack_1 = RegimentGenerator("1_regiment")
    pack_2 = RegimentGenerator("2_regiment")
    pack_3 = RegimentGenerator("3_regiment")
    pack_4 = RegimentGenerator("4_regiment")
    """

    def __init__(self, name_of_file: str):
        self.name_of_file = name_of_file
        self.amount = None
        self.counter = None
        self.level_troop_list = []
        self.determinate_number_of_troops()
        self.determinate_level_of_troops()
        generated_orcs = self.gen_determinate_amount_of_orcs(self.level_troop_list)
        self.save_to_txt_file(generated_orcs)

        # generated_orcs = self.gen_amount_of_orcs(self.amount)
        # self.save_to_txt_file(generated_orcs)

    def determinate_number_of_troops(self):
        self.amount = randint(4, 20)
        self.counter = self.amount

    def determinate_level_of_troops(self):
        self.level_troop_list = []
        while True:
            if self.counter == 0:
                break
            else:
                self.counter -= 1
                percent_chance = randint(1, 100)
                if 60 >= percent_chance >= 1:
                    self.level_troop_list.append("regular")
                elif 80 >= percent_chance >= 61:
                    self.level_troop_list.append("sneak")
                elif 100 >= percent_chance >= 81:
                    self.level_troop_list.append("brute")

    def gen_determinate_amount_of_orcs(self, troop_list: list, orcs_kind: str = "orc"):
        orcs = []
        for level in troop_list:
            if level == "sneak":
                kind = {"orc": GenerateOrc(), "black": GenerateOrc("black"), "wild": GenerateOrc("wild")}
                orc = kind[orcs_kind]
                orc.sneak_level()
                orcs.append(orc)
            elif level == "brute":
                kind = {"orc": GenerateOrc(), "black": GenerateOrc("black"), "wild": GenerateOrc("wild")}
                orc = kind[orcs_kind]
                orc.brute_level()
                orcs.append(orc)
            elif level == "chief":
                kind = {"orc": GenerateOrc(), "black": GenerateOrc("black"), "wild": GenerateOrc("wild")}
                orc = kind[orcs_kind]
                orc.chief_level()
                orcs.append(orc)
            else:
                kind = {"orc": GenerateOrc(), "black": GenerateOrc("black"), "wild": GenerateOrc("wild")}
                orc = kind[orcs_kind]
                orcs.append(orc)
        return orcs

    def gen_amount_of_orcs(self, amount: int = 1, orcs_kind: str = "orc", orc_type: str = "regular"):
        """
        experimental_pack = RegimentGenerator("ex_regiment")
        experimental_pack.save_to_txt_file(experimental_pack.gen_amount_of_orcs(1, "black", "chief"))

        :param amount:
        :param orcs_kind:
        :param orc_type:
        :return:
        """
        orcs = []
        for _ in range(amount):
            if orc_type == "sneak":
                kind = {"orc": GenerateOrc(), "black": GenerateOrc("black"), "wild": GenerateOrc("wild")}
                orc = kind[orcs_kind]
                orc.sneak_level()
                orcs.append(orc)
            elif orc_type == "brute":
                kind = {"orc": GenerateOrc(), "black": GenerateOrc("black"), "wild": GenerateOrc("wild")}
                orc = kind[orcs_kind]
                orc.brute_level()
                orcs.append(orc)
            elif orc_type == "chief":
                kind = {"orc": GenerateOrc(), "black": GenerateOrc("black"), "wild": GenerateOrc("wild")}
                orc = kind[orcs_kind]
                orc.chief_level()
                orcs.append(orc)
            else:
                kind = {"orc": GenerateOrc(), "black": GenerateOrc("black"), "wild": GenerateOrc("wild")}
                orc = kind[orcs_kind]
                orcs.append(orc)
        return orcs

    def save_to_txt_file(self, generated_army):
        with open(f"{self.name_of_file}.txt", '+a') as file:
            for _ in range(len(generated_army)):
                file.write(generated_army[_].__str__())
                file.write("\n")
            file.close()


class GreenRegimentGenerator(object):
    """
    pack_1 = GreenRegimentGenerator("1_regiment", 1, 20, "goblin")
    pack_2 = GreenRegimentGenerator("2_regiment", 1, 10, "fanatic")
    pack_3 = GreenRegimentGenerator("3_regiment", 1, 200, "snotling")
    """

    def __init__(self, name_of_file: str, minimum: int, maximum: int, green_type: str = "goblin"):
        self.name_of_file = name_of_file
        self.amount = None
        self.counter = None
        self.level_troop_list = []
        self.determinate_number_of_troops(minimum, maximum)
        self.determinate_level_of_troops()
        generated_greens = self.gen_determinate_amount_of_green(self.level_troop_list, green_type)
        self.save_to_txt_file(generated_greens)

        # generated_orcs = self.gen_amount_of_orcs(self.amount)
        # self.save_to_txt_file(generated_orcs)

    def determinate_number_of_troops(self, minimum, maximum):
        self.amount = randint(minimum, maximum)
        self.counter = self.amount

    def determinate_level_of_troops(self):
        self.level_troop_list = []
        while True:
            if self.counter == 0:
                break
            else:
                self.counter -= 1
                percent_chance = randint(1, 100)
                if 60 >= percent_chance >= 1:
                    self.level_troop_list.append("regular")
                elif 94 >= percent_chance >= 81:
                    self.level_troop_list.append("sneak")
                elif 100 >= percent_chance >= 95:
                    self.level_troop_list.append("brute")

    def gen_determinate_amount_of_green(self, troop_list: list, green_kind: str = "goblin"):
        greens = []
        for level in troop_list:
            if level == "sneak":
                kind = {"goblin": GenerateGreen(), "snotling": GenerateGreen("snotling"), "fanatic": GenerateGreen("fanatic")}
                green = kind[green_kind]
                green.sneak_level()
                greens.append(green)
            elif level == "brute":
                kind = {"goblin": GenerateGreen(), "snotling": GenerateGreen("snotling"), "fanatic": GenerateGreen("fanatic")}
                green = kind[green_kind]
                green.brute_level()
                greens.append(green)
            elif level == "chief":
                kind = {"goblin": GenerateGreen(), "snotling": GenerateGreen("snotling"), "fanatic": GenerateGreen("fanatic")}
                green = kind[green_kind]
                green.chief_level()
                greens.append(green)
            else:
                kind = {"goblin": GenerateGreen(), "snotling": GenerateGreen("snotling"), "fanatic": GenerateGreen("fanatic")}
                green = kind[green_kind]
                greens.append(green)
        return greens

    def gen_amount_of_green(self, amount: int = 1, green_kind: str = "goblin", green_type: str = "regular"):
        """
        experimental_pack = GreenRegimentGenerator("ex_regiment")
        experimental_pack.save_to_txt_file(experimental_pack.gen_amount_of_green(1, "goblin", "sneak"))

        :param amount:
        :param green_kind:
        :param green_type:
        :return:
        """
        greens = []
        for _ in range(amount):
            if green_type == "sneak":
                kind = {"goblin": GenerateGreen(), "snotling": GenerateGreen("snotling"), "fanatic": GenerateGreen("fanatic")}
                green = kind[green_kind]
                green.sneak_level()
                greens.append(green)
            elif green_type == "brute":
                kind = {"goblin": GenerateGreen(), "snotling": GenerateGreen("snotling"), "fanatic": GenerateGreen("fanatic")}
                green = kind[green_kind]
                green.brute_level()
                greens.append(green)
            elif green_type == "chief":
                kind = {"goblin": GenerateGreen(), "snotling": GenerateGreen("snotling"), "fanatic": GenerateGreen("fanatic")}
                green = kind[green_kind]
                green.chief_level()
                greens.append(green)
            else:
                kind = {"goblin": GenerateGreen(), "snotling": GenerateGreen("snotling"), "fanatic": GenerateGreen("fanatic")}
                green = kind[green_kind]
                greens.append(green)
        return greens

    def save_to_txt_file(self, generated_army):
        with open(f"{self.name_of_file}.txt", '+a') as file:
            for _ in range(len(generated_army)):
                file.write(generated_army[_].__str__())
                file.write("\n")
            file.close()

class ArmyGenerator(object):

    def __init__(self, amount_of_army=1):
        self.overall_counter = 0
        for cnt in range(amount_of_army):
            regiment = RegimentGenerator(f"{cnt+1}_regiment")
            self.overall_counter += regiment.amount
        experimental_pack = RegimentGenerator("ex_regiment")
        experimental_pack.save_to_txt_file(experimental_pack.gen_amount_of_orcs(1, "black", "chief"))
        self.overall_counter += experimental_pack.amount

class ArmyGeneratorv2(object):
    """
    orcs_clan = ArmyGeneratorv2(2, 10, 150, "snotling")
    orcs_clan = ArmyGeneratorv2(5, 5, 50, "goblin")
    orcs_clan = ArmyGeneratorv2(3, 1, 3, "fanatic")
    """
    def __init__(self, amount_of_army=1, min_reg=1, max_reg=2, green_type="goblin"):
        self.overall_counter = 0
        for cnt in range(amount_of_army):
            regiment = GreenRegimentGenerator(f"{cnt+1}_regiment", min_reg, max_reg, green_type)
            self.overall_counter += regiment.amount

orcs_clan = ArmyGeneratorv2(3, 1, 3, "fanatic")
print(orcs_clan.overall_counter)
