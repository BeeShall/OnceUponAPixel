
from data.Clarifai import Clarifai
from data.PassageFetcher import PassageFetcher


class Model(object):

    def __init__(self, url):
        self.URL = url
        self.Tags = None

    def RunClarifai(self):
        tags = Clarifai.SubmitImageWithURL(self.URL)
        tags = sorted(list(Clarifai.GetProbabilities(tags)), key=lambda tag: tag[1], reverse=True)
        tags = [tag[0] for tag in tags]
        self.Tags = tags
        return tags

    def GeneratePassage(self):
        passage = PassageFetcher.FetchAndCompilePassages(self.Tags)
        return passage
