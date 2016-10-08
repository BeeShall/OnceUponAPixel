from PassageFetcher import PassageFetcher

tags = ["trees", "city", "rain", "person"]
passage = PassageFetcher.FetchAndCompilePassages(tags)

print("\n\n")
print("Passage for " + ", ".join(tags) + "\n------------------\n\n")
print(passage)
print("\n\n")