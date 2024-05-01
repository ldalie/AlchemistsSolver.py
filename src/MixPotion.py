''''
Takes in two alchemicals and returns their restult.
'''

def MixPotion(alchemical1,alchemical2):
    result = []

    for i in range(len(alchemical1)):
        if alchemical1[i] == alchemical2[i]:
            result.append(alchemical1[i])
        else: result.append(0)
    
    # neutral or single match
    if len([component for component in result if component != 0]) < 2:
        return result
    
    else:
        prioritizedIndex = result.index(0)-1
        prioritizedResult = [0,0,0]
        prioritizedResult[prioritizedIndex] = result[prioritizedIndex]
        return prioritizedResult

