import test_data
import json

## Platforms ##
#This is the Platform class.
#Note that the initializer takes 2 arguments:
#  name
#  launch_year
class Platform:
    def __init__(self, name="Unknown", launch_year=0):
        self.name = name
        self.launch_year = launch_year

#This is the Game class.
#Note that the initializer takes 3 arguments:
#  title
#  platform
#  year
class Game:
    def __init__(self, title="Unknown", platform=None, year=0):
        self.title = title
        self.platform = platform
        self.year = year

#This is the GameLibrary class.
#It is defined by a single piece of data: a list of games
class GameLibrary:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def __str__(self):
        return_str = "Analyzing game library data:\n"
        game_count = 0
        for game in self.games:
            return_str += "  Game " + str(game_count) + "\n"
            return_str += "    Title = " + game.title + "\n"
            return_str += "    Year  = " + str(game.year) + "\n"
            return_str += "    Platform = " + "\n"
            return_str += "       Name = " + game.platform.name + "\n"
            return_str += "       Launch Year = " + str(game.platform.launch_year) + "\n"
            game_count += 1
        return return_str
    
#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    for game in json_data["games"]: #Loop through the json_data
        #Create a new Game object from the json_data by reading
        newGame = Game(
        title = game["title"],
        platform = Platform(name = game["platform"]["name"], launch_year = game["platform"]["launch_year"]),
        year = game["year"])
        game_library.add_game(newGame) #Add that Game object to the game_library
    ### End Add Code Here ###

    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
with open(input_json_file, "r") as reader:
#Use the json module to load the data from the file
    game_json_data = json.load(reader)
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
print(make_game_library_from_json(game_json_data))
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
