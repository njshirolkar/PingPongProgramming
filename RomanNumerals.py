"""
Roman Numerals

Convert roman numerals to decimal and back


"""

decimal = [1, 5, 10, 50, 100, 500, 1000]
roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

def toRoman(decimalNumber: str) -> str:
    """ Converts decimal numbers (as string data type) to roman numerals (as string as well)
    >>> toRoman("10")
    'X'
    >>> toRoman("4")
    'IV'
    >>> toRoman("15")
    'XV'
    >>> toRoman("24")
    'XXIV'
    """
    num = int(decimalNumber)
    
    # Find closest numeral grater than this number
    closest = 0
    while decimal[closest] < num:
        closest += 1
    
    # Edge case of equals
    if decimal[closest] == num:
        return roman[closest]
    # Edge case if number is greater than half of the next number
    elif num * 2 > decimal[closest]:
        return toRoman(decimal[closest] - num) + roman[closest]
    
    # Ignore that greater than number, find closest less than number
    closest -= 1
    
    # Find the closest's deicmal value
    decimalClosest = decimal[closest]
    
    # Find the number of repeats and how much is leftover
    multiplicity = num // decimalClosest
    remainder = num % decimalClosest
    
    # If there is more of the number left, keep on going, otherwise end
    if remainder > 0:
        return roman[closest] * multiplicity + toRoman(remainder)
    return roman[closest] * multiplicity

def lookupValue(romanNumeral: str) -> int:
    return decimal[roman.index(romanNumeral)]

def toDecimalInt(romanNumber: str) -> int:
    # Find a block of continous numbers
    ptr = 0
    while ptr + 1 < len(romanNumber) and \
            romanNumber[ptr] == romanNumber[ptr + 1]:
        ptr += 1
    # Find the sum of that block
    blockSum = lookupValue(romanNumber[0]) * (ptr + 1)
    
    # If at the end, return the sum
    if ptr + 1 == len(romanNumber):
        return blockSum
    # Else if the next numeral is less than the current numeral, 
    # add the rest of the number's sum to this block's sum
    elif lookupValue(romanNumber[ptr]) > lookupValue(romanNumber[ptr + 1]):
        return blockSum + toDecimalInt(romanNumber[ptr + 1:])
    # If the next numeral is grater than the current numeral
    # Subtract this number's sum from the rest of the number
    return toDecimalInt(romanNumber[ptr + 1:]) - blockSum

def toDecimal(romanNumber: str) -> str:
    """ Converts roman numbers (as string data type) to decimal numerals (as string as well)
    >>> toDecimal("X")
    '10'
    >>> toDecimal("IV")
    '4'
    >>> toDecimal("XV")
    '15'
    >>> toDecimal("XXIV")
    '24'
    """
    return str(toDecimalInt(romanNumber))
