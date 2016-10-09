import json

class DataManager(object):

    def __init__(self):
        with open("./data/Result_Map.json", 'r') as datafile:
            self.DATA = json.load(datafile)

