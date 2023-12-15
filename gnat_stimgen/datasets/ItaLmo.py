

"""Dataset for ItaLmo stimuli."""
from ..types import AudioStimulus, PictureStimulus


pstimlist: list[PictureStimulus] = [
    # POSITIVE PICTURE STIMULI
    #               Filename,    Description,                     Valence
    PictureStimulus("pos01.jpg", "Ladybird",                 "pos"),
    PictureStimulus("pos02.jpg", "Land turtle on grass/straw", "pos"),
    PictureStimulus("pos03.jpg", "Monkeys in tree",             "pos"),
    PictureStimulus("pos04.jpg", "Peacock with wheel tail",   "pos"),
    PictureStimulus("pos05.jpg", "Sea horses",      "pos"),
    PictureStimulus("pos06.jpg", "Toddler pushes toy car on lawn",        "pos"),
    PictureStimulus("pos07.jpg", "Yellow flower corolla",          "pos"),
    PictureStimulus("pos08.jpg", "Cat aeting from a jar",             "pos"),
    PictureStimulus("pos09.jpg", "Boy on the swing at the beach",            "pos"),
    PictureStimulus("pos10.jpg", "White water lily", "pos"),
    #               Filename,    Description,                         Valence
    PictureStimulus("pos11.jpg", "Pier on the sea",     "pos"),
    PictureStimulus("pos12.jpg", "Grean mountain with road",           "pos"),
    PictureStimulus("pos13.jpg", "Flowers in meadow", "pos"),
    PictureStimulus("pos14.jpg", "Broad-leaved green grass",         "pos"),
    PictureStimulus("pos15.jpg", "Beach shore with children and swans",  "pos"),
    PictureStimulus("pos16.jpg", "Tulips in the grass",        "pos"),
    PictureStimulus("pos17.jpg", "2 dandelions in bloom",    "pos"),
    PictureStimulus("pos18.jpg", "2 water lilies with leaves",            "pos"),
    PictureStimulus("pos19.jpg", "3 young friends from behind, on sea rocks",    "pos"),
    #               Filename,    Description,                          Valence
    PictureStimulus("pos20.jpg", "Skier in snowy landscape",          "pos"),
    PictureStimulus("pos21.jpg", "Corals with lots of little fish",            "pos"),
    PictureStimulus("pos22.jpg", "Toddler in the woods with sunglasses",        "pos"),
    PictureStimulus("pos23.jpg", "Cow grazing in meadow",         "pos"),
    PictureStimulus("pos24.jpg", "Hills, flowery meadow and trees",      "pos"),
    PictureStimulus("pos25.jpg", "Dirt road in the woods", "pos"),
    PictureStimulus("pos26.jpg", "Snowboarder in the snow",         "pos"),
    PictureStimulus("pos27.jpg", "Butterfly on leaves",          "pos"),
    PictureStimulus("pos28.jpg", "Yellow tulips with leaves",             "pos"),
    PictureStimulus("pos29.jpg", "Tropical fish",          "pos"),
    PictureStimulus("pos30.jpg", "Palm trees from below",                "pos"),
    #               Filename,    Description,                 Valence
    PictureStimulus("pos31.jpg", "Multicolored parachute",      "pos"),
    PictureStimulus("pos32.jpg", "Diver with corals", "pos"),
    PictureStimulus("pos33.jpg", "Palm trees with hut",         "pos"),
    PictureStimulus("pos34.jpg", "Yellow boat sailing, with mountains",    "pos"),
    PictureStimulus("pos35.jpg", "2 elderly people on a little bridge",         "pos"),
    PictureStimulus("pos36.jpg", "Flowers for sale at a market",    "pos"),
    PictureStimulus("pos37.jpg", "Flowers for sale wrapped in cellophane", "pos"),
    PictureStimulus("pos38.jpg", "2 cows grazing, with mountains",     "pos"),
    PictureStimulus("pos39.jpg", "Surfer flying over the sea",    "pos"),
    PictureStimulus("pos40.jpg", "2 fish among corals",       "pos"),
    # NEGATIVE PICTURE STIMULI
    #               Filename,    Description,                       Valence
    PictureStimulus("neg01.jpg", "Gutted hamster on cloth",       "neg"),
    PictureStimulus("neg02.jpg", "Dead frog",         "neg"),
    PictureStimulus("neg03.jpg", "Mosquito on human skin",   "neg"),
    PictureStimulus("neg04.jpg", "Sectioned guinea pig, with scissors",     "neg"),
    PictureStimulus("neg05.jpg", "Black kitten with injured muzzle",          "neg"),
    PictureStimulus("neg06.jpg", "Big hairy spider",   "neg"),
    PictureStimulus("neg07.jpg", "Crushed pigeon",        "neg"),
    PictureStimulus("neg08.jpg", "Globose arachnid with its eggs",           "neg"),
    PictureStimulus("neg09.jpg", "Rotting rat with ants and crumbs",           "neg"),
    PictureStimulus("neg10.jpg", "Dead bird on sand", "neg"),
    #               Filename,    Description,                       Valence
    PictureStimulus("neg11.jpg", "Snowy concentration camp",    "neg"),
    PictureStimulus("neg12.jpg", "Rubbish in vegetation",    "neg"),
    PictureStimulus("neg13.jpg", "Dilapidated building",         "neg"),
    PictureStimulus("neg14.jpg", "Piles of rubbish in industrial warehouse",     "neg"),
    PictureStimulus("neg15.jpg", "Flooded and messy basement",       "neg"),
    PictureStimulus("neg16.jpg", "Moldy soup in the pot",    "neg"),
    PictureStimulus("neg17.jpg", "Rubbish at the foot of a tree",        "neg"),
    PictureStimulus("neg18.jpg", "Rotting rodents",        "neg"),
    PictureStimulus("neg19.jpg", "White toilet with drops of blood", "neg"),
    PictureStimulus("neg20.jpg", "Burnt garbage can",  "neg"),
    #               Filename,    Description,                        Valence
    PictureStimulus("neg21.jpg", "Rusty waste bin",   "neg"),
    PictureStimulus("neg22.jpg", "2 revolvers",                 "neg"),
    PictureStimulus("neg23.jpg", "Man lying on the sidewalk",               "neg"),
    PictureStimulus("neg24.jpg", "Filthy white toilet",                 "neg"),
    PictureStimulus("neg25.jpg", "Weapons and handcuffs", "neg"),
    PictureStimulus("neg26.jpg", "Man rummaging in waste bin",                         "neg"),
    PictureStimulus("neg27.jpg", "People sleeping on urban public passage",              "neg"),
    PictureStimulus("neg28.jpg", "Coffins",               "neg"),
    PictureStimulus("neg29.jpg", "Scrap metal on lawn",            "neg"),
    PictureStimulus("neg30.jpg", "Car accident, victim and rescuers", "neg"),
    #               Filename,    Description,                            Valence
    PictureStimulus("neg31.jpg", "Filthy blue toilet",                         "neg"),
    PictureStimulus("neg32.jpg", "Looted bicycle, without wheels",            "neg"),
    PictureStimulus("neg33.jpg", "Car accident at night",              "neg"),
    PictureStimulus("neg34.jpg", "Motorcycle accident",                       "neg"),
    PictureStimulus("neg35.jpg", "Soldier with rifle on his shoulder",     "neg"),
    PictureStimulus("neg36.jpg", "Truck seriously damaged",              "neg"),
    PictureStimulus("neg37.jpg", "Dead boar and blood",         "neg"),
    PictureStimulus("neg38.jpg", "Woman sleeping on the sidewalk",                           "neg"),
    PictureStimulus("neg39.jpg", "Corpse on sidewalk and police",                  "neg"),
    PictureStimulus("neg40.jpg", "Accidented car and tram",                "neg"),
]

