"""
Roman Numerals

Convert roman numerals to decimal and back


"""

def toRoman(decimalNumber):
    """ Converts decimal numbers (as string data type) to roman numerals (as string as well)
    >>> toRoman("10"):
    "X"
    >>> toRoman("4"):
    "IV"
    >>> toRoman("15"):
    "XV"
    >>> toRoman("24"):
    "XXIV"
    """
    num = int(decimalNumber)
    mapDecimalToRoman = {
        1:'I',
        2:'II',
        3:'III',
        4:'IV',
        5:'V',
        10:'X',
        50:'L',
        100:'C',
        500:'D',
        1000:'M'   
    }
    if num in mapDecimalToRoman.keys():
        return mapDecimalToRoman[num]  
    return "N"

def toDecimal(romanNumber):
    """ Converts roman numbers (as string data type) to decimal numerals (as string as well)
    >>> toDecimal("X"):
    "10"
    >>> toDecimal("IV"):
    "4"
    >>> toDecimal("XV"):
    "15"
    >>> toDecimal("XXIV"):
    "24"
    """
    mapRomanToDecimal = {
        'I':1,
        'II':2,
        'III':3,
        'IV':4,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000   
    }
    if romanNumber in mapRomanToDecimal.keys():
        return str(mapRomanToDecimal[romanNumber])  
    return "N"
