import ast
from __builtin__ import True

def isSubType(a, b):
    if((not isinstance(a, ast.Type)) or not isinstance(b, ast.Type)):
        print "Not 'Type' type"
        return False
    if(a.kind == 'basic' and a.typename == 'error') :
        return False
    if(b.kind == 'basic' and b.typename == 'error') :
        return False
    
    if(a.kind == 'basic' and a.typename == 'Null') :
        return True
    if(a.kind != b.kind) :
        return False
    if(a.kind == 'basic') :
        if(a.typename == b.typename) :
            return True
        if(a.typename == 'int' and b.typename == 'float') :
            return True
        return False
    elif(a.kind == 'class') :
        return isSubClass(ast.classtable[a.typename], ast.classtable[b.typename])
    elif(a.kind == 'class_literal') :
        return isSubClass(ast.classtable[a.typename], ast.classtable[b.typename])
    else :
        return isSubType(a.basetype, b.basetype)

def isSubClass(a, b):
    if((not isinstance(a, ast.Class)) or not isinstance(b, ast.Class)) :
        print "Not 'Class' Type"
        return False
    if(a.name == b.name) :
        return True
    if(a.superclass == None) :
        return False
    return isSubClass(a.superclass, b)
        
def classCheck(node):
    flag = True
    for i in node.constructors :
        if(not functionCheck(i)):
            flag = False
    for i in node.methods : 
        if(not functionCheck(i)) :
            flag =  False
    return flag

def functionCheck(node):
    return stmtCheck(node.body)

# stmt Check
def stmtCheck(node): 
    if(isinstance(node, ast.IfStmt)) :
        return ifStmtCheck(node)
    elif(isinstance(node, ast.WhileStmt)) :
        return whileStmtCheck(node)
    elif(isinstance(node, ast.ForStmt)):
        return forStmtCheck(node)
    elif(isinstance(node, ast.ReturnStmt)) :
        return returnStmtCheck(node)
    elif(isinstance(node, ast.ExprStmt)):
        return exprStmtCheck(node)
    elif(isinstance(node, ast.BlockStmt)):
        return blockStmtCheck(node)
    elif(isinstance(node, ast.BreakStmt)):
        return True
    elif(isinstance(node, ast.ContinueStmt)):
        return True
    elif(isinstance(node, ast.SkipStmt)):
        return True
    else :
        return False
    
def ifStmtCheck(node):
    flag = True
    if not isinstance(node, ast.IfStmt) :
        print 'Error ifstmtCheck, not IfStmt'
        flag = False
    if(not exprCheck(node.condition)) :
        print('Line %d: if condition type check failed') %node.lines
        flag = False
    if(node.condition.basetype.kind != 'basic' or node.condition.basetype.typename != 'boolean') :
        print('Line %d: if condition type check failed') %node.lines
        flag =  False
    if(not stmtCheck(node.thenpart)) :
        print('Line %d: if then stmt check failed') %node.lines
        flag = False
    if(not stmtCheck(node.elsepart)) :
        print('Line %d: if else stmt check failed') %node.lines
        flag = False
    return flag

def whileStmtCheck(node):
    flag = True
    if not isinstance(node, ast.WhileStmt) :
        print 'Error whilestmtCheck, not WhileStmt'
        flag = False
    if(not exprCheck(node.cond)) :
        print('Line %d: while condition type check failed') %node.lines
        flag = False
    if(node.cond.basetype.kind != 'basic' or node.cond.basetype.typename != 'boolean') :
        print('Line %d: while condition type check failed') %node.lines
        flag = False
    if(not stmtCheck(node.body)) :
        print('Line %d: while body check failed') %node.lines
        flag = False
    return flag

def forStmtCheck(node):
    flag = True
    if not isinstance(node, ast.ForStmt):
        print 'Error forStmtCheck, not ForStmt'
        flag = False
    if(not exprCheck(node.cond)) :
        print('Line %d: for condition type check failed') %node.lines
        flag = False
    if(node.cond.basetype.kind != 'basic' or node.cond.basetype.typename != 'boolean') :
        print('Line %d: for condition type check failed') %node.lines
        flag = False
    if(not exprCheck(node.init)) :
        print('Line %d: for initialization check failed') %node.lines
        flag = False
    if(not exprCheck(node.update)):
        print('Line %d: for update check failed') %node.lines
        flag = False
    if(not stmtCheck(node.body)):
        print('Line %d: for body check failed') %node.lines
        flag = False
    return flag

