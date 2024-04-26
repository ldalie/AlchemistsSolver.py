
import itertools

Ingredients = ["Mushroom","Sprout","Toad","Talon","Orchid","Root","Scorpion","Feather"]
#Alchemicals formatted as Red, Green, Blue
Alchemicals = [[-1, 1, -1],[1, -1, 1],[1, -1, -1],[-1, 1, 1],[-1, -1, 1],[1, 1, -1],[-1, -1, -1],[1, 1, 1]]


# ------ would love a one sentence description above each function definition
# ------ explaining what the function is doing !
def PromptForFact(Facts):
    # ------ put each of these comments under their corresponding branch instead
    # Mix Potion : Two Ingredients and one result value
    # Sell Potion : Two Ingredients and one to three result values
    # Debunk: One Ingredient and one result value
    # Periscope: One Ingredient and one result value
    
    # ------ for user inputs its usually better to let them type in full string or a number
    # ------ something like "Enter type of information: Mix Potion (1), Sell Potion (2), Debunk (3), or Periscope (4)"
    GetType = input("Enter type of information: Mix Potion, Sell Potion, Debunk, or Periscope.")
    if GetType == "Mix Potion" :
        GetMixPotionInput(Facts)
    if GetType == "Sell Potion" :
        GetSellPotionInput(Facts)
    if GetType == "Debunk" :
        GetDebunkInput(Facts)
    if GetType == "Periscope":
        GetPeriscopeInput(Facts) # ------ this function is not defined?

def GetMixPotionInput(Facts):
    # ------ these 4 lines are the exact same as the ones in GetSellPotionInput
    # ------ worth considering how you can abstract these into its own lil helper function
    Ingredient1 = input("Enter the first ingredient used:")
    Ingredient2 = input("Enter the second ingredient used:")
    # ------ line below should probably tell you what numbers correspond to each color
    # ------ "Enter the potion as three numbers for Red (-1), Green (0), and Blue (1)" OR
    # ------ users to input a letter instead ("R" "G" "B") and you map it to the correct # in code
    PotionInput = input("Enter the potion as three numbers for Red, Green, and Blue (such as '-1 0 0')")
    PotionSplit = PotionInput.split()
    PotionToAdd = []
    # ------ can be done inline, also done in below function, could abstract
    for value in PotionSplit:
        PotionToAdd.append(int(value))
    Facts["Mix Potion"].append([Ingredient1,Ingredient2,PotionToAdd])

def GetSellPotionInput(Facts):
    # ------ see comment in previous function
    Ingredient1 = input("Enter the first ingredient used:")
    Ingredient2 = input("Enter the second ingredient used:")
    PotionInput = input("Enter the result as three numbers for Red, Green, and Blue (such as '-1 -1 -1')")
    PotionSplit = PotionInput.split()
    PotionSplitInt = []
    # ------ can be done inline
    for value in PotionSplit:
        PotionSplitInt.append(int(value))
    PotionsToAdd = []    
    for index in range(len(PotionSplitInt)):
        Potion =[0,0,0]
        if PotionSplitInt[index] != 0:
            Potion[index] = PotionSplitInt[index]
            PotionsToAdd.append(Potion)
    Facts["Sell Potion"].append([Ingredient1,Ingredient2,PotionsToAdd])

def GetDebunkInput(Facts):
    Ingredient = input("Enter the ingredient that's been debunked:")
    # ------ see prior comment
    ComponentInput = input("Enter the true component's value as three numbers for Red, Green, and Blue (such as '0 1 0'):")
    ComponentSplit = ComponentInput.split()
    ComponentOutput = []
    for component in ComponentSplit:
        ComponentOutput.append(int(component))
    Facts["Debunk"].append([Ingredient,ComponentOutput])

def permutate(Ingredients,Alchemicals):
    UniqueCombinations = []
    IngredientPermutations = itertools.permutations(Ingredients,len(Alchemicals))
   
    for perm in IngredientPermutations:
        AssignmentSet = {}
        for i in range(len(perm)):
            AssignmentSet[perm[i]] = Alchemicals [i]
        UniqueCombinations.append(AssignmentSet)       
    
    return UniqueCombinations

