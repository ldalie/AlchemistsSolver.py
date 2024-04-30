
import itertools

ingredients = ["Mushroom","Sprout","Toad","Talon","Orchid","Root","Scorpion","Feather"]
#alchemicals formatted as Red, Green, Blue
alchemicals = [[-1, 1, -1],[1, -1, 1],[1, -1, -1],[-1, 1, 1],[-1, -1, 1],[1, 1, -1],[-1, -1, -1],[1, 1, 1]]

class Fact:
    # Create instance with attributes containing a list of relevant alchemicals and a list of relevent ingredients
    def __init__(self,factualAlchemicals,factualIngredients):
        self.factualAlchemicals = factualAlchemicals
        self.factualIngredients = factualIngredients

class MixPotionFact(Fact):
    def __str__(self):
        return str(self.factualAlchemicals)

    def FactCheck(self,assignmentSet):
        MixedIngredients = [self.factualIngredients[0],self.factualIngredients[1]]
        factualResult = self.factualAlchemicals[0]

        assignedAlchemicals = []
        for ingredient in MixedIngredients: 
            assignedAlchemicals.append(assignmentSet[ingredient])
        assignedResult = MixPotion(assignedAlchemicals[0],assignedAlchemicals[1])

        return (assignedResult == factualResult)
    



# Prompt the user for input on the type of information
def promptForFact(facts):
    getType = input("Enter type of information: Mix Potion (1), Sell Potion (2), or Debunk (3).")
    if getType == "Mix Potion" or getType == "1" :
        getMixPotionInput(facts)
    if getType == "Sell Potion" or getType == "2" :
        getSellPotionInput(facts)
    if getType == "Debunk" or getType == "3":
        getDebunkInput(facts)

    # if getType == "Periscope" or "4":
    #     getPeriscopeInput(facts) 

# Get input for mixed potions. Add a Mixed Potion fact to fact with both ingredients and the potion as a list of three integers
def getMixPotionInput(facts):
    ingredient1 = input("Enter the first ingredient used:")
    ingredient2 = input("Enter the second ingredient used:")
    potionInput = input("Enter the potion as three numbers for Red, Green, and Blue (such as '-1 0 0')")
    potionSplitInt = [int(v) for v in potionInput.split()]
    facts["Mix Potion"].append([ingredient1,ingredient2,potionSplitInt])

def getSellPotionInput(facts):
    ingredient1 = input("Enter the first ingredient used:")
    ingredient2 = input("Enter the second ingredient used:")
    potionInput = input("Enter the result as three numbers for Red, Green, and Blue (such as '-1 -1 -1')")
    potionSplitInt = [int(v) for v in potionInput.split()]
    potionsToAdd = []    
    for index in range(len(potionSplitInt)):
        potion =[0,0,0]
        if potionSplitInt[index] != 0:
            potion[index] = potionSplitInt[index]
            potionsToAdd.append(potion)
    # Add special case
    facts["Sell Potion"].append([ingredient1,ingredient2,potionsToAdd])

def getDebunkInput(facts):
    ingredient = input("Enter the ingredient that's been debunked:")
    componentInput = input("Enter the true component's value as three numbers for Red, Green, and Blue (such as '0 1 0'):")
    componentSplit = componentInput.split()
    componentOutput = []
    for component in componentSplit:
        componentOutput.append(int(component))
    facts["Debunk"].append([ingredient,componentOutput])

def permutate(ingredients,alchemicals):
    uniqueCombinations = []
    ingredientPermutations = itertools.permutations(ingredients,len(alchemicals))
   
    for perm in ingredientPermutations:
        assignmentSet = {}
        for i in range(len(perm)):
            assignmentSet[perm[i]] = alchemicals [i]
        uniqueCombinations.append(assignmentSet)       
    
    return uniqueCombinations

def factCheckAssignments(allAssignments,facts):
    possibleAssignments = []
    for assignmentSet in allAssignments:
        ExperimentTracker = []
        for experiment in facts["Mix Potion"]:
            experimentBoolean = FactCheckMixPotion(assignmentSet,experiment)
            ExperimentTracker.append(experimentBoolean)

        for experiment in facts["Sell Potion"]:
            experimentBoolean = FactCheckSellPotion(assignmentSet,experiment)
            ExperimentTracker.append(experimentBoolean)

        for debunking in facts["Debunk"]:
            debunkingBoolean = FactCheckDebunk(assignmentSet,debunking)
            ExperimentTracker.append(debunkingBoolean)

        if all(ExperimentTracker):
            possibleAssignments.append(assignmentSet)

    return possibleAssignments

