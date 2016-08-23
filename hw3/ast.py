# AST table

idConstructorNum = 1
idMethodNum = 1
idFieldNum = 1
idVaribleNum = 1

classList = []
classDic = {}

tempVarTable = {}
tempVarList = []

noError = True

class Class(object):

    constructors = {}
    methods = {}
    fields = {}
    name = ''
    superClassName = ''

    def __init__(self, name, superclass, decl):
        global noError
        self.name = name
        if classDic.has_key(self.name) :
            noError = False
            print "Error: Duplicate class %s defined!" %self.name
            return
        classList.append(self)
        classDic[self.name] = self 
        self.superClassName = superclass
        # print ">>>>>>>>>>>>>"
        # print self.name
        # print self.fields
        # print self.constructors
        # print self.methods
        # print ">>>>>>>>>>>>>"
        # without the fellowing code, field, constructor, method just inhert
        # previous one, are ya kidding....
        self.fields = {}
        self.constructors = {}
        self.methods = {}
        if decl:
            for item in decl:
                if type(item) is Constructor:
                    item.containingClass = name
                    self.constructors[item.id] = item
                elif type(item) is Method:
                    item.containingClass = name
                    self.methods[item.name] = item
                elif type(item) == Field:
                    item.containingClass = name
                    if(self.fields.has_key(item.name)):
                        noError = False
                        print "Error: Duplicate Fields %s defined in class %s!" %item.name,self.name
                        return
                    self.fields[item.name] = item
                else:
                    noError = False
                    print "Error: no mathcing class in field, constructor, method\n"
        # print ">>>>>>>>>>>>>"
        # print self.name
        # print self.fields
        # print self.constructors
        # print self.methods
        # print ">>>>>>>>>>>>>"
        # error with initialize here

    def output(self):
        s = "Class Name: %s\n" % self.name
        s += "Super Class Name: %s\n" % self.superClassName
        s += "Fields: \n"

        if self.fields:
            for item in self.fields:
                s += self.fields[item].output()
        s += "Constructors: \n"
        if self.constructors:
            for item in self.constructors:
                s += self.constructors[item].output()
        s += "Methods: \n"
        if self.methods:
            for item in self.methods:
                s += self.methods[item].output()
        s += "--------------------------------------------------------------\n"
        return s


class Constructor(Class):

    id = -1
    visibility = ''          # public / private
    parameters = 0          # seq of variable
    variableTable = {}
    variableList = []
    contructorBody = []     # statement

    def __init__(self, mod, name, paramList, block ):
        global  idConstructorNum,noError
        self.id = idConstructorNum
        idConstructorNum += 1    # each Constructor has identical ID
        self.visibility = mod[0]          # public / private
        self.parameters = len(paramList)         # seq of variable
        for t in paramList :
            t.kind = 'formal'
        self.variableList = paramList
        for t in paramList : 
            if self.variableTable.has_key(t.name) :
                noError = False
                print 'Error: Duplicate Variable of %s' % t.name
            else :
                self.variableTable[t.name] = t.id
        self.contructorBody = block

    def output(self):
        global noError
        s = "Constructor: %d, %s\n"% (self.id, self.visibility)
        
        if(self.parameters > 0) :
            s += "Constructor Parameters: %d\n" %self.parameters
        else :
            s += "Constructor Parameters: \n" 
        s += "Variable Table: \n"
        if self.contructorBody.varibleList:
            for item in self.contructorBody.varibleList:
                if self.variableTable.has_key(item.name) :
                    noError = False
                    print 'Error: Duplicate Variable of %s' % item.name
                else :
                    self.variableTable[item.name] = item.id
                    self.variableList.append(item)
        for t in self.variableList :
            s += t.output()
        s += "Constructor Body: \n"
        if self.contructorBody:
            s +=  self.contructorBody.output()
        return s


