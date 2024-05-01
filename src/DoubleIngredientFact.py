'''
Subclass of Fact. Contains two ingredients. 

Factcheck method takes in an assignmentSet and returns True / False on whether it is compatible with that instance.

# DO I EVEN NEED THE FACTS TO BE DIFFERENT? 

'''
from Fact import Fact

class DoubleIngredientFact(Fact):

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