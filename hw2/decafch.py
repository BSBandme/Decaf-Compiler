import sys
import ply.lex as lex
import ply.yacc as yacc


import decaflexer
import decafparser

import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

# linesum = []

#testmode = "debug"
testmode = "release"
filename = ""
inputstring = "MYPROGRAMSTARTPOINT "

lexer1 = lex.lex(module=decaflexer)
if testmode == "debug":
    filename = "input.txt"
else :
    filename = sys.argv[1]
        
f = open(filename)
rin = f.readlines()
for i in range(0, len(rin)):
    inputstring += rin[i]
#     linesum.append(len(rin[i]))
#     if i != 0 :
#         linesum[i] += linesum[i - 1]
# for i in range(len(rin) - 1, 0, -1) :
#     linesum[i] = linesum[i - 1]
inputstring += " MYPROGRAMENDPOINT"
lexer1.input(inputstring)
# for token in lexer1:
#     print token
myparser = yacc.yacc(module=decafparser,debug=True,debuglog=log)
result = myparser.parse(lexer=lexer1, tracking=True,debug=log)
if result == 'Correct' :  
    print('Yes')
if len(myparser.statestack) > 2 : 
    print('Syntax Error: Unexpected of EOF')