class Method(Class):

    variNum = 0
    name = ''
    id = -1
    containingClass = ''                # name of class
    visibility = ''             # public / private
    applicability  = ''         # static or non-static
    parameters = 0         # seq of variable
    variableList = []
    variableTable = {}
    returnValue = ''        # type / emp (void)
           # statement

    def __init__(self, mod, type, name, paramList, block):
        self.name = name
        global idMethodNum,noError
        self.id = idMethodNum
        idMethodNum += 1
        self.containingClass = ''                # name of class
        self.visibility = mod[0]             # public / private
        self.applicability = mod[1]         # static or non-static
        self.parameters = len(paramList)         # seq of variable
        for t in paramList :
            t.kind = 'formal'
        self.variableList = paramList
        for t in paramList : 
            if self.variableTable.has_key(t.name) :
                noError = False
                print 'Error: Duplicate Variable of %s' % t.name
            else :
                self.variableTable[t.name] = t.id
                
        self.methodBody = block
        self.returnValue = type

    def output(self):
        global noError
        s = "METHOD: %d, %s, %s, %s, %s, %s\n"% (self.id, self.name, self.containingClass, self.visibility, self.applicability, self.returnValue)
        if(self.parameters > 0) :
            s += "Method Parameters: %d\n" %self.parameters
        else :
            s += "Method Parameters: \n" 
        s += "Variable Table: \n"
        if self.methodBody.varibleList:
            for item in self.methodBody.varibleList:
                if self.variableTable.has_key(item.name) :
                    noError = False
                    print 'Error: Duplicate Variable of %s' % item.name
                else :
                    self.variableTable[item.name] = item.id
                    self.variableList.append(item)
        for t in self.variableList :
            s += t.output()
        s += "Method Body: \n"

        s += self.methodBody.output()
        return s


class Field(Class):

    variNum = 0
    name = ''
    id = idFieldNum
    type = ''
    containingClass = ''
    visibility = ''         # public / private
    applicability = ''
    #variableList = []

    def __init__(self, vis, app, name, type):
        self.variNum = 0
        self.name = name
        global idFieldNum
        self.id = idFieldNum
        idFieldNum += 1
        self.type = type
        self.visibility = vis
        self.applicability = app

    def output(self):
        s = "FIELD: %d, %s, %s, %s, %s, %s\n" %(self.id, self.name, self.containingClass, self.visibility, self.applicability, self.type)
        return s


class Variable :
    name = ''
    id = -1                 # unique in constructor or method
    kind = ''              # formal / local
    type = ''
    baseType = ''
    loc = 0
    
    def __init__(self, name, loc):
        global idVaribleNum, tempVarTable, tempVarList 
        self.name = name
        self.id = idVaribleNum      # unique in constructor or method
        idVaribleNum += 1
        if(not tempVarTable.has_key(self.name)) :
            tempVarTable[self.name] = []
        tempVarTable[self.name].append(self.id)
        self.kind = 'local'              # formal / local
        self.type = ''              
        self.baseType = ''
        self.loc = loc

    def output(self):
        s = "VARIABLE %d, %s, %s, %s\n" %(self.id, self.name, self.kind, self.type)
        return s


class Type:                     # array or elementary
    type = ''
    def __init__(self, type):         # one of int, float, boolean, or string or class name
        self.type = type

# Statement Group

class Statement:

    lineStart = -1
    lineEnd = -1

    def __init__(self):
        self.lineStart           # index of start and end
        self.lineEnd             # to be added to code


class IfStmt(Statement):

    ifStmt = []
    thenStmt = []
    elseStmt = []

    def __init__(self, ifStmt,thenStmt, elseStmt):
        self.ifStmt = ifStmt           # expression
        self.thenStmt = thenStmt         # Statement
        self.elseStmt = elseStmt         # Statement

    def output(self):
        s = "If(%s), then(%s)"% (self.ifStmt.output(), self.thenStmt.output())
        if self.elseStmt != []:
            s += ", else(%s)" %self.elseStmt.output()
        return s



