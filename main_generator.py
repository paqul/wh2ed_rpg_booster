from random import randint
# from humans_generator import GenerateHuman
from orcs_generator import GenerateOrc

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


class ArmyGenerator(object):

    def __init__(self):
        self.overall_counter = 0
        for cnt in range(10):
            regiment = RegimentGenerator(f"{cnt+1}_regiment")
            self.overall_counter += regiment.amount
        experimental_pack = RegimentGenerator("ex_regiment")
        experimental_pack.save_to_txt_file(experimental_pack.gen_amount_of_orcs(1, "black", "chief"))
        self.overall_counter += experimental_pack.amount

orcs_clan = ArmyGenerator()
print(orcs_clan.overall_counter)