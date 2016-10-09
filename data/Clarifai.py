
from clarifai.client import ClarifaiApi
import json

class Clarifai(object):
    
    CONNECTION = ClarifaiApi()

    @staticmethod
    def SubmitImageWithBuffer(resource):
        result = Clarifai.CONNECTION.tag_images(resource)
        return result

    @staticmethod
    def SubmitImageWithURL(url):
        result = Clarifai.CONNECTION.tag_image_urls(url)
        return result

    @staticmethod
    def ParseProbabilities(JSON_response):
        results = zip(JSON_response['results'][0]['result']['tag']['classes'], 
            JSON_response['results'][0]['result']['tag']['probs'])
        return results

    @staticmethod
    def GetProbabilities(JSON_Object):
        return Clarifai.ParseProbabilities(JSON_Object)


