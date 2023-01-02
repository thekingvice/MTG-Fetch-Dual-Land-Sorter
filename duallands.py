#Finished List
landList= []
noDuplicates = []

#Dual Lands
azoriusWU = ["Sea of Clouds","Hallowed Fountain","Deserted Beach","Glacial Floodplain"]
dimirUB = ["Morphic Pool","Watery Grave","Shipwreck Marsh","Ice Tunnel"]
rakdosBR = ["Luxury Suite","Blood Crypt","Haunted Ridge","Sulfurous Mire"]
gruulRG = ["Spire Garden","Stomping Ground","Rockfall Vale","Highland Forest"]
selesnyaGW = ["Bountiful Promenade","Temple Garden","Overgrown Farmland","Arctic Treeline"]
orzhovWB = ["Vault of Champions","Godless Shrine","Shattered Sanctum","Snowfield Sinkhole"]
izzetUR = ["Training Center","Steam Vents","Stormcarved Coast","Volatile Fjord"]
golgariBG = ["Undergrowth Stadium","Overgrown Tomb","Deathcap Glade","Woodland Chasm"]
borosRW = ["Spectator Seating","Sacred Foundry","Sundown Pass","Alpine Meadow"]
simicGU = ["Rejuvenating Springs","Breeding Pool","Dreamroot Cascade","Rimewood Falls"]

#User Input and Extend Finished Lists
colorSelection = input()
if "w" in colorSelection and "u" in colorSelection:
    landList.extend(azoriusWU)
if "u" in colorSelection and "b" in colorSelection:
    landList.extend(dimirUB)
if "b" in colorSelection and "r" in colorSelection:
    landList.extend(rakdosBR)
if "r" in colorSelection and "g" in colorSelection:
    landList.extend(gruulRG)
if "g" in colorSelection and "w" in colorSelection:
    landList.extend(selesnyaGW)
if "w" in colorSelection and "b" in colorSelection:
    landList.extend(orzhovWB)
if "u" in colorSelection and "r" in colorSelection:
    landList.extend(izzetUR)
if "b" in colorSelection and "g" in colorSelection:
    landList.extend(golgariBG)
if "r" in colorSelection and "w" in colorSelection:
    landList.extend(borosRW)
if "g" in colorSelection and "u" in colorSelection:
    landList.extend(simicGU)
for land in landList:
    if land not in noDuplicates:
        noDuplicates.append(land)
for item in noDuplicates:
    print(item)