def calculateOldLove(name1, name2):
    """Return the love % between two given names
    Parameters:
        name1 (string): a name
        name2 (string): a name
    Return:
        int: the percentage of love
    """

    lengthN1 = len(name1)
    lengthN2 = len(name2)
    result = abs(lengthN1 - lengthN2)

    if result <= 2:
        return "20 % match"
    elif result <= 4:
        return "40 % match"
    elif result <= 6:
        return "60 % match"
    elif result <= 8:
        return "80 % match"
    elif result <= 10:
        return "1000 % match"
    else:
        return "hopeless case"
    

from difflib import SequenceMatcher
def calculateTrueLove(name1, name2):
    """Calculates the true love percentage between two given names
    Parameters:
        name1 (string): a name
        name2 (string): a name
    Return:
        string: the love percentage
    """
    result = round(SequenceMatcher(None,name1, name2).ratio()*100,0)
    return str(result) + "% match"