def FactCheckMixPotion(assignmentSet,experiment):
    MixedIngredients = [experiment[0],experiment[1]]
    factualResult = experiment[2]

    assignedAlchemicals = []
    for ingredient in MixedIngredients: 
        assignedAlchemicals.append(assignmentSet[ingredient])
    assignedResult = MixPotion(assignedAlchemicals[0],assignedAlchemicals[1])

    return (assignedResult == factualResult)

def FactCheckSellPotion(assignmentSet,experiment):
    MixedIngredients = [experiment[0],experiment[1]]

    assignedAlchemicals = []
    for ingredient in MixedIngredients:
        assignedAlchemicals.append(assignmentSet[ingredient])
    assignedResult = MixPotion(assignedAlchemicals[0],assignedAlchemicals[1])

    SubExperimentTracker = []
    for factualResult in experiment[2]:
        if assignedResult == factualResult:
            SubExperimentTracker.append(True)
    if any(SubExperimentTracker):
        return True
    else:
        return False

def FactCheckDebunk(assignmentSet,debunking):
    ingredient = debunking[0]
    factualComponent = debunking[1]
    assignedAlchemical = assignmentSet[ingredient]
    for index in range(len(factualComponent)):
        if factualComponent[index] != 0:
            if factualComponent[index] == assignedAlchemical[index] :
                return True
            else:
                return False

def MixPotion(alchemical1,Alchemical2):
    Result = []
    for i in range(len(alchemical1)) :
        if alchemical1[i] == Alchemical2[i] :
            Result.append(alchemical1[i])
        else: Result.append(0)
    # Neutral
    if Result == [0,0,0] :
        return Result
    # Single match
    if len([component for component in Result if component != 0]) == 1:
        return Result
    # Doublematch 
    else:
        prioritizedIndex = Result.index(0)-1
        prioritizedResult = [0,0,0]
        prioritizedResult[prioritizedIndex] = Result[prioritizedIndex]
        return prioritizedResult

def assignmentCounter(ingredients,alchemicals,possibleAssignments):
    assignmentCount = createEmptyMap(ingredients,alchemicals)
    for assignmentSet in possibleAssignments:
        for ingredient in assignmentSet:
            assignedAlchemicalKey = str(assignmentSet[ingredient])
            assignmentCount[ingredient][assignedAlchemicalKey] += 1
    return assignmentCount

def createEmptyMap(ingredients,alchemicals):
    allIngredientMap = {}
    for ingredient in ingredients:
        singleIngredientMap = {}
        for alchemical in alchemicals:
            singleIngredientMap[str(alchemical)] = 0
        allIngredientMap[ingredient] = singleIngredientMap
    return allIngredientMap

def assignmentCountToProbability(assignmentCount):
    assignmentProbabilities = assignmentCount.copy()
    for ingredient in assignmentProbabilities:
        totalCount = 0
        for alchemical in assignmentProbabilities[ingredient]:
            totalCount += assignmentProbabilities[ingredient][alchemical]
        for alchemical in assignmentProbabilities[ingredient]:
            assignmentProbabilities[ingredient][alchemical] /= totalCount
    return assignmentProbabilities

def printProbabilityMapping(ingredients,alchemicals,assignmentProbabilities):
    print("\n      ")
    topLine = '               '
    for ingredient in ingredients:
        topLine += str.ljust(ingredient,15," ")
    print(topLine)
    for alchemical in alchemicals:
        alchemical = str(alchemical)
        alchemicalLine = str.ljust(alchemical,15," ")
        for ingredient in ingredients:
            alchemicalProbability = str(int(100*(assignmentProbabilities[ingredient][str(alchemical)])))
            alchemicalLine += str.ljust(alchemicalProbability,15," ")
        print(alchemicalLine)

def main():
    facts = {"Mix Potion":[],"Sell Potion":[],"Debunk":[],"Periscope":[]}
    allAssignments = permutate(ingredients,alchemicals)
    while True:
        promptForFact(facts)
        possibleAssignments = factCheckAssignments(allAssignments,facts)
        assignmentCount = assignmentCounter(ingredients,alchemicals,possibleAssignments)
        assignmentProbabilities = assignmentCountToProbability(assignmentCount)
        printProbabilityMapping(ingredients,alchemicals,assignmentProbabilities)


# main()