class WhileStmt(Statement):

    loopCondition = []
    body = []

    def __init__(self,loopcondition, body):
        self.loopCondition = loopcondition   # expression
        self.body = body              # statement#

    def output(self):
        s = "While(%s), Body: %s" % (self.loopCondition, self.body)
        return s


class ForStmt(Statement):

    intializer = []       # expression
    condition = []        # expression
    update = []           # expression
    body = []            # statement

    def __init__(self, intializer, condition, update, body):
        self.intializer = intializer       # expression
        self.condition = condition        # expression
        self.update = update           # expression
        self.body = body            # statement
    def output(self):
        s = "For(%s, %s, %s), Body: %s" %(self.intializer.output(), self.condition.output(), self.update.output(), self.body.output())
        return s



class ReturnStmt(Statement):

    returnValue = []

    def __init__(self,returnValue):
        self.returnValue = returnValue    # expression
    def output(self):
        if(len(self.returnValue.args) != 0) :
            s = "Return(%s)"% self.returnValue.output()
        else :
            s = "Return()"
        return s


class ExprStmt(Statement):

    expression = []

    def __init__(self, expression):
        self.expression        # expression

    def output(self):
        s = "Expression: (  ",
        for item in self.expression:
            s += item.output
        s += "   )\n"
        return  s


class BlockStmt(Statement):

    stmt = []

    def __init__(self, stmt, tspan):
        global idVaribleNum, tempVarTable, tempVarList,noError
        self.varibleTable = {}
        self.varibleList = []
        self.span = tspan;
        self.stmt = stmt         # statement seq
        t = len(tempVarList) - 1
        while t >= 0 and tempVarList[t].loc <= self.span[1] and tempVarList[t].loc >= self.span[0] :
            self.varibleList.append(tempVarList[t])
            if(self.varibleTable.has_key(tempVarList[t].name)) :
                print ("Error: Duplicated variable of %s!") % tempVarList[t].name
                noError = False
            else :
                self.varibleTable[tempVarList[t].name] = tempVarList[t].id
            tempVarTable[tempVarList[t].name].pop()
            tempVarList.pop()
            t -= 1

    def output(self):
        s = "Block(["
#        print self.stmt
        if self.stmt:
            for item in self.stmt:
                s += "\n"
                if(item != self.stmt[0]) :
                    s += ','
#               print "****%s" %item
                s += item.output()
        s += "\n ])\n"
        return s


class BreakStmt(Statement):

    def __init__(self):
        pass

    @staticmethod
    def output(self):
        return "Break"


class ContinueStmt(Statement):

    def __init__(self):
        pass

    @staticmethod
    def output(self):
        return "Continue"


class SkipStmt(Statement):

    def __init__(self):
        pass                   # empty else part

    @staticmethod
    def output(self):
        return "Skip"


# Expression Group
class Expression:
    lineStart = -1
    lineEnd = -1

#     def __init__(self,bef):
#          self.lineStart = 
#          self.lineEnd


class ConstantExpr (Expression):

    info = []
    type = ''

    def __init__(self, info, type):
        self.info = info                  # Integer / Float / String / Null
        self.type = type

    def output(self):
        s = "Constant(%s(%s))"% (self.type, self.info)
        return s


class VarExpr (Expression):

    id = []

    def __init__(self, tid):
        global idVaribleNum, tempVarTable, tempVarList
        self.id = tid
        for t in tid :
            tempVarList.append(t)

    def output(self):
        s =''
        if self.id:
            s = "Declare Variable: # "
            for item in self.id:
                if(item != self.id[0]) :
                    s += ','
                s += "%s" %item.name
        return s



class AssignExpr (Expression):
    left = ''
    right = ''

    def __init__(self, left, right):
        self.left = left                 # expression
        self.right = right                # expression

    def output(self):
#        print self.left.output()
#        print self.right.output()
        s = "Assign:( %s, %s)" %( self.left.output() , self.right.output())
        return s



