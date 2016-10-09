
from data.DataManager import DataManager
import json, random, re

Novels = {
    "20000_Leagues_Under_The_Sea.txt": "Jules Verne",
    "A_Tale_of_Two_Cities.txt": "Charles Dickens",
    "Aladdin_and_the_Lamp.txt": "Antoine Galland",
    "Alices_Adventures_in_Wonderland.txt": "Lewis Carroll",
    "Around_the_World_in_80_Days.txt": "Jules Verne",
    "Gullivers_Travels.txt": "Jonathan Swift",
    "Leviathon": "Thomas Hobbes",
    "Peter_Pan": "J. M. Barrie" 
}

class PassageFetcher(object):

    DATA_MANAGER = DataManager()
    LINE_CACHE_SIZE = 4
    LOOK_FORWARD_SIZE = 4
    TAG_LIMIT = 4
    NEGATORY_QUOTE = "'Remember not only to say the right thing in the right place, but far more difficult still, to leave unsaid the wrong thing at the tempting moment.' - Benjamin Franklin"

    @staticmethod
    def FetchAndCompilePassages(tags):
        print(tags)
        tags = [str(tag) for tag in tags]
        # Validate tags
        valid_tags = PassageFetcher.ValidateTags(tags)
        print(valid_tags)

        
        
        # Get passages
        result = "\n\n".join(PassageFetcher.
            FetchPassages(valid_tags if len(valid_tags) < PassageFetcher.
                TAG_LIMIT else valid_tags[0:PassageFetcher.
                TAG_LIMIT]))

        if result == None or result.isspace():
            return PassageFetcher.NEGATORY_QUOTE
        else:
            return result

    @staticmethod
    def FetchPassages(tags):
        return [PassageFetcher.PassagePipe(tag) for tag in tags]

    @staticmethod
    def PassagePipe(tag):
        locations = PassageFetcher.GetLocations(tag)
        if locations == None: return ""
        coordinates = PassageFetcher.GetRandomLocation(locations)
        raw_passage = PassageFetcher.ExtractPassage(coordinates)
        treated_passage = PassageFetcher.TreatPassage(raw_passage)
        return treated_passage


    @staticmethod
    def ValidateTags(tags):
        ### ADD THE SORT HERE ###
        valid_tags = []
        for tag in tags:
            try:
                PassageFetcher.DATA_MANAGER.DATA[tag.lower()]
                valid_tags.append(tag)
            except:
                print(tag + " was not found.")

        return valid_tags

    @staticmethod
    def GetLocations(tag):
        try:
            locations = PassageFetcher.DATA_MANAGER.DATA[tag.lower()]
        except Exception as e:
            print("Error: ")
            return None
        return locations


    @staticmethod
    def GetRandomLocation(locations):
        return random.choice(locations)

    @staticmethod
    def ExtractPassage(coordinates):

        line_index = 0
        word_index = 0

        # Open up the book
        with open("./data/books/" + coordinates[0]) as file:
            # Compile regex sentence pattern
            line_cache = []
            found_flag = False
            local_timer = PassageFetcher.LOOK_FORWARD_SIZE
            # Find line
            for line in file:
                words = line.split()
                # Find word
                for word in words:
                    # If the word is found, compile the passage response
                    if word_index == coordinates[2]:
                        found_flag = True

                    word_index += 1
                line_index += 1

                if line != '\r\n' and line != '\n' and line != '\r':
                    line_cache.append(line)
                    if len(line_cache) > PassageFetcher.LINE_CACHE_SIZE and not found_flag:
                        line_cache.pop(0)

                if found_flag:
                    local_timer -= 1

                if local_timer <= 0:
                    break


        return "".join(line_cache)

    @staticmethod
    def TreatPassage(raw_passage):
        pattern = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
        sentences = pattern.findall(raw_passage)

        if len(sentences) > 3:
            sentences.pop(0)
            sentences.pop(len(sentences)-1)
        return " ".join(sentences)


