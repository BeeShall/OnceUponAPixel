from PassageFetcher import PassageFetcher
from Clarifai import Clarifai

tags = Clarifai.SubmitImage(open('/Users/NateMoon/downloads/testimage.jpg'))['results'][0]['result']['tag']['classes']

passage = PassageFetcher.FetchAndCompilePassages(tags)

print("\n\n")
print("Passage for " + ", ".join(tags) + "\n------------------\n\n")
print(passage)
print("\n\n")