class ThisExpr (Expression):
    name = ''
    def __init__(self):
        self.name = 'This'

    def output(self):
        s = "This"
        return s


class SuperExpr(Expression):
    name = ''
    def __init__(self):
        self.name = 'Super'

    def output(self):
        s = "Super"
        return s


class ClassReference(Expression):
    className = ''

    def __init__(self):
        self.className       # class name

class NewObjectExpr(Expression):
    def __init__(self, className, argument):
        self.className = className  # string
        self.argument  = argument   # seq of expression / emp

    def output(self):
        s = "New-object(%s, %s)"% (self.className, self.argument.output())
        return s

class args_opt(Expression):
    args = []
    
    def __init__(self, list):
        self.args = list
    def output(self):
        s = "["
        for t in self.args :
            if(t != self.args[0]) :
                s += ','
            s += t.output()
        s += ']'
        return s
class stmtexpr_opt(Expression) : 
    args = []
    def __init__(self, list):
                self.args = list
    def output(self):
        s = ""
        for t in self.args :
            if(t != self.args[0]) :
                s += ','
            s += t.output()
        return s
        
class FieldAccessExpr (Expression):

    def __init__(self,name):
        self.bas = 'This'         # expression
        self.name = name         # string

    def output(self):
        s = "Field-Access(%s, %s)"% (self.bas, self.name)
        return  s
        
class VarAccessExpr (Expression):

    def __init__(self,name):
        global idVaribleNum, tempVarTable, tempVarList
        self.name = name         # string
        self.id = -1
        if tempVarTable.has_key(self.name):
            self.id = tempVarTable[self.name][len(tempVarTable[self.name])-1]

    def output(self):
        s = "Variable(%s)" %self.id
        return  s

class ArrayAccessExpr(Expression):
    bas = ''
    index = ''

    def __init__(self, bas, index):
        self.bas = bas           # expression
        self.index = index        # expression
    def output(self):
        s = "Array-Access(%s, %s)" %(self.bas.output(),self.index.output())
        return s

class MethodCallExpr (Expression):
    def __init__(self, bas, name, argu2Call ):
        self.bas  = bas        #expr
        self.name  = name        #string
        self.argu2Call  = argu2Call  #seq of expr  / emp

    def output(self):
        s = "Method-call(%s,%s," %(self.bas.output(), self.name) + self.argu2Call.output()
        s += ")"
        return s
        
class BinaryExpr (Expression):

    operand1 = ''
    operand2 = ''
    operator = ''

    def __init__(self, operand1, operator, operand2):
        self.operand1 = operand1              # expression
        self.operand2 = operand2             # expression
        self.operator = operator            # add, sub, mul, div, and, or, eq, neq, lt, leq, gt, and geq

    def output(self):
        s = "Binary(%s, %s, %s)" % (self.operator, self.operand1.output(),  self.operand2.output())
        return s

class UnaryExpr (Expression):

    operand = ''
    operator = ''

    def __init__(self, operand, operator):
        self.operand = operand                # +25 -25
        self.operator = operator

    def output(self):
        s = "Unary(%s, %c)" % (self.operand.output(), self.operator)
        return s    

class AutoExpr (Expression):       # x++

    operand = ''
    autoIncre = ''
    post = ''

    def __init__(self, operand, autoIncre, post):
        self.operand = operand       # expression
        self.autoIncre = autoIncre   # increase/decrease
        self.post = post             # post/pre

    def output(self):
        s = "Auto(%s, %s, %s)" % (self.operand.output(), self.autoIncre, self.post)
        return s

class NewArrayExpr (Expression):

    type = ''
    dimension = ''

    def __init__(self, typ, dim):
        self.type = typ
        self.dimension = dim       # array
    def output(self):
        return self.dimension

# new int[25][][] should be represented by an new array expression
# of base type array(array(int)), with array dimension 25