
from PassageFetcher import PassageFetcher

locations = PassageFetcher.GetLocations("tree")

coords = PassageFetcher.GetRandomLocation(locations)
print()
print(coords)


with open("./books/" + coords[0]) as file:
    lines = file.readlines()
    print(lines)
    print(lines[coords[1]])