pstimdict: dict[str, PictureStimulus] = {
    stim.filename: stim for stim in pstimlist
}

astimlist: list[AudioStimulus] = [
    # ItaMAN AUDIO STIMULISTIMULI
    #             Filename,    Description,                 Lang,  Compatible positive picture stimuli,                                                              Compatible negative picture stimuli
    AudioStimulus("Ita01.wav", "Glass",                   "Ita", [pstimdict["pos01.jpg"], pstimdict["pos11.jpg"], pstimdict["pos21.jpg"], pstimdict["pos31.jpg"]], [pstimdict["neg01.jpg"], pstimdict["neg11.jpg"], pstimdict["neg21.jpg"], pstimdict["neg31.jpg"]]),
    AudioStimulus("Ita02.wav", "Roof",      "Ita", [pstimdict["pos02.jpg"], pstimdict["pos12.jpg"], pstimdict["pos22.jpg"], pstimdict["pos32.jpg"]], [pstimdict["neg02.jpg"], pstimdict["neg12.jpg"], pstimdict["neg22.jpg"], pstimdict["neg32.jpg"]]),
    AudioStimulus("Ita03.wav", "Pipe/Tube/Hose",      "Ita", [pstimdict["pos03.jpg"], pstimdict["pos13.jpg"], pstimdict["pos23.jpg"], pstimdict["pos33.jpg"]], [pstimdict["neg03.jpg"], pstimdict["neg13.jpg"], pstimdict["neg23.jpg"], pstimdict["neg33.jpg"]]),
    AudioStimulus("Ita04.wav", "Juice",                     "Ita", [pstimdict["pos04.jpg"], pstimdict["pos14.jpg"], pstimdict["pos24.jpg"], pstimdict["pos34.jpg"]], [pstimdict["neg04.jpg"], pstimdict["neg14.jpg"], pstimdict["neg24.jpg"], pstimdict["neg34.jpg"]]),
    AudioStimulus("Ita05.wav", "Chest",         "Ita", [pstimdict["pos05.jpg"], pstimdict["pos15.jpg"], pstimdict["pos25.jpg"], pstimdict["pos35.jpg"]], [pstimdict["neg05.jpg"], pstimdict["neg15.jpg"], pstimdict["neg25.jpg"], pstimdict["neg35.jpg"]]),
    AudioStimulus("Ita06.wav", "Chicken",                  "Ita", [pstimdict["pos06.jpg"], pstimdict["pos16.jpg"], pstimdict["pos26.jpg"], pstimdict["pos36.jpg"]], [pstimdict["neg06.jpg"], pstimdict["neg16.jpg"], pstimdict["neg26.jpg"], pstimdict["neg36.jpg"]]),
    AudioStimulus("Ita07.wav", "Iron",          "Ita", [pstimdict["pos07.jpg"], pstimdict["pos17.jpg"], pstimdict["pos27.jpg"], pstimdict["pos37.jpg"]], [pstimdict["neg07.jpg"], pstimdict["neg17.jpg"], pstimdict["neg27.jpg"], pstimdict["neg37.jpg"]]),
    AudioStimulus("Ita08.wav", "Nerve",                   "Ita", [pstimdict["pos08.jpg"], pstimdict["pos18.jpg"], pstimdict["pos28.jpg"], pstimdict["pos38.jpg"]], [pstimdict["neg08.jpg"], pstimdict["neg18.jpg"], pstimdict["neg28.jpg"], pstimdict["neg38.jpg"]]),
    AudioStimulus("Ita09.wav", "Chariot",                   "Ita", [pstimdict["pos09.jpg"], pstimdict["pos19.jpg"], pstimdict["pos29.jpg"], pstimdict["pos39.jpg"]], [pstimdict["neg09.jpg"], pstimdict["neg19.jpg"], pstimdict["neg29.jpg"], pstimdict["neg39.jpg"]]),
    AudioStimulus("Ita10.wav", "Breath",                 "Ita", [pstimdict["pos10.jpg"], pstimdict["pos20.jpg"], pstimdict["pos30.jpg"], pstimdict["pos40.jpg"]], [pstimdict["neg10.jpg"], pstimdict["neg20.jpg"], pstimdict["neg30.jpg"], pstimdict["neg40.jpg"]]),
    #             Filename,    Description,                 Lang,  Compatible positive picture stimuli,                                                              Compatible negative picture stimuli
    AudioStimulus("Ita11.wav", "Package",                   "Ita", [pstimdict["pos01.jpg"], pstimdict["pos11.jpg"], pstimdict["pos21.jpg"], pstimdict["pos31.jpg"]], [pstimdict["neg01.jpg"], pstimdict["neg11.jpg"], pstimdict["neg21.jpg"], pstimdict["neg31.jpg"]]),
    AudioStimulus("Ita12.wav", "Tower",              "Ita", [pstimdict["pos02.jpg"], pstimdict["pos12.jpg"], pstimdict["pos22.jpg"], pstimdict["pos32.jpg"]], [pstimdict["neg02.jpg"], pstimdict["neg12.jpg"], pstimdict["neg22.jpg"], pstimdict["neg32.jpg"]]),
    AudioStimulus("Ita13.wav", "Sack",              "Ita", [pstimdict["pos03.jpg"], pstimdict["pos13.jpg"], pstimdict["pos23.jpg"], pstimdict["pos33.jpg"]], [pstimdict["neg03.jpg"], pstimdict["neg13.jpg"], pstimdict["neg23.jpg"], pstimdict["neg33.jpg"]]),
    AudioStimulus("Ita14.wav", "Finger",                "Ita", [pstimdict["pos04.jpg"], pstimdict["pos14.jpg"], pstimdict["pos24.jpg"], pstimdict["pos34.jpg"]], [pstimdict["neg04.jpg"], pstimdict["neg14.jpg"], pstimdict["neg24.jpg"], pstimdict["neg34.jpg"]]),
    AudioStimulus("Ita15.wav", "Edge/Board",              "Ita", [pstimdict["pos05.jpg"], pstimdict["pos15.jpg"], pstimdict["pos25.jpg"], pstimdict["pos35.jpg"]], [pstimdict["neg05.jpg"], pstimdict["neg15.jpg"], pstimdict["neg25.jpg"], pstimdict["neg35.jpg"]]),
    AudioStimulus("Ita16.wav", "Wall",                     "Ita", [pstimdict["pos06.jpg"], pstimdict["pos16.jpg"], pstimdict["pos26.jpg"], pstimdict["pos36.jpg"]], [pstimdict["neg06.jpg"], pstimdict["neg16.jpg"], pstimdict["neg26.jpg"], pstimdict["neg36.jpg"]]),
    AudioStimulus("Ita17.wav", "Neck",                     "Ita", [pstimdict["pos07.jpg"], pstimdict["pos17.jpg"], pstimdict["pos27.jpg"], pstimdict["pos37.jpg"]], [pstimdict["neg07.jpg"], pstimdict["neg17.jpg"], pstimdict["neg27.jpg"], pstimdict["neg37.jpg"]]),
    AudioStimulus("Ita18.wav", "Bump/Hill",      "Ita", [pstimdict["pos08.jpg"], pstimdict["pos18.jpg"], pstimdict["pos28.jpg"], pstimdict["pos38.jpg"]], [pstimdict["neg08.jpg"], pstimdict["neg18.jpg"], pstimdict["neg28.jpg"], pstimdict["neg38.jpg"]]),
    AudioStimulus("Ita19.wav", "Step",                 "Ita", [pstimdict["pos09.jpg"], pstimdict["pos19.jpg"], pstimdict["pos29.jpg"], pstimdict["pos39.jpg"]], [pstimdict["neg09.jpg"], pstimdict["neg19.jpg"], pstimdict["neg29.jpg"], pstimdict["neg39.jpg"]]),
    AudioStimulus("Ita20.wav", "Arm",                "Ita", [pstimdict["pos10.jpg"], pstimdict["pos20.jpg"], pstimdict["pos30.jpg"], pstimdict["pos40.jpg"]], [pstimdict["neg10.jpg"], pstimdict["neg20.jpg"], pstimdict["neg30.jpg"], pstimdict["neg40.jpg"]]),
    #             Filename,    Description,                 Lang,  Compatible positive picture stimuli,                                                              Compatible negative picture stimuli
    AudioStimulus("Ita21.wav", "Church",                      "Ita", [pstimdict["pos01.jpg"], pstimdict["pos11.jpg"], pstimdict["pos21.jpg"], pstimdict["pos31.jpg"]], [pstimdict["neg01.jpg"], pstimdict["neg11.jpg"], pstimdict["neg21.jpg"], pstimdict["neg31.jpg"]]),
    AudioStimulus("Ita22.wav", "Vase/Jar",    "Ita", [pstimdict["pos02.jpg"], pstimdict["pos12.jpg"], pstimdict["pos22.jpg"], pstimdict["pos32.jpg"]], [pstimdict["neg02.jpg"], pstimdict["neg12.jpg"], pstimdict["neg22.jpg"], pstimdict["neg32.jpg"]]),
    AudioStimulus("Ita23.wav", "Wind",            "Ita", [pstimdict["pos03.jpg"], pstimdict["pos13.jpg"], pstimdict["pos23.jpg"], pstimdict["pos33.jpg"]], [pstimdict["neg03.jpg"], pstimdict["neg13.jpg"], pstimdict["neg23.jpg"], pstimdict["neg33.jpg"]]),
    AudioStimulus("Ita24.wav", "Soup",                       "Ita", [pstimdict["pos04.jpg"], pstimdict["pos14.jpg"], pstimdict["pos24.jpg"], pstimdict["pos34.jpg"]], [pstimdict["neg04.jpg"], pstimdict["neg14.jpg"], pstimdict["neg24.jpg"], pstimdict["neg34.jpg"]]),
    AudioStimulus("Ita25.wav", "Oil",                      "Ita", [pstimdict["pos05.jpg"], pstimdict["pos15.jpg"], pstimdict["pos25.jpg"], pstimdict["pos35.jpg"]], [pstimdict["neg05.jpg"], pstimdict["neg15.jpg"], pstimdict["neg25.jpg"], pstimdict["neg35.jpg"]]),
    AudioStimulus("Ita26.wav", "Bath/Bathroom/Toilet",                    "Ita", [pstimdict["pos06.jpg"], pstimdict["pos16.jpg"], pstimdict["pos26.jpg"], pstimdict["pos36.jpg"]], [pstimdict["neg06.jpg"], pstimdict["neg16.jpg"], pstimdict["neg26.jpg"], pstimdict["neg36.jpg"]]),
    AudioStimulus("Ita27.wav", "Valley",                "Ita", [pstimdict["pos07.jpg"], pstimdict["pos17.jpg"], pstimdict["pos27.jpg"], pstimdict["pos37.jpg"]], [pstimdict["neg07.jpg"], pstimdict["neg17.jpg"], pstimdict["neg27.jpg"], pstimdict["neg37.jpg"]]),
    AudioStimulus("Ita28.wav", "Ray/Radius",                  "Ita", [pstimdict["pos08.jpg"], pstimdict["pos18.jpg"], pstimdict["pos28.jpg"], pstimdict["pos38.jpg"]], [pstimdict["neg08.jpg"], pstimdict["neg18.jpg"], pstimdict["neg28.jpg"], pstimdict["neg38.jpg"]]),
    AudioStimulus("Ita29.wav", "Ditch",            "Ita", [pstimdict["pos09.jpg"], pstimdict["pos19.jpg"], pstimdict["pos29.jpg"], pstimdict["pos39.jpg"]], [pstimdict["neg09.jpg"], pstimdict["neg19.jpg"], pstimdict["neg29.jpg"], pstimdict["neg39.jpg"]]),
    AudioStimulus("Ita30.wav", "Field",                     "Ita", [pstimdict["pos10.jpg"], pstimdict["pos20.jpg"], pstimdict["pos30.jpg"], pstimdict["pos40.jpg"]], [pstimdict["neg10.jpg"], pstimdict["neg20.jpg"], pstimdict["neg30.jpg"], pstimdict["neg40.jpg"]]),
    #             Filename,    Description,                 Lang,  Compatible positive picture stimuli,                                                              Compatible negative picture stimuli
    AudioStimulus("Ita31.wav", "Beak",          "Ita", [pstimdict["pos01.jpg"], pstimdict["pos11.jpg"], pstimdict["pos21.jpg"], pstimdict["pos31.jpg"]], [pstimdict["neg01.jpg"], pstimdict["neg11.jpg"], pstimdict["neg21.jpg"], pstimdict["neg31.jpg"]]),
    AudioStimulus("Ita32.wav", "Lift",                      "Ita", [pstimdict["pos02.jpg"], pstimdict["pos12.jpg"], pstimdict["pos22.jpg"], pstimdict["pos32.jpg"]], [pstimdict["neg02.jpg"], pstimdict["neg12.jpg"], pstimdict["neg22.jpg"], pstimdict["neg32.jpg"]]),
    AudioStimulus("Ita33.wav", "Stage",                     "Ita", [pstimdict["pos03.jpg"], pstimdict["pos13.jpg"], pstimdict["pos23.jpg"], pstimdict["pos33.jpg"]], [pstimdict["neg03.jpg"], pstimdict["neg13.jpg"], pstimdict["neg23.jpg"], pstimdict["neg33.jpg"]]),
    AudioStimulus("Ita34.wav", "Part",                      "Ita", [pstimdict["pos04.jpg"], pstimdict["pos14.jpg"], pstimdict["pos24.jpg"], pstimdict["pos34.jpg"]], [pstimdict["neg04.jpg"], pstimdict["neg14.jpg"], pstimdict["neg24.jpg"], pstimdict["neg34.jpg"]]),
    AudioStimulus("Ita35.wav", "Patience",                  "Ita", [pstimdict["pos05.jpg"], pstimdict["pos15.jpg"], pstimdict["pos25.jpg"], pstimdict["pos35.jpg"]], [pstimdict["neg05.jpg"], pstimdict["neg15.jpg"], pstimdict["neg25.jpg"], pstimdict["neg35.jpg"]]),
    AudioStimulus("Ita36.wav", "Zone",                      "Ita", [pstimdict["pos06.jpg"], pstimdict["pos16.jpg"], pstimdict["pos26.jpg"], pstimdict["pos36.jpg"]], [pstimdict["neg06.jpg"], pstimdict["neg16.jpg"], pstimdict["neg26.jpg"], pstimdict["neg36.jpg"]]),
    AudioStimulus("Ita37.wav", "Mask",                      "Ita", [pstimdict["pos07.jpg"], pstimdict["pos17.jpg"], pstimdict["pos27.jpg"], pstimdict["pos37.jpg"]], [pstimdict["neg07.jpg"], pstimdict["neg17.jpg"], pstimdict["neg27.jpg"], pstimdict["neg37.jpg"]]),
    AudioStimulus("Ita38.wav", "Entryway",                  "Ita", [pstimdict["pos08.jpg"], pstimdict["pos18.jpg"], pstimdict["pos28.jpg"], pstimdict["pos38.jpg"]], [pstimdict["neg08.jpg"], pstimdict["neg18.jpg"], pstimdict["neg28.jpg"], pstimdict["neg38.jpg"]]),
    AudioStimulus("Ita39.wav", "Access",                    "Ita", [pstimdict["pos09.jpg"], pstimdict["pos19.jpg"], pstimdict["pos29.jpg"], pstimdict["pos39.jpg"]], [pstimdict["neg09.jpg"], pstimdict["neg19.jpg"], pstimdict["neg29.jpg"], pstimdict["neg39.jpg"]]),
    AudioStimulus("Ita40.wav", "Step",                      "Ita", [pstimdict["pos10.jpg"], pstimdict["pos20.jpg"], pstimdict["pos30.jpg"], pstimdict["pos40.jpg"]], [pstimdict["neg10.jpg"], pstimdict["neg20.jpg"], pstimdict["neg30.jpg"], pstimdict["neg40.jpg"]]),
    # MOSELLE-FRANCONIAN AUDIO STIMULI
    #             Filename,    Description,                 Lang,  Compatible positive picture stimuli,                                                              Compatible negative picture stimuli
    AudioStimulus("Lmo01.wav", "Midday/Noon",               "Lmo", [pstimdict["pos01.jpg"], pstimdict["pos11.jpg"], pstimdict["pos21.jpg"], pstimdict["pos31.jpg"]], [pstimdict["neg01.jpg"], pstimdict["neg11.jpg"], pstimdict["neg21.jpg"], pstimdict["neg31.jpg"]]),
    AudioStimulus("Lmo02.wav", "Newspaper",                 "Lmo", [pstimdict["pos02.jpg"], pstimdict["pos12.jpg"], pstimdict["pos22.jpg"], pstimdict["pos32.jpg"]], [pstimdict["neg02.jpg"], pstimdict["neg12.jpg"], pstimdict["neg22.jpg"], pstimdict["neg32.jpg"]]),
    AudioStimulus("Lmo03.wav", "HGV/Lorry",                 "Lmo", [pstimdict["pos03.jpg"], pstimdict["pos13.jpg"], pstimdict["pos23.jpg"], pstimdict["pos33.jpg"]], [pstimdict["neg03.jpg"], pstimdict["neg13.jpg"], pstimdict["neg23.jpg"], pstimdict["neg33.jpg"]]),
    AudioStimulus("Lmo04.wav", "Vegetable",                 "Lmo", [pstimdict["pos04.jpg"], pstimdict["pos14.jpg"], pstimdict["pos24.jpg"], pstimdict["pos34.jpg"]], [pstimdict["neg04.jpg"], pstimdict["neg14.jpg"], pstimdict["neg24.jpg"], pstimdict["neg34.jpg"]]),
    AudioStimulus("Lmo05.wav", "Brother-in-law",            "Lmo", [pstimdict["pos05.jpg"], pstimdict["pos15.jpg"], pstimdict["pos25.jpg"], pstimdict["pos35.jpg"]], [pstimdict["neg05.jpg"], pstimdict["neg15.jpg"], pstimdict["neg25.jpg"], pstimdict["neg35.jpg"]]),
    AudioStimulus("Lmo06.wav", "Fork",                      "Lmo", [pstimdict["pos06.jpg"], pstimdict["pos16.jpg"], pstimdict["pos26.jpg"], pstimdict["pos36.jpg"]], [pstimdict["neg06.jpg"], pstimdict["neg16.jpg"], pstimdict["neg26.jpg"], pstimdict["neg36.jpg"]]),
    AudioStimulus("Lmo07.wav", "Suit",                      "Lmo", [pstimdict["pos07.jpg"], pstimdict["pos17.jpg"], pstimdict["pos27.jpg"], pstimdict["pos37.jpg"]], [pstimdict["neg07.jpg"], pstimdict["neg17.jpg"], pstimdict["neg27.jpg"], pstimdict["neg37.jpg"]]),
    AudioStimulus("Lmo08.wav", "Broom",                     "Lmo", [pstimdict["pos08.jpg"], pstimdict["pos18.jpg"], pstimdict["pos28.jpg"], pstimdict["pos38.jpg"]], [pstimdict["neg08.jpg"], pstimdict["neg18.jpg"], pstimdict["neg28.jpg"], pstimdict["neg38.jpg"]]),
    AudioStimulus("Lmo09.wav", "Bucket",                    "Lmo", [pstimdict["pos09.jpg"], pstimdict["pos19.jpg"], pstimdict["pos29.jpg"], pstimdict["pos39.jpg"]], [pstimdict["neg09.jpg"], pstimdict["neg19.jpg"], pstimdict["neg29.jpg"], pstimdict["neg39.jpg"]]),
    AudioStimulus("Lmo10.wav", "Potato",                    "Lmo", [pstimdict["pos10.jpg"], pstimdict["pos20.jpg"], pstimdict["pos30.jpg"], pstimdict["pos40.jpg"]], [pstimdict["neg10.jpg"], pstimdict["neg20.jpg"], pstimdict["neg30.jpg"], pstimdict["neg40.jpg"]]),
    #             Filename,    Description,                 Lang,  Compatible positive picture stimuli,                                                              Compatible negative picture stimuli
    AudioStimulus("Lmo11.wav", "Apple",                     "Lmo", [pstimdict["pos01.jpg"], pstimdict["pos11.jpg"], pstimdict["pos21.jpg"], pstimdict["pos31.jpg"]], [pstimdict["neg01.jpg"], pstimdict["neg11.jpg"], pstimdict["neg21.jpg"], pstimdict["neg31.jpg"]]),
    AudioStimulus("Lmo12.wav", "Patience",                  "Lmo", [pstimdict["pos02.jpg"], pstimdict["pos12.jpg"], pstimdict["pos22.jpg"], pstimdict["pos32.jpg"]], [pstimdict["neg02.jpg"], pstimdict["neg12.jpg"], pstimdict["neg22.jpg"], pstimdict["neg32.jpg"]]),
    AudioStimulus("Lmo13.wav", "Story/Tale",                "Lmo", [pstimdict["pos03.jpg"], pstimdict["pos13.jpg"], pstimdict["pos23.jpg"], pstimdict["pos33.jpg"]], [pstimdict["neg03.jpg"], pstimdict["neg13.jpg"], pstimdict["neg23.jpg"], pstimdict["neg33.jpg"]]),
    AudioStimulus("Lmo14.wav", "Marble",                    "Lmo", [pstimdict["pos04.jpg"], pstimdict["pos14.jpg"], pstimdict["pos24.jpg"], pstimdict["pos34.jpg"]], [pstimdict["neg04.jpg"], pstimdict["neg14.jpg"], pstimdict["neg24.jpg"], pstimdict["neg34.jpg"]]),
    AudioStimulus("Lmo15.wav", "Pillow(/Kissing)",          "Lmo", [pstimdict["pos05.jpg"], pstimdict["pos15.jpg"], pstimdict["pos25.jpg"], pstimdict["pos35.jpg"]], [pstimdict["neg05.jpg"], pstimdict["neg15.jpg"], pstimdict["neg25.jpg"], pstimdict["neg35.jpg"]]),
    AudioStimulus("Lmo16.wav", "Curtain/Drape(/Garden)",    "Lmo", [pstimdict["pos06.jpg"], pstimdict["pos16.jpg"], pstimdict["pos26.jpg"], pstimdict["pos36.jpg"]], [pstimdict["neg06.jpg"], pstimdict["neg16.jpg"], pstimdict["neg26.jpg"], pstimdict["neg36.jpg"]]),
    AudioStimulus("Lmo17.wav", "Calf",                      "Lmo", [pstimdict["pos07.jpg"], pstimdict["pos17.jpg"], pstimdict["pos27.jpg"], pstimdict["pos37.jpg"]], [pstimdict["neg07.jpg"], pstimdict["neg17.jpg"], pstimdict["neg27.jpg"], pstimdict["neg37.jpg"]]),
    AudioStimulus("Lmo18.wav", "Neighbour",                 "Lmo", [pstimdict["pos08.jpg"], pstimdict["pos18.jpg"], pstimdict["pos28.jpg"], pstimdict["pos38.jpg"]], [pstimdict["neg08.jpg"], pstimdict["neg18.jpg"], pstimdict["neg28.jpg"], pstimdict["neg38.jpg"]]),
    AudioStimulus("Lmo19.wav", "Buttered bread",            "Lmo", [pstimdict["pos09.jpg"], pstimdict["pos19.jpg"], pstimdict["pos29.jpg"], pstimdict["pos39.jpg"]], [pstimdict["neg09.jpg"], pstimdict["neg19.jpg"], pstimdict["neg29.jpg"], pstimdict["neg39.jpg"]]),
    AudioStimulus("Lmo20.wav", "Bird",                      "Lmo", [pstimdict["pos10.jpg"], pstimdict["pos20.jpg"], pstimdict["pos30.jpg"], pstimdict["pos40.jpg"]], [pstimdict["neg10.jpg"], pstimdict["neg20.jpg"], pstimdict["neg30.jpg"], pstimdict["neg40.jpg"]]),
    #             Filename,    Description,                 Lang,  Compatible positive picture stimuli,                                                              Compatible negative picture stimuli
    AudioStimulus("Lmo21.wav", "Attic",                     "Lmo", [pstimdict["pos01.jpg"], pstimdict["pos11.jpg"], pstimdict["pos21.jpg"], pstimdict["pos31.jpg"]], [pstimdict["neg01.jpg"], pstimdict["neg11.jpg"], pstimdict["neg21.jpg"], pstimdict["neg31.jpg"]]),
    AudioStimulus("Lmo22.wav", "Mustard",                   "Lmo", [pstimdict["pos02.jpg"], pstimdict["pos12.jpg"], pstimdict["pos22.jpg"], pstimdict["pos32.jpg"]], [pstimdict["neg02.jpg"], pstimdict["neg12.jpg"], pstimdict["neg22.jpg"], pstimdict["neg32.jpg"]]),
    AudioStimulus("Lmo23.wav", "Belt",                      "Lmo", [pstimdict["pos03.jpg"], pstimdict["pos13.jpg"], pstimdict["pos23.jpg"], pstimdict["pos33.jpg"]], [pstimdict["neg03.jpg"], pstimdict["neg13.jpg"], pstimdict["neg23.jpg"], pstimdict["neg33.jpg"]]),
    AudioStimulus("Lmo24.wav", "Pot",                       "Lmo", [pstimdict["pos04.jpg"], pstimdict["pos14.jpg"], pstimdict["pos24.jpg"], pstimdict["pos34.jpg"]], [pstimdict["neg04.jpg"], pstimdict["neg14.jpg"], pstimdict["neg24.jpg"], pstimdict["neg34.jpg"]]),
    AudioStimulus("Lmo25.wav", "Glass",                     "Lmo", [pstimdict["pos05.jpg"], pstimdict["pos15.jpg"], pstimdict["pos25.jpg"], pstimdict["pos35.jpg"]], [pstimdict["neg05.jpg"], pstimdict["neg15.jpg"], pstimdict["neg25.jpg"], pstimdict["neg35.jpg"]]),
    AudioStimulus("Lmo26.wav", "Hiccup",                    "Lmo", [pstimdict["pos06.jpg"], pstimdict["pos16.jpg"], pstimdict["pos26.jpg"], pstimdict["pos36.jpg"]], [pstimdict["neg06.jpg"], pstimdict["neg16.jpg"], pstimdict["neg26.jpg"], pstimdict["neg36.jpg"]]),
    AudioStimulus("Lmo27.wav", "Shoulder/Pupil",            "Lmo", [pstimdict["pos07.jpg"], pstimdict["pos17.jpg"], pstimdict["pos27.jpg"], pstimdict["pos37.jpg"]], [pstimdict["neg07.jpg"], pstimdict["neg17.jpg"], pstimdict["neg27.jpg"], pstimdict["neg37.jpg"]]),
    AudioStimulus("Lmo28.wav", "Puddle",                    "Lmo", [pstimdict["pos08.jpg"], pstimdict["pos18.jpg"], pstimdict["pos28.jpg"], pstimdict["pos38.jpg"]], [pstimdict["neg08.jpg"], pstimdict["neg18.jpg"], pstimdict["neg28.jpg"], pstimdict["neg38.jpg"]]),
    AudioStimulus("Lmo29.wav", "Household",                 "Lmo", [pstimdict["pos09.jpg"], pstimdict["pos19.jpg"], pstimdict["pos29.jpg"], pstimdict["pos39.jpg"]], [pstimdict["neg09.jpg"], pstimdict["neg19.jpg"], pstimdict["neg29.jpg"], pstimdict["neg39.jpg"]]),
    AudioStimulus("Lmo30.wav", "Plasterer",                 "Lmo", [pstimdict["pos10.jpg"], pstimdict["pos20.jpg"], pstimdict["pos30.jpg"], pstimdict["pos40.jpg"]], [pstimdict["neg10.jpg"], pstimdict["neg20.jpg"], pstimdict["neg30.jpg"], pstimdict["neg40.jpg"]]),
    #             Filename,    Description,                 Lang,  Compatible positive picture stimuli,                                                              Compatible negative picture stimuli
    AudioStimulus("Lmo31.wav", "Coincidence",               "Lmo", [pstimdict["pos01.jpg"], pstimdict["pos11.jpg"], pstimdict["pos21.jpg"], pstimdict["pos31.jpg"]], [pstimdict["neg01.jpg"], pstimdict["neg11.jpg"], pstimdict["neg21.jpg"], pstimdict["neg31.jpg"]]),
    AudioStimulus("Lmo32.wav", "Hill/Bump/Planer",          "Lmo", [pstimdict["pos02.jpg"], pstimdict["pos12.jpg"], pstimdict["pos22.jpg"], pstimdict["pos32.jpg"]], [pstimdict["neg02.jpg"], pstimdict["neg12.jpg"], pstimdict["neg22.jpg"], pstimdict["neg32.jpg"]]),
    AudioStimulus("Lmo33.wav", "Drawer",                    "Lmo", [pstimdict["pos03.jpg"], pstimdict["pos13.jpg"], pstimdict["pos23.jpg"], pstimdict["pos33.jpg"]], [pstimdict["neg03.jpg"], pstimdict["neg13.jpg"], pstimdict["neg23.jpg"], pstimdict["neg33.jpg"]]),
    AudioStimulus("Lmo34.wav", "Half",                      "Lmo", [pstimdict["pos04.jpg"], pstimdict["pos14.jpg"], pstimdict["pos24.jpg"], pstimdict["pos34.jpg"]], [pstimdict["neg04.jpg"], pstimdict["neg14.jpg"], pstimdict["neg24.jpg"], pstimdict["neg34.jpg"]]),
    AudioStimulus("Lmo35.wav", "Foul water kennel",         "Lmo", [pstimdict["pos05.jpg"], pstimdict["pos15.jpg"], pstimdict["pos25.jpg"], pstimdict["pos35.jpg"]], [pstimdict["neg05.jpg"], pstimdict["neg15.jpg"], pstimdict["neg25.jpg"], pstimdict["neg35.jpg"]]),
    AudioStimulus("Lmo36.wav", "Bag",                       "Lmo", [pstimdict["pos06.jpg"], pstimdict["pos16.jpg"], pstimdict["pos26.jpg"], pstimdict["pos36.jpg"]], [pstimdict["neg06.jpg"], pstimdict["neg16.jpg"], pstimdict["neg26.jpg"], pstimdict["neg36.jpg"]]),
    AudioStimulus("Lmo37.wav", "Envelope",                  "Lmo", [pstimdict["pos07.jpg"], pstimdict["pos17.jpg"], pstimdict["pos27.jpg"], pstimdict["pos37.jpg"]], [pstimdict["neg07.jpg"], pstimdict["neg17.jpg"], pstimdict["neg27.jpg"], pstimdict["neg37.jpg"]]),
    AudioStimulus("Lmo38.wav", "Godfather",                 "Lmo", [pstimdict["pos08.jpg"], pstimdict["pos18.jpg"], pstimdict["pos28.jpg"], pstimdict["pos38.jpg"]], [pstimdict["neg08.jpg"], pstimdict["neg18.jpg"], pstimdict["neg28.jpg"], pstimdict["neg38.jpg"]]),
    AudioStimulus("Lmo39.wav", "Carpenter",                 "Lmo", [pstimdict["pos09.jpg"], pstimdict["pos19.jpg"], pstimdict["pos29.jpg"], pstimdict["pos39.jpg"]], [pstimdict["neg09.jpg"], pstimdict["neg19.jpg"], pstimdict["neg29.jpg"], pstimdict["neg39.jpg"]]),
    AudioStimulus("Lmo40.wav", "Arm",                       "Lmo", [pstimdict["pos10.jpg"], pstimdict["pos20.jpg"], pstimdict["pos30.jpg"], pstimdict["pos40.jpg"]], [pstimdict["neg10.jpg"], pstimdict["neg20.jpg"], pstimdict["neg30.jpg"], pstimdict["neg40.jpg"]]),
]

astimdict: dict[str, AudioStimulus] = {
    stim.filename: stim for stim in astimlist
}
