'''
Takes in the lists of all alchemicals and all ingredients from constants.

Generates a list of all permutations of the list of alchemicals.

Returns a list of dictionaries that contains (a) a dictionary with ingredients as keys and an alchemical as their value, 
and (b) their assignment multiplier.

eg.:
allAssignmentPermutations = [
    {"assignmentSet":[
        {"Mushroom" : [-1,1,1]}
        {"Toad" : [1,-1,1]}
        ....
        ]
    },
    {"Multiplier": 1}
]


'''
from CONSTANTS import ALL_ALCHEMICALS , ALL_INGREDIENTS
import itertools

# build a list of all possible permutations of the eight alchemicals. should be about 40k long. 
def buildAllAlchemicalPermutatoins(ALL_ALCHEMICALS):
    allAlchemPerm = list(itertools.permutations(ALL_ALCHEMICALS))
    
    return allAlchemPerm

# build a list of dictionaries assigning each ingredient to each alchemical for each iteration. 
# each assignment set comes with a multiplier value to be used when calculating the probability in the case of periscoping a mixed result sold potion. 
def genAllAssignmentPerm(ALL_ALCHEMICALS):

    for alchemicalSet in allAlchemPerm:
        for ingredient in ALL_INGREDIENTS:
            setDict = dict()
            setDict[ingredient]

def buildAllAssignmentPerm():
    pass
    