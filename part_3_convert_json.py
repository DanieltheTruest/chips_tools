import cc_dat_utils as ccdat
import cc_classes as cclass
import json
#Part 3


def make_cc_level_pack_from_json(level_data):
    level_pack = cclass.CCLevelPack()
    for level in level_data["levels"]:
        ccLevel = cclass.CCLevel()
        ccLevel.level_number = level["level_number"]
        ccLevel.time = level["time"]
        ccLevel.num_chips = level["chip_number"]
        ccLevel.upper_layer = level["upperLayer"]
        print(ccLevel.upper_layer)
        if level["title"] != None:
            ccLevel.add_field(cclass.CCMapTitleField(level["title"]))
        if level["encpassword"] != None:
            ccLevel.add_field(cclass.CCEncodedPasswordField(level["encpassword"]))
        if level["monsters"]  != None:
            monsters = []
            for monster in level["monsters"]:
                x = monster["x"]
                y = monster["y"]
                monsterCoordinates = cclass.CCCoordinate(x, y)
                monsters.append(monsterCoordinates)
            ccLevel.add_field(cclass.CCMonsterMovementField(monsters))
        if level["hints"] != None:
            ccLevel.add_field(cclass.CCMapHintField(level["hints"]))
        level_pack.add_level(ccLevel)
    return level_pack


input_json_file = "data/dc3_levelPack.json"
with open(input_json_file, "r") as file:  #Load your custom JSON file
    level_data = json.load(file)     




level_pack = make_cc_level_pack_from_json(level_data) #Convert JSON data to CCLevelPack
print(level_pack)


output = "dc3_levelPack.dat" #Save converted data to DAT file
ccdat.write_cc_level_pack_to_dat(level_pack, output)
print("yes")