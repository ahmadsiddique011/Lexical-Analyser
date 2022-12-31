#                         <<<<LEXICAL ANALYSIS>>>
#MUHAMMAD AHMAD SIDDIQUE
#200901077

import re
def LexicalAnalyser(EXP):    #using PascalCase

    pattern = r'\d+|[a-zA-Z]+|[^\s\d+a-zA-Z]+' #expression pattern
    regex_EXP = re.compile(pattern)   #using snake_case #built in function(compile) to compile RE.
    matches = regex_EXP.finditer(EXP) #match string will extract

    tokens = []  #append matched strings in token list
    for match in matches:
        token = match.group()
        tokens.append(token)
    return tokens
print ("\nENTER Expression, i.e  a+(b*c)\n")
EXP = input("Enter an expression: ")
tokens = LexicalAnalyser(EXP)
print(tokens)
