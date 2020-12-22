import sys
import os

def calcLuhn(cardNo: str, isCurrentCharEven: bool = False):
    """
    cardNo:
           cardNo for checking if isCurrentCharEven = False
           cardNoWithoutLuhn for calculation Luhn number if isCurrentCharEven = True
    isCurrentCharEven:
           False for checking
           True for calculation Luhn number
    """
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
    # If initial isCurrentCharEven == False (called for checking)
    #     and luhnNumber == 0 then cardNo[-1] is correct Luhn number
    #     else cardNo[-1] is NOT correct Luhn number
    # else luhnNumber is calculated Luhn number
    return luhnNumber   
def checkLuhn(cardNo: str):
    return False if calcLuhn(cardNo) else True
def generateLuhn(cardNoWithoutLuhn: str):
    return cardNoWithoutLuhn + chr(calcLuhn(cardNoWithoutLuhn, True) + ord('0'))

if __name__ == "__main__":
    # print(generateLuhn("444555oooooo777".replace("o","0")))
    if len(sys.argv) == 2:
        print(generateLuhn(sys.argv[1].replace("o","0")))
    else:
        print("Usage: %s <First 15 digits of card no>" % os.path.split(sys.argv[0])[1])
