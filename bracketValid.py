#! Python3
# bracketValid.py - Ensures all bracktes are valid and closed correctly
# Contains testing on the bottom of code.
# problem 20 on leetcode.com

def isValid(s):
    '''s = string including brackets
    return type: bool
    verifies all brackets are valid by being closed correctly'''
    bracket = []
    openingBrackets = ['(', '[', '{']
    closingBrackets = {')':'(', ']':'[', '}':'{'}
    for i in range(len(s)):
        if len(bracket) == 0 and s[i] in closingBrackets:
            return False
        if s[i] in closingBrackets:
            if bracket[len(bracket)-1] != closingBrackets[s[i]]:
                return False
            else:
                bracket.pop()
        else:
            if s[i] in openingBrackets:
                bracket.append(s[i])
    if len(bracket) == 0:
        return True
    else:
        return False



# TEST SCENARIOS
s1 = '()[]{}'
s2 = '([])'
s3 = '(([[]]))'
s4 = '(soooo[])'
s5 = '([)]'
s6 = '[([]])'
s7 = '['
s8 = '[{'
s9 = ')]'

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))
print(isValid(s4))
print('Should be False:')
print(isValid(s5))
print(isValid(s6))
print(isValid(s7))
print(isValid(s8))
print(isValid(s9))