def returnStmtCheck(node):
    if not isinstance(node, ast.ReturnStmt):
        print 'Error returnStmtCheck, not ReturnStmt'
        return False
    if(node.expr == None) :
        if(node.rtype.kind != 'basic' or node.rtype.typename != 'void') :
            print('Line %d: return value type is not a subtype of return type') %node.lines
            return False
    else :
        if(not exprCheck(node.expr)) :
            print('Line %d: return expr check failed') %node.lines
            return False
        if(not isSubType(node.expr.basetype, node.rtype)) :
            print('Line %d: return value type is not a subtype of return type') %node.lines
            return False
    return True

def exprStmtCheck(node):
    if not isinstance(node, ast.ExprStmt):
        print 'Error exprStmtCheck, not ExprStmt'
        return False
    if(not exprCheck(node.expr)) :
        print('Line %d: expr stmt check failed') %node.lines
        return False
    return True

def blockStmtCheck(node): 
    if not isinstance(node, ast.BlockStmt):
        print 'Error blockStmtCheck, not BlockStmt'
        return False
    flag = True
    for t in node.stmtlist :
        if(not stmtCheck(t)) :
            flag = False
    return flag

##### expr Check
#####
def exprCheck(node):
    if(isinstance(node, ast.ConstantExpr)) :
        return constantExprCheck(node)
    elif(isinstance(node, ast.VarExpr)) :
        return varExprCheck(node)
    elif(isinstance(node, ast.UnaryExpr)) :
        return unaryExprCheck(node) 
    elif(isinstance(node, ast.BinaryExpr)) :
        return binaryExprCheck(node)
    elif(isinstance(node, ast.AssignExpr)) :
        return assignExprCheck(node)
    elif(isinstance(node, ast.AutoExpr)) :
        return autoExprCheck(node)
    elif(isinstance(node, ast.FieldAccessExpr)) :
        return fieldAccessExprCheck(node)
    elif(isinstance(node, ast.MethodInvocationExpr)) :
        return methodInvocationExprCheck(node)
    elif(isinstance(node, ast.NewObjectExpr)) :
        return newObjectExprCheck(node)
    elif(isinstance(node, ast.ThisExpr)) :
        return True
    elif(isinstance(node, ast.SuperExpr)) :
        return True
    elif(isinstance(node, ast.ClassReferenceExpr)):
        return True
    elif(isinstance(node, ast.ArrayAccessExpr)) :
        return arrayAccessExprCheck(node)
    elif(isinstance(node, ast.NewArrayExpr)) :
        return newArrayExprCheck(node)
    else :
        return False

def constantExprCheck(node):
    if not isinstance(node, ast.ConstantExpr) :
        print 'Error constantExprCheck, not ConstantExpr'
        return False
    return isinstance(node.basetype, ast.Type) and node.basetype.kind == 'basic' and node.basetype.typename != 'error' 

def varExprCheck(node):
    if (not isinstance(node, ast.VarExpr) ):
        print 'Error varExprCheck, not varExpr'
        return False
    return True

def unaryExprCheck(node):
    if not isinstance(node, ast.UnaryExpr) :
        print 'Error unaryExprCheck, not UnaryExpr'
        return False
    exprCheck(node.arg)
    node.basetype = node.arg.basetype
    if(node.uop == 'neg') :
        if(node.basetype.kind != 'basic' or node.basetype.typename != 'boolean') :
            node.basetype = ast.Type('error')
            print('Line %d: Not a boolean type for unary"!"') %node.lines 
            return False
    elif node.uop == 'uminus':
        if(node.basetype.kind != 'basic' or (node.basetype.typename != 'int' and node.basetype.typename != 'float')) :
            node.basetype = ast.Type('error')
            print('Line %d: Not a int or float type for unary"-"') %node.lines
            return False
    
    return True
        
