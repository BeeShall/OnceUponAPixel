from PassageFetcher import PassageFetcher
from Clarifai import Clarifai

tags = Clarifai.SubmitImageWithURL("http://www.qqxxzx.com/images/awesome-images/awesome-images-20.jpg")
tags = sorted(list(Clarifai.GetProbabilities(tags)), key=lambda tag: tag[1], reverse=True)
tags = [tag[0] for tag in tags]
passage = PassageFetcher.FetchAndCompilePassages(tags)

print("\n\n")
print("Passage for " + ", ".join(tags) + "\n------------------\n\n")
print(passage)
print("\n\n")



