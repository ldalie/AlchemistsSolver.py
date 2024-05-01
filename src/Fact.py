'''
Abstract super class to implement subclasses. 

Has attributes for ingredients and alchemicals. 

Fact
  ┃--SingleIngredientFact
  ┃          
  ┃--DoubleIngredientFact
            ┃
            ┃--MixPotion
            ┃
            ┃--SellPotion <--MAYBE DONT NEED THIS LAYER? OR EVEN THE LAYER ABOVE THAT???


'''

class Fact(object):
    def __init__(self,ingredients,alchemicals):
        # add an assert?
        self.ingredients = ingredients
        self.alchemicals = alchemicals
    
    def __str__(self):
        return str("< ",self.ingredients," ,",self.alchemicals," >")

    def getIngredients(self):
        return self.ingredients.copy()

    def getAlchemicals(self):
        return self.alchemicals.copy()
    
