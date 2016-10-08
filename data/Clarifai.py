
from clarifai.client import ClarifaiApi
import json

class Clarifai(object):
    
    CONNECTION = ClarifaiApi()

    @staticmethod
    def SubmitImage(url):
        result = Clarifai.CONNECTION.tag_images(url)
        return result

    @staticmethod
    def ParseProbabilities(JSON_response, tags):
        results = zip(JSON_response['results'][0]['result']['tag']['classes'], 
            JSON_response['results'][0]['result']['tag']['probs'])
        retval = []
        for entry in results:
            if entry[0] in tags:
                retval.append(entry)
        return retval

    @staticmethod
    def GetProbabilities(url, tags):
        return Clarifai.ParseProbabilities(Clarifai.SubmitImage(url), tags)