def binaryExprCheck(node):
    if not isinstance(node, ast.BinaryExpr) :
        print 'Error binaryExprCheck, not BinaryExpr'
        return False
    exprCheck(node.arg1)
    exprCheck(node.arg2)
    if(node.bop in ['add','sub','mul','div']) : 
        if(node.arg1.basetype.kind != 'basic' or node.arg1.basetype.kind != 'basic') :
            node.basetype = ast.Type('error')
            print('Line %d: Not a int or float type for binary Expression') %node.lines 
            return False
        if((node.arg1.basetype.typename != 'int' and node.arg1.basetype.typename != 'float') or(node.arg2.basetype.typename != 'int' and node.arg2.basetype.typename != 'float')):
            node.basetype = ast.Type('error')
            print('Line %d: Not a int or float type for binary Expression') %node.lines
            return False
        if(node.arg1.basetype.typename == 'float' or node.arg2.basetype.typename == 'float') :
            node.basetype = ast.Type('float')
        else :
            node.basetype = ast.Type('int')
        return True
    elif(node.bop in ['and', 'or']) :
        if(node.arg1.basetype.kind != 'basic' or node.arg1.basetype.kind != 'basic') :
            node.basetype = ast.Type('error')
            print('Line %d: Not a boolean type for binary Expression') %node.lines
            return False
        if(node.arg1.basetype.typename != 'boolean' or node.arg2.basetype.typename != 'boolean'):
            node.basetype = ast.Type('error')
            print('Line %d: Not a boolean type for binary Expression') %node.lines
            return False
        else :
            node.basetype = ast.Type('boolean')
            return True
    elif(node.bop in ['lt','leq','gt','geq']) : 
        if(node.arg1.basetype.kind != 'basic' or node.arg1.basetype.kind != 'basic') :
            print('Line %d: Not a int or float type for binary Expression') %node.lines
            node.basetype = ast.Type('error')
            return False
        if(
            (node.arg1.basetype.typename != 'int' and node.arg1.basetype.typename != 'float') or
            (node.arg2.basetype.typename != 'int' and node.arg2.basetype.typename != 'float')
          ):
            print('Line %d: Not a int or float type for binary Expression') %node.lines
            node.basetype = ast.Type('error')
            return False
        node.basetype = ast.Type('boolean')
        return True
    elif(node.bop in ['eq', 'neq']) :
        if(isSubType(node.arg1.basetype, node.arg2.basetype)) :
            node.basetype = ast.Type('boolean')
            return True
        if(isSubType(node.arg2.basetype, node.arg1.basetype)) :
            node.basetype = ast.Type('boolean')
            return True
        print('Line %d: expr is not a subtype of expr for binary Expression') %node.lines
        node.basetype = ast.Type('error')
        return False
    else:
        node.basetype = ast.Type('error')
        return False
    return True

def assignExprCheck(node):
    if not isinstance(node, ast.AssignExpr) :
        print 'Error assignExprCheck, not AssignExpr'
        return False
    exprCheck(node.lhs)
    exprCheck(node.rhs)
    if(isSubType(node.rhs.basetype, node.lhs.basetype)) :
        node.basetype = node.rhs.basetype
        return True
    print('Line %d: expr2 is not a subtype of expr1 for assign Expression') %node.lines
    node.basetype = ast.Type('error')
    return False
        
def autoExprCheck(node):
    if not isinstance(node, ast.AutoExpr) :
        print 'Error autoExprCheck, not AutoExpr'
        return False
    exprCheck(node.arg)
    if(node.arg.basetype.kind != 'basic' or (node.arg.basetype.typename != 'int' and node.arg.basetype.typename != 'float')):
        print('Line %d: expr is not a int or float type for auto Expression') %node.lines
        node.basetype = ast.Type('error')
        return False
    node.basetype = node.arg.basetype
    return True
        
def fieldAccessExprCheck(node):    
    if not isinstance(node, ast.FieldAccessExpr) :
        print 'Error fieldAccessExprCheck, not fieldAccessExpr'
        node.basetype = ast.Type('error')
        return False                                                                            #need
    cname = node.base
    if(cname == None) :
        print('Line %d: base is "none" in field access') %node.lines
        node.basetype = ast.Type('error')
        return False  
    if not exprCheck(cname) :
        node.basetype = ast.Type('error')
        return False
    if(not ast.classtable.has_key(cname.basetype.typename)) :
        print('Line %d: can\'t find base class in field access') %node.lines
        node.basetype = ast.Type('error')
        return False          
    c = ast.classtable[cname.basetype.typename]
    flag = False
    while(c != None and (not flag)) :
        flag = True
        if(not c.fields.has_key(node.fname)) :
            flag = False
            c = c.superclass
            continue
        p = c.fields[node.fname]
        if(cname.basetype.kind == 'class_literal' and p.storage != 'static') :
            flag = False
#             print('Line %d: Field is not static in class-literal') %node.lines
#             node.basetype = ast.Type('error')
#             return False

        if(cname.basetype.kind == 'class' and p.storage == 'static') :
            flag = False
#             print('Line %d: Field is static in class') %node.lines
#             node.basetype = ast.Type('error')
#             return False
        if(p.visibility == 'private' and (not isinstance(cname, ast.ThisExpr))) :
            flag = False 
#             print('Line %d: Field is private in class') %node.lines
#             node.basetype = ast.Type('error')
#             return False        
        if(flag) :
            node.basetype = p.type
            node.field = p
            break;
        c = c.superclass
    if c == None:
        print('Line %d: Field is not found in field access') %node.lines
        node.basetype = ast.Type('error')
        return False
    
    return True
        
def matchparams(args, params):
    if(len(args) != len(params)) :
        return False
    flag = True
    for i in range(0, len(args)) :
        if(isinstance(args[i], ast.Variable)):
            if(not isSubType(args[i].type, params[i].type)):
                flag = False
                break
        else:
            if(not isSubType(args[i].basetype, params[i].type)) :
                flag = False
                break
    return flag
                  
