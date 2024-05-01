'''
Subclass of Fact. Contains one ingredient. 

Factcheck method takes in an assignmentSet and returns True / False on whether it is compatible with that instance. 
'''
from Fact import Fact

class SingleIngredientFact(Fact):

    def FactCheck(self,assignmentSet):
        factIndexesAndValues = {}
        for i, value in enumerate(self.alchemicals):
            if value != 0:
                factIndexesAndValues[i] = value

        assignmentAlchemical = []
        for ingredient in self.ingredients:
            assignmentAlchemical.append(assignmentSet['assignments'][ingredient])

        checkList = []
        for alchemicalFact in factIndexesAndValues:
            checkList.append(assignmentAlchemical[i] == alchemicalFact[i])

        return any(checkList)
        
        
