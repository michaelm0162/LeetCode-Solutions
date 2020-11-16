#! Python3
# romanToInt - Returns the numerical value for a roman numeral between 1 and 3999

Numerals = {'I':1,'V':5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}
def romanToInt(s):
    '''Will find the numerical value
    for any roman numeral between 1 and 3999'''
    lastNum = 0
    total = 0
    for i in range(len(s),0,-1):
        num = Numerals[s[i-1]]
        if num < lastNum:
            total = total - num
        else:
            total = total + num
        lastNum = num
    return total

s = input('Input roman numeral(Max value 3,999): ')

for i in range(len(s)):
    if s[i] not in Numerals:
        print('Invalid roman numeral or beyond range')
        quit()
        
print("The numerical value for '{}' is {}".format(s,romanToInt(s)))
