'''
Takes in the lists of all alchemicals and all ingredients from constants.

Generates a list of all permutations of assignments of alchemicals to ingredients. Each starts with a multiplier of 1. 

buildAllAssignmentSets: () => 
[
    {
        "multiplier": 1,
        "assignments": [
            { "Mushroom" : [-1,1,1] },
            { "Toad" : [1,-1,1] },
            ...
            ]

    }
    ...
]
'''

from CONSTANTS import ALL_ALCHEMICALS , ALL_INGREDIENTS
import itertools

# build a list of all possible permutations of the eight alchemicals. len should be 40320. 
# build a list of dictionaries assigning each ingredient to each alchemical for each iteration. 
# each assignment set comes with a multiplier value to be used when calculating the probability in the case of periscoping a mixed result sold potion. 
def buildAllAssignmentSets():

    allAlchemicalPermutations = list(itertools.permutations(ALL_ALCHEMICALS))
    
    allAssignmentSets = []

    for alchemicalPermutation in allAlchemicalPermutations:
        assignmentSet = dict()
        assignmentSet["multiplier"] = 1
        assignmentSet["assignments"] = []

        for i in range(len(ALL_INGREDIENTS)):
            assignment = dict()
            assignment[ALL_INGREDIENTS[i]] = alchemicalPermutation[i]
            assignmentSet["assignments"].append(assignment)

        allAssignmentSets.append(assignmentSet)
    
    return allAssignmentSets