def methodInvocationExprCheck(node):
    if not isinstance(node, ast.MethodInvocationExpr) :
        print 'Error methodInvocationExprChec, not MethodInvocationExpr'
        return False                                                                            #need
    cname = node.base
    if(cname == None) :
        print('Line %d: base is "none" in method invocation') %node.lines
        node.basetype = ast.Type('error')
        return False  
    if not exprCheck(cname) :
        node.basetype = ast.Type('error')
        return False
    if(not ast.classtable.has_key(cname.basetype.typename)) :
        print('Line %d: can''t find base class in method invocation') %node.lines
        node.basetype = ast.Type('error')
        return False          
    c = ast.classtable[cname.basetype.typename]
    args = node.args
    for targs in args :
        exprCheck(targs)
    
    while(c != None) :
        can = []
        for i in c.methods :
            params = i.vars.get_params()
            if(matchparams(args, params) and i.name == node.mname) :
                flag = True
                if(cname.basetype.kind == 'class_literal' and i.storage != 'static') :
                    flag = False
#             print('Line %d: Field is not static in class-literal') %node.lines
#             node.basetype = ast.Type('error')
#             return False

                if(cname.basetype.kind == 'class' and i.storage == 'static') :
                    flag = False
#             print('Line %d: Field is static in class') %node.lines
#             node.basetype = ast.Type('error')
#             return False
                if(i.visibility == 'private' and (not isinstance(cname, ast.ThisExpr))) :
                    flag = False 
#             print('Line %d: Field is private in class') %node.lines
#             node.basetype = ast.Type('error')
#             return False        
                if(flag):
                    can.append(i)
                    
        for i in can :
            params = i.vars.get_params()
            flag = True
            for j in can :
                if(i == j) :
                    continue
                rparams = j.vars.get_params();
                if(matchparams(rparams, params)) :
                    flag = False
            if(flag) :
                if(node.method != None) :
                    print('Line %d: duplicate method accesses are applicable') %node.lines
                    node.basetype = ast.Type('error')
                    return False
                else :
                    node.basetype = i.rtype
                    node.method = i    
                        
        if(node.method != None) :
            break
        else :
            c = c.superclass
            
    if(node.method == None) :
        print('Line %d: no method accesses are applicable') %node.lines
        node.basetype = ast.Type('error')
        return False
            
    return True
         
def newObjectExprCheck(node):
    if not isinstance(node, ast.NewObjectExpr) :
        print 'Error newObjectExprCheck, not NewObjectExpr'
        return False                                                                            #need
    cname = node.classref
    if(cname == None) :
        print('Line %d: constructor class is "none" in new object') %node.lines
        node.basetype = ast.Type('error')
        return False      
    c = ast.classtable[cname.name]
    args = node.args
    for targs in args :
        exprCheck(targs)
    
    for i in c.constructors :
        params = i.vars.get_params()
        if(matchparams(args, params)) :
            flag = True
            for j in c.constructors :
                if(i != j) :
                    rparams = j.vars.get_params();
                    if(matchparams(rparams, params)) :
                        flag = False
            if(flag) :
                if(node.constructor != None) :
                    print('Line %d: duplicate constructor accesses are applicable') %node.lines
                    node.basetype = ast.Type('error')
                    return False
                else :
                    node.basetype = ast.Type(c)
                    node.constructor = i
            
    if(node.constructor != None) : 
        return True
    else :
        node.basetype = ast.Type('error')
        print('Line %d: can\'t find constructor') %node.lines
        return False
    
def arrayAccessExprCheck(node):
    if not isinstance(node, ast.ArrayAccessExpr) :
        print'Error arrayAccessExprCheck, not ArrayAccessExpr'
        return False
    exprCheck(node.index)
    if(node.index.basetype.kind != 'basic' or node.index.basetype.typename != 'int') :
        print('Line %d: index is not integer in array access') %node.lines
        node.basetype = ast.Type('error')
        return False
    exprCheck(node.base)
    if(node.base.basetype.kind != 'array') :
        print('Line %d: Not an array type in array access') %node.lines
        node.basetype = ast.Type('error')
        return False
    node.basetype = node.base.basetype.basetype
    return True
        
def newArrayExprCheck(node):
    if(not isinstance(node, ast.NewArrayExpr)) :
        print'Error newArrayExprCheck, not NewArrayExpr'
        return False
    for arg in node.args :
        exprCheck(arg)
        if (not isinstance(arg.basetype, ast.Type)) or (arg.basetype.kind != 'basic') or (arg.basetype.typename != 'int') :
            print('Line %d: Not an integer index in NewArrayExpr') %node.lines
            node.basetype = ast.Type('error')
            return False
        
    return True

