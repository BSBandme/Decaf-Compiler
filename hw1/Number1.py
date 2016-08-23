#program submit
import sys
import string

#mode = "test"   # test mode input from file
mode = "submit"   # submit mode keyboard input

commands = ""
stack = []
store = []

def labelCheck(label,colon = False):
    #check label name validness
    #label the string to check; colon if the label end with colon
    if colon == True and label[len(label)-1] != ':':
        return False
    else:
        label = label[:len(label)-1]
    if label[0] in string.lowercase:
        for digit in label[1:]:
            if not (digit.isdigit() or digit in string.lowercase or digit == '_'):
                return  False
    else:
        return False
    return  True

def rpop(list):
    #the pop check
    if stack:
        return stack.pop()
    else:
        print ("Error: the stack is empty, cannot pop")
        print (i)
        exit()

def inputProcess():
    #load the commands and check it's validity
    global commands
    global jumpRegister
    tempCommands = []

    #load commands
    if mode == "test":
        f = open("input2.txt")
        tempCommands = f.readlines()
        f.close()
    else:
        for line in sys.stdin:
            tempCommands.append(line)

    for i in range(0,len(tempCommands),1):
        #process of comment and combine lines
        if (tempCommands[i].find('#') == -1 ):
            if tempCommands[i].find('\n') == -1:
                temp=len(tempCommands[i])
            else:
                temp=tempCommands[i].find('\n')
        else:
            temp=tempCommands[i].find( '#' )
        commands += tempCommands[i][:temp]
        commands += ' '

    #split base on ' '
    commands = commands.split()

    i=0
    while i < len(commands):
        #input grammar chack if fails, exit
        #print(i,commands[i])
        if commands[i] in ['ildc',                       #Fellowed by num
                          ]:
            if not(commands[i+1].isdigit() == True or (commands[i+1][1:].isdigit() == True and commands[i+1][0] == '-')):
                print("Error: ildc + num wrong ",commands[i+1],commands[i+1][1:].isdigit() == True, commands[0] == '-')
                exit()
            i += 1
        elif commands[i] in [
                           'iadd','isub','imul','idiv','imod',
                           'pop','dup','swap',
                           'load','store','pop'            #Related to store
                          ]:
            pass
        elif commands[i] in [
                           'jz','jnz', 'jmp'                  #Fellowed by label
                          ]:
            if labelCheck(commands[i+1],False):
                if not (commands.count(commands[i+1]+':') == 1):
                    #print(commands.count(commands[i+1]+':'),commands[i+1]+':',commands[4])
                    print("Error: no where to jump to")
                    exit()
            else:
                print("label check failed 1")
                exit()
            i += 1
        elif commands[i][len(commands[i]) - 1] == ':': 
            if not labelCheck(commands[i],True):
                print("label check failed 2  " + commands[i])
                exit()  
            if commands.count(commands[i]) > 1:
                print("duplicate label");
                exit()
#            if not (commands.count(commands[i][:len(commands[i])-1]) == 1):
#                print("Error: no matching jump command")
#                exit()
        else:
            exit()
            print("Error: input not standard" + commands[i])
        i += 1


#end of funciton input Process

#semantics
#'ildc',                       #Fellowed by num
#'iadd','isub','imul','idiv'
#'rpop','dup','swap'
#'jz','jnz','jump',                   #Fellowed by label
#'load','store'                #Related to store
def calcProcess():
    global i
    i=0
    while i < len(commands):
        keyWord = commands[i]
        if keyWord == 'ildc':
            stack.append(int(string.atof(commands[i+1])))
            i += 1
        elif keyWord == 'iadd':
            a = rpop(list)
            b = rpop(list)
            stack.append(a+b)

        elif keyWord == 'isub':
            a = rpop(list)
            b = rpop(list)
            stack.append(b-a)
        elif keyWord == 'imul':
            a = rpop(list)
            b = rpop(list)
            stack.append(a*b)
        elif keyWord == 'idiv':
            a = rpop(list)
            b = rpop(list)
            stack.append(b/a)
        elif keyWord == 'imod':
            a = rpop(list)
            b = rpop(list)
            stack.append(b%a)
        elif keyWord == 'pop':
            if (stack):
                a = rpop(list)
                store[0] = a
            else:
                print("Error: stack is empty cannot laod")
                exit()
        elif keyWord == 'dup':
            a = rpop(list)
            stack.append(a)
            stack.append(a)
        elif keyWord == 'swap':
            a = rpop(list)
            b = rpop(list)
            stack.append(a)
            stack.append(b)

        elif keyWord == 'jz':
            if rpop(list) == 0:
                i = commands.index(commands[i+1]+":")
        elif keyWord == 'jnz':
            if rpop(list) != 0:
                i = commands.index(commands[i+1]+":")
        elif keyWord == 'jmp':
            i = commands.index(commands[i+1]+":")
        elif keyWord == 'load':
            a = rpop(list)
            if a < 0:
                print("Error: the store address is negative")
                exit()
            if store[a] != 'empty':
                stack.append(store[a])
            else:
                print ("Error: store is not intitalized before use ")
                exit()
        elif keyWord == 'store':
            a = rpop(list)
            b = rpop(list)
            store[b] = a
        i += 1


#main
for i in range(1000):
    store.append("empty")  #since only digit is stored, it's ok to use empty
inputProcess()
calcProcess()
if(mode == 'test'):
    print(store[1])
else:
    print(int(rpop(list)))