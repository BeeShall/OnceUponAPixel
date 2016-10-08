
from DataManager import DataManager
import json, random, re

class PassageFetcher(object):

    DATA_MANAGER = DataManager()
    LINE_CACHE_SIZE = 4
    LOOK_FORWARD_SIZE = 4


    @staticmethod
    def FetchAndCompilePassages(tags):
        return "\n\n".join(PassageFetcher.FetchPassages(tags))

    @staticmethod
    def FetchPassages(tags):
        return [PassageFetcher.PassagePipe(tag) for tag in tags]

    @staticmethod
    def PassagePipe(tag):
        locations = PassageFetcher.GetLocations(tag)
        coordinates = PassageFetcher.GetRandomLocation(locations)
        raw_passage = PassageFetcher.ExtractPassage(coordinates)
        treated_passage = PassageFetcher.TreatPassage(raw_passage)
        return treated_passage

    @staticmethod
    def GetLocations(tag):
        return PassageFetcher.DATA_MANAGER.DATA[tag.lower()]

    @staticmethod
    def GetRandomLocation(locations):
        return random.choice(locations)

    @staticmethod
    def ExtractPassage(coordinates):

        line_index = 0
        word_index = 0

        # Open up the book
        with open("./books/" + coordinates[0]) as file:
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
        print(sentences)

        if len(sentences) > 3:
            sentences.pop(0)
            sentences.pop(len(sentences)-1)
        return " ".join(sentences)


