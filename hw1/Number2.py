#program submit
import sys
import string

#mode = "test"   # test mode input from file
mode = "submit"   # submit mode keyboard input
commands = ""
vari = []
value = []
result = ""

def labelCheck(label,colon = False):
    #check label name validness
    #label the string to check; colon if the label end with colon
    if colon == True and label[len(label)-1] != ':':
        return False
    else:
        label = label[:len(label)-1]
    if len(label)==0:
        if label in string.lowercase:
            return True
        else:
            return False
    elif label[0] in string.lowercase:
        for digit in label[1:]:
            if not (digit.isdigit() or digit in string.lowercase or digit == '_'):
                return  False
    else:
        return False
    return  True

def inputProcess():
    #load the commands and check it's validity
    global commands
    global vari

    tempCommands = []

    #load commands
    if mode == "test":
        f = open("input1.txt")
        tempCommands = f.readlines()
        f.close()
    else:
        for line in sys.stdin:
            tempCommands.append(line)

    for i in range(0,len(tempCommands),1):
        if ((tempCommands[i].find('~ ')!=-1)or(tempCommands[i].find('~\n')!=-1)or(tempCommands[i].find('~\t')!=-1)):
            print('Error: illegal use of ~')
            exit()
        #process of comment and combine lines
        if (tempCommands[i].find(';') != -1 ):
            tempCommands[i] = tempCommands[i].replace(';',' ; ')
            semcolonFlag = True
        else:
            semcolonFlag = False

        if (tempCommands[i].find('~') != -1 ):
            tempCommands[i] = tempCommands[i].replace('~',' ~ ')

        commands += tempCommands[i]
    if semcolonFlag == False:
        print("Error: command not ended with ;")
        exit()
    #split base on ' '
    commands = commands.split()

    i = 0
    opeNum = 0
    numNum = 0
    newline = 0
    result = 0
    startIndex = 0
    variNum = 0
    while i < len(commands):
        # syntax check
        # since all operator has 2 input: #operater = #num + 1
        if newline == 0:
            if not labelCheck(commands[i]):
                print "Error: Variable name check fail"
                exit()
            else:
                if commands[i] not in vari:
                    vari.append(commands[i])
                    result = len(vari)-1
                    value.append("empty")
                newline += 1
        elif newline == 1:
            if not commands[i] == '=':
                print("Error: = not found")
                exit()
            else:
                newline = -1 #close the new line process
        elif commands[i] == ';':
            if opeNum +1 == numNum:
                newline = 0 # restart new line process
                opeNum = 0
                numNum = 0
                value[result] = "initalized"
                opeNum = 0
                numNum = 0
            else:
                print("Error: operator number and operand number not match")  #fix
                exit()
        elif commands [i] == '~':
            if commands [i+1].isdigit():
                commands [i+1] = '-' + commands [i+1]
                numNum += 1
                i += 1
            else:
                print("Error: no number after \'~\'")
                exit()
        elif commands [i].isdigit():
            numNum += 1
        elif commands[i] in ['+','-','*','/','%']:
            opeNum += 1
        elif commands[i] in vari:
            if value[vari.index(commands[i])] == "initalized":
                numNum += 1
            else:
                print("Error: variable defined but not initalized")
                exit()
        else:
            print(commands[i],commands[i+1])
            print("Error: syntax wrong or use variable without initialize")
            exit()
        i += 1
    for i in range(0, len(commands), 1):
        if(commands[i] == '~') :
            commands.remove("~")
            break

    #print("syntax check success")

def myCompile():
    global result,commands
    lineStart = 0;
    lineEnd = 0;
    while lineStart < len(commands):
        # compile
        lineEnd = commands.index(";",lineStart)

        result += "ildc "+str(vari.index(commands[lineStart])) + '\n'  # x =
        linestart = syntaxCheck(lineStart+2)
        if(linestart != lineEnd):
            print("Error: Syntax error!")
            exit()
        result += "store\n"
        lineStart = lineEnd + 1

def syntaxCheck(i) :
    if (i<0):
        return i
    global vari,valuen,result
    op = ""
    if(commands[i].isdigit() or (len(commands) > 1 and commands[i][0] == '-' and commands[i][1:].isdigit())) :
        result += "ildc "
        result += str(int(string.atof(commands[i])))+'\n'
        return i + 1
    elif commands[i] in vari:
        result += "ildc " + str(vari.index(commands[i]))+'\n'
        result += "load" + '\n'
        return i+1
    elif commands[i] in ['+','-','*','/','%']:
        if commands[i] == '+':
            op = "iadd"
        if commands[i] == '-':
            op = "isub"
        if commands[i] == '*':
            op = "imul"
        if commands[i] == '/':
            op = "idiv"
        if commands[i] == '%':
            op = "imod"
        i = syntaxCheck(i+1)
        i = syntaxCheck(i)
        result += op + '\n'
        return i
    else:
        return -1

def output():
    global result
    print(result)
inputProcess()
myCompile()
output()