def FactCheckAssignments(AllAssignments,Facts):
    # ------ function is very long
    # ------ probably worth rbeaking up the internal for loops out into their own functions
    # ------ eg: lines 93-105 would be its own function
    PossibleAssignments = []
    for AssignmentSet in AllAssignments:
        ExperimentTracker = []
        for experiment in Facts["Mix Potion"]:
            MixedIngredients = [experiment[0],experiment[1]]
            FactualResult = experiment[2]

            AssignedAlchemicals = []
            for ingredient in MixedIngredients: 
                AssignedAlchemicals.append(AssignmentSet[ingredient])
            AssignedResult = MixPotion(AssignedAlchemicals[0],AssignedAlchemicals[1])

            if AssignedResult == FactualResult:
                ExperimentTracker.append(True)
            else:
                ExperimentTracker.append(False)
        for experiment in Facts["Sell Potion"]:
            MixedIngredients = [experiment[0],experiment[1]]

            AssignedAlchemicals = []
            for ingredient in MixedIngredients:
                AssignedAlchemicals.append(AssignmentSet[ingredient])
            AssignedResult = MixPotion(AssignedAlchemicals[0],AssignedAlchemicals[1])

            SubExperimentTracker = []
            for FactualResult in experiment[2]:
                if AssignedResult == FactualResult:
                    SubExperimentTracker.append(True)
            if any(SubExperimentTracker):
                ExperimentTracker.append(True)
            else:
                ExperimentTracker.append(False)

        for debunking in Facts["Debunk"]:
            Ingredient = debunking[0]
            FactualComponent = debunking[1]
            AssignedAlchemical = AssignmentSet[Ingredient]
            for index in range(len(FactualComponent)):
                if FactualComponent[index] != 0:
                    if FactualComponent[index] == AssignedAlchemical[index] :
                        ExperimentTracker.append(True)
                    else:
                        ExperimentTracker.append(False)
        
        # for periscoping in 

        if all(ExperimentTracker):
            PossibleAssignments.append(AssignmentSet)
    return PossibleAssignments

def MixPotion(Alchemical1,Alchemical2):
    Result = []
    for i in range(len(Alchemical1)) :
        if Alchemical1[i] == Alchemical2[i] :
            Result.append(Alchemical1[i])
        else: Result.append(0)
    # Neutral
    if Result == [0,0,0] :
        return Result
    # Single match
    if len([component for component in Result if component != 0]) == 1:
        return Result
    # Doublematch 
    else:
        PrioritizedIndex = Result.index(0)-1
        PrioritizedResult = [0,0,0]
        PrioritizedResult[PrioritizedIndex] = Result[PrioritizedIndex]
        return PrioritizedResult

def AssignmentCounter(Ingredients,Alchemicals,PossibleAssignments):
    AssignmentCount = CreateEmptyMap(Ingredients,Alchemicals)
    for AssignmentSet in PossibleAssignments:
        for Ingredient in AssignmentSet:
            AssignedAlchemicalKey = str(AssignmentSet[Ingredient])
            AssignmentCount[Ingredient][AssignedAlchemicalKey] += 1
    return AssignmentCount

def CreateEmptyMap(Ingredients,Alchemicals):
    AllIngredientMap = {}
    for Ingredient in Ingredients:
        SingleIngredientMap = {}
        for Alchemical in Alchemicals:
            SingleIngredientMap[str(Alchemical)] = 0
        AllIngredientMap[Ingredient] = SingleIngredientMap
    return AllIngredientMap

def AssignmentCountToProbability(AssignmentCount):
    AssignmentProbabilities = AssignmentCount
    for Ingredient in AssignmentProbabilities:
        TotalCount = 0
        for Alchemical in AssignmentProbabilities[Ingredient]:
            TotalCount += AssignmentProbabilities[Ingredient][Alchemical]
        for Alchemical in AssignmentProbabilities[Ingredient]:
            AssignmentProbabilities[Ingredient][Alchemical] /= TotalCount
    return AssignmentProbabilities

def PrintProbabilityMapping(Ingredients,Alchemicals,AssignmentProbabilities):
    print("\n      ")
    TopLine = '               '
    for Ingredient in Ingredients:
        TopLine += str.ljust(Ingredient,15," ")
    print(TopLine)
    for Alchemical in Alchemicals:
        Alchemical = str(Alchemical)
        AlchemicalLine = str.ljust(Alchemical,15," ")
        for Ingredient in Ingredients:
            AlchemicalProbability = str(int(100*(AssignmentProbabilities[Ingredient][str(Alchemical)])))
            AlchemicalLine += str.ljust(AlchemicalProbability,15," ")
        print(AlchemicalLine)

def main():
    Facts = {"Mix Potion":[],"Sell Potion":[],"Debunk":[],"Periscope":[]}
    AllAssignments = permutate(Ingredients,Alchemicals)
    while True:
        PromptForFact(Facts)
        PossibleAssignments = FactCheckAssignments(AllAssignments,Facts)
        AssignmentCount = AssignmentCounter(Ingredients,Alchemicals,PossibleAssignments)
        AssignmentProbabilities = AssignmentCountToProbability(AssignmentCount)
        PrintProbabilityMapping(Ingredients,Alchemicals,AssignmentProbabilities)


main()

