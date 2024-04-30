'''
Create a list of all permutations of alchemicals.

Enter while loop that stops when all alchemicals are determined.

Take in a fact from a user. 

Check each permutation against each fact, and return a new list with all possible permutations. 

Display those possible permutations in a grid resembling the player board. 

'''
from CONSTANTS import ALL_INGREDIENTS,ALL_ALCHEMICALS
from buildAllAssignmentSets import buildAllAssignmentSets

def main():
    Facts = []
    # return all possible assignment sets, each with a multiplier of 1.
    possibleAssignmentSets = buildAllAssignmentSets(ALL_ALCHEMICALS,ALL_INGREDIENTS)
    # initiate loop that will end once the entire board is known.
    while isBoardNotComplete:
        # prompt user for new fact. add that fact to Facts list. 
        getFactFromUser(Facts,ALL_ALCHEMICALS,ALL_INGREDIENTS)
        # check each alchemical permutation in the list of possiblePermutations against each fact. filter out impossible permutations.
        factCheckPermutations(Facts,possiblePermutations)
        # take in the list of possible permutations. return list of dictionaries containing the probability for each ingredient-alchemical assignemnt.
        assignmentProbabilities = calculateAssignmentProbabilities(ALL_INGREDIENTS,possiblePermutations)
        # display the probability of each ingredient-alchemical assignment as grid to user.
        displayProbabilities(assignmentProbabilities)
        # check if the all ingredient-achemical assignments are known.
        isBoardNotComplete = checkForCompletedBoard(assignmentProbailities)



