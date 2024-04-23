
import itertools

Ingredients = ["Mushroom","Sprout","Toad","Talon","Orchid","Root","Scorpion","Feather"]
#Alchemicals formatted as Red, Green, Blue
Alchemicals = [[-1, 1, -1],[1, -1, 1],[1, -1, -1],[-1, 1, 1],[-1, -1, 1],[1, 1, -1],[-1, -1, -1],[1, 1, 1]]

def PromptForFact(Facts):
    # Mix Potion : Two Ingredients and one result value
    # Sell Potion : Two Ingredients and one to three result values
    # Debunk: One Ingredient and one result value
    # Periscope: One Ingredient and one result value
    GetType = input("Enter type of information: Mix Potion, Sell Potion, Debunk, or Periscope.")
    if GetType == "Mix Potion" :
        GetMixPotionInput(Facts)
    if GetType == "Sell Potion" :
        GetSellPotionInput(Facts)
    if GetType == "Debunk" :
        GetDebunkInput(Facts)
    if GetType == "Periscope":
        GetPeriscopeInput(Facts)

def GetMixPotionInput(Facts):
    Ingredient1 = input("Enter the first ingredient used:")
    Ingredient2 = input("Enter the second ingredient used:")
    PotionInput = input("Enter the potion as three numbers for Red, Green, and Blue (such as '-1 0 0')")
    PotionSplit = PotionInput.split()
    PotionToAdd = []
    for value in PotionSplit:
        PotionToAdd.append(int(value))
    Facts["Mix Potion"].append([Ingredient1,Ingredient2,PotionToAdd])

def GetSellPotionInput(Facts):
    Ingredient1 = input("Enter the first ingredient used:")
    Ingredient2 = input("Enter the second ingredient used:")
    PotionInput = input("Enter the result as three numbers for Red, Green, and Blue (such as '-1 -1 -1')")
    PotionSplit = PotionInput.split()
    PotionSplitInt = []
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
    # Mix Potion, Sell Potion, Debunk, Periscope
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

