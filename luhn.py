# Implementation of Luhn algorithm for checking and generation tail control digit of card number
# https://en.wikipedia.org/wiki/Luhn_algorithm

def calcLuhn(cardNo: str, isCurrentCharEven: bool = False):   # isCurrentCharEven = False for checking, True for calculation Luhn number
    luhnNumber = 0
    for currentChar in cardNo[::-1]:    # Pass from right to left, so reverse cardNo
        currenDigit = ord(currentChar) - ord('0')
        if isCurrentCharEven:
            currenDigit = currenDigit * 2
        luhnNumber = luhnNumber + (currenDigit // 10)
        luhnNumber = luhnNumber + (currenDigit %  10)
        isCurrentCharEven = not isCurrentCharEven
        
    luhnNumber = luhnNumber % 10
    if luhnNumber:  
        luhnNumber = 10 - luhnNumber    # Calculate Luhn number for generateLuhn(cardNoWithoutLuhn)
    # If initial isCurrentCharEven == False 
    #     and luhnNumber == 0 then cardNo[-1] is correct Luhn number
    #     else cardNo[-1] is NOT correct Luhn number
    # else luhnNumber is calculated Luhn number
    return luhnNumber   

def checkLuhn(cardNo: str):
    return False if calcLuhn(cardNo) else True

def generateLuhn(cardNoWithoutLuhn: str):
    return cardNoWithoutLuhn + chr(calcLuhn(cardNoWithoutLuhn, True) + ord('0'))
    
if __name__=="__main__":
    cardNo = "79927398710"
    if (checkLuhn(cardNo)):
        print("'%s' is a valid card number" % cardNo)
    else:
        print("'%s' is NOT a valid card number" % cardNo)
    print("'%s' is correct card number" % generateLuhn(cardNo[:-1]))
