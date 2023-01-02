#Finished List
landList= []
noDuplicates = []

#Generic
genericLands = ["Command Tower","Prismatic Vista"]

#Fetch Lands
wFetch = ["Flooded Strand","Marsh Flats","Arid Mesa","Windswept Heath"]
bFetch = ["Polluted Delta","Bloodstained Mire","Marsh Flats","Verdant Catacombs"]
uFetch = ["Polluted Delta","Flooded Strand","Scalding Tarn","Misty Rainforest"]
rFetch = ["Bloodstained Mire","Wooded Foothills","Scalding Tarn","Arid Mesa"]
gFetch = ["Windswept Heath","Wooded Foothills","Verdant Catacombs","Misty Rainforest"]

#User Input and Extend Finished Lists
colorSelection = input()
landList.extend(genericLands)
if "w" in colorSelection:
    landList.extend(wFetch)
if "b" in colorSelection:
    landList.extend(bFetch)
if "u" in colorSelection:
    landList.extend(uFetch)
if "r" in colorSelection:
    landList.extend(rFetch)
if "g" in colorSelection:
    landList.extend(gFetch)
for land in landList:
    if land not in noDuplicates:
        noDuplicates.append(land)
for item in noDuplicates:
    print(item)

