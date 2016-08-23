# Yacc example

# Get the token map from the lexer.  This is required.

from decaflexer import tokens
from decaflexer import precedence

def p_pp_print(p):
    'pp : program'
    p[0] = p[1]
    
## program
def p_program(p):
    '''program : MYST
               | program class_decl
               | program MYED'''
    if len(p) >= 3 and p[2] != 'MYPROGRAMENDPOINT':
        if p[1] == 'Correct' :
            p[0] = p[2]
    elif len(p) >= 3:
        p[0] = p[1]
    else :
        p[0] = 'Correct'
def p_program_error(p):
    '''program : program error'''
    print "Syntax error in line %d: no 'class' word found!" %p.lineno(2)
    
## class_decl 
def p_class_decl1(p):
    '''class_decl1 : CLASS ID LBIG
                   | CLASS ID EXTENDS ID LBIG'''
    p[0] = 'Correct'
def p_class_decl1_class_error(p):
    '''class_decl1 : error ID EXTENDS ID LBIG
                   | error ID LBIG'''
    print "Syntax error in line %d: no 'class' word found!" %p.lineno(1)
def p_class_decl1_classname_error(p):
    '''class_decl1 : CLASS error EXTENDS ID LBIG
                   | CLASS error LBIG'''
    print "Syntax error in line %d: class name is not validate" %p.lineno(2)
def p_class_decl1_extends_error(p):
    '''class_decl1 : CLASS ID error'''
    print "Syntax error in line %d: 'extends' or '{' needed" %p.lineno(3)
def p_class_decl1_LBIG_error(p):
    '''class_decl1 : CLASS ID EXTENDS ID error'''
    print "Syntax error in line %d: '{' needed" % p.lineno(5)
    p[0] = 'Error'
def p_class_decl2(p):
    '''class_decl2 : class_decl1 class_body_decl
                   | class_decl2 class_body_decl'''
    if p[1] == 'Correct' and p[2] == 'Correct' : 
        p[0] = 'Correct' 
def p_class_decl(p):
    'class_decl : class_decl2 RBIG'
    if p[1] == 'Correct' :
        p[0] = 'Correct'
# def p_class_decl_error(p):
#     'class_decl : class_decl2 error'
#     print "Syntax error in line %d: '}' needed or modifier needed" %p.lineno(2)

## class_body_decl
def p_class_body_decl(p):
    '''class_body_decl : field_decl
                       | method_decl
                       | constructor_decl'''
    p[0] = p[1]
    
## field_decl
def p_field_decl(p):
    'field_decl : modifier var_decl'
    if p[1] == 'Correct' and p[2] == 'Correct' :
        p[0] = 'Correct'
    
## modifier 
def p_modifier_first(p):
    '''modifier_first : PUBLIC
                      | PRIVATE 
                      | '''
    p[0] = 'Correct'
# def p_modifier_first_error(p):
#     '''modifier_first : error'''
#     print("Syntax error in line %d: modifier not validate" %p.lineno(1))
def p_modifier(p):
    '''modifier : modifier_first
                | modifier_first STATIC'''
    
    p[0] = p[1]
    
## var_decl
def p_var_decl(p):
    'var_decl : type variables SEMICOLON'
    if(p[1] == 'Correct' and p[2] == 'Correct') :
        p[0] = 'Correct'
def p_var_decl_error(p):
    'var_decl : type variables error'
    print("Syntax error in line %d: missing \';\' or '[' or ',' or '('" %p.lineno(1))

## type                        need
def p_type(p): 
    '''type : INT
            | FLOAT
            | BOOLEAN
            | ID'''
    p[0] = 'Correct'
def p_type_error(p):
    'type : error'
    print("Syntax error in line %d: Type error, type format not match" %p.lineno(1))
    
## variables
def p_variables(p):
    '''variables : variable
                 | variables COMMA variable'''
    if(len(p) > 2) : 
        if(p[1] == 'Correct' and p[3] == 'Correct') :
            p[0] = 'Correct'
    else: 
        p[0] = p[1]

## variable
def p_variable(p):
    '''variable : ID
                | variable LSQ RSQ'''
    p[0] = "Correct"
def p_variable_RSQ_error(p):
    '''variable : variable LSQ error '''
    print("Syntax error in line %d: ']' needed" %p.lineno(1))
    
## method_decl
def p_method_decl1(p):
    '''method_decl1 : modifier type ID LPAREN
                    | modifier VOID ID LPAREN'''
    if(p[2] == 'void') : 
        p[0] = p[1]
    else :
        if(p[1] == 'Correct' and p[2] == 'Correct'):
            p[0] = 'Correct'
def p_method_decl(p):
    '''method_decl : method_decl1 formals RPAREN block
                   | method_decl1 RPAREN block'''
    if(p[1] != 'Correct'): 
        return
    if(len(p) == 5):
        if(p[len(p) - 1] == 'Correct' and p[2] == 'Correct') :
            p[0] = 'Correct'
    else:
        p[0] = p[len(p) - 1] 
        

## constructor_decl
def p_constructor_decl(p):
    '''constructor_decl : modifier ID LPAREN RPAREN block
                        | modifier ID LPAREN formals RPAREN block'''
    if(len(p) == 6) :
        p[0] = p[len(p) - 1]
    else :
        if(p[4] == 'Correct' and p[6] == 'Correct') :
            p[0] = 'Correct'
def p_constructor_decl_error(p):
    '''constructor_decl : modifier ID error RPAREN block
                        | modifier ID error formals RPAREN block'''
    print("Syntax error in line %d: '(' needed" %p.lineno(1))

## formals 
def p_formals_single(p):
    '''formals : formal_param
               | formals COMMA formal_param'''
    if(len(p) < 3) :
        p[0] = p[1]
    else :
        if(p[1] == 'Correct' and p[3] == 'Correct') :
            p[0] = 'Correct' 
## formal_param
def p_formal_param(p):
    'formal_param : type variable'
    if(p[1] == 'Correct' and p[2] == 'Correct') :
        p[0] = 'Correct' 
    
## block
def p_block1_first(p):
    '''block1 : LBIG
              | block1 stmt'''
    if(len(p) == 3):
        if(p[1] == 'Correct' and p[2] == 'Correct') :
            p[0] = 'Correct'
    else :
        p[0] = 'Correct'
def p_block(p):
    'block : block1 RBIG'
    p[0] = p[1]

## stmt
#### summary
def p_stmt_summary(p):
    'stmt : noncompleteif_stmt'
    p[0] = p[1]
def p_stmt_summary1(p):
    'stmt : other_stmt'
    p[0] = p[1]
#### noncompleteif_stmt
###### if
def p_noncompleteif_if(p):
    'noncompleteif_stmt : IF LPAREN expr RPAREN stmt'
    p[0] = p[5]
    if(p[3] == 'Error'):
        p[0] = 'Error'
###### ifelse
def p_noncompleteif_ifelse(p):
    'noncompleteif_stmt : IF LPAREN expr RPAREN other_stmt ELSE noncompleteif_stmt'
    if(p[5] == 'Correct' and p[7] == 'Correct'):
        p[0] = 'Correct'
    if(p[3] == 'Error'):
        p[0] = 'Error' 
###### while
def p_noncompleteif__while(p): 
    'noncompleteif_stmt : WHILE LPAREN expr RPAREN noncompleteif_stmt'
    if(p[5] == 'Correct') :
        p[0] = 'Correct'
    if(p[3] == 'Error') :
        p[0] = 'Error'
###### for
def p_noncompleteif_for(p):
    'noncompleteif_stmt : forbasic noncompleteif_stmt'
    if(p[2] == 'Correct'):
        p[0] = 'Correct'
#### other_stmt 
###### complete_if
def p_other_stmt_complete_if(p):
    'other_stmt : IF LPAREN expr RPAREN other_stmt ELSE other_stmt'
    if(p[5] == 'Correct' and p[7] == 'Correct'):
        p[0] = 'Correct'
    if(p[3] == 'Error') :
        p[0] = 'Error'
###### while
def p_other_stmt_complete_while(p): 
    'other_stmt : WHILE LPAREN expr RPAREN other_stmt'
    p[0] = p[5]
    if(p[3] == 'Error') :
        p[0] = 'Error'
###### for
def p_forbasic1(p):
    '''forbasic1 : FOR LPAREN SEMICOLON
                 | FOR LPAREN stmt_expr SEMICOLON'''
    if(len(p) == 5) :
        p[0] = p[3]
    else :
        p[0] = 'Correct'
def p_forbasic2(p):
    '''forbasic2 : forbasic1 SEMICOLON
                 | forbasic1 expr SEMICOLON'''
    p[0] = p[1]
    if(p[2] == 'Error') :
        p[0] = 'Error'
def p_forbasic(p):
    '''forbasic : forbasic2 RPAREN
                | forbasic2 stmt_expr RPAREN'''
    if(len(p) == 4) :
        if(p[1] == 'Correct' and p[2] == 'Correct'):
            p[0] = 'Correct'
    else :
        p[0] = p[1]
def p_other_stmt_for(p):
    'other_stmt : forbasic other_stmt'
    if(p[1] == 'Correct' and p[2] == 'Correct') :
        p[0] = 'Correct'
###### return
def p_other_stmt_return(p):
    '''other_stmt : RETURN SEMICOLON
                  | RETURN expr SEMICOLON'''
    p[0] = 'Correct'
    if(p[2] == 'Error') :
        p[0] = 'Error'
def p_other_stmt_return_error(p):
    '''other_stmt : RETURN error
                  | RETURN expr error'''
    print("Syntax error in line %d: missing \';\'" %p.lineno(1))
###### stmt_expr
def p_other_stmt_stmt_expr(p): 
    'other_stmt : stmt_expr SEMICOLON'
    p[0] = p[1]
def p_other_stmt_stmt_expr_error(p):
    'other_stmt : stmt_expr error'
    print("Syntax error in line %d: missing \';\'" %p.lineno(1))
###### break
def p_other_stmt_break(p):
    'other_stmt : BREAK SEMICOLON'
    p[0] = 'Correct'
def p_other_stmt_break_error(p):
    'other_stmt : BREAK error'
    print("Syntax error in line %d: missing \';\'" %p.lineno(1))
###### continue
def p_other_stmt_continue(p):
    'other_stmt : CONTINUE SEMICOLON'
    p[0] = "Correct"
def p_other_stmt_continue_error(p):
    'other_stmt : CONTINUE error'
    print("Syntax error in line %d: missing \';\'" %p.lineno(1))
    
###### block
def p_other_stmt_block(p):
    'other_stmt : block'
    p[0] = p[1]
###### var_decl 
def p_other_stmt_var_decl(p):
    'other_stmt : var_decl'
    p[0] = p[1]   
    if(p[1] == 'Error'):
        p[0] = 'Error'
###### SEMICOLON
def p_stmt_semicolon(p):
    'other_stmt : SEMICOLON'
    p[0] = "Correct"
  
## literal
def p_literal(p):
    '''literal : INT_CONST
               | FLOAT_CONST
               | STRING_CONST
               | NULL
               | TRUE
               | FALSE'''
    p[0] = p[1]
      
## primary
#### iteral
def p_primary_literal(p):
    'primary : literal'
    p[0] = p[1]
#### this
def p_primary_this(p):
    'primary : THIS'
    p[0] = 0
#### super
def p_primary_super(p):
    'primary : SUPER'
    p[0] = 0
#### paren
def p_primary_paren(p):
    'primary : LPAREN expr RPAREN'
    p[0] = p[2]
    if(p[2] == 'Error'):
        p[0] = 'Error'
#### new
def p_primary_pnew1(p):
    'pnew1 : NEW ID'
    p[0] = p[2]
def p_primary_pnew(p):
    '''pnew : pnew1 LPAREN RPAREN
            | pnew1 LPAREN arguments RPAREN'''
    p[0] = p[1]
def p_primary_summary(p):
    'primary : pnew'
    p[0] = p[1]
#### lhs
def p_primary_lhs(p):
    'primary : lhs'
    p[0] = p[1]
#### method_invocation
def p_primary_method_invocation(p):
    'primary : method_invocation'
    p[0] = p[1]
    
## arguments
def p_argument_init(p):
    '''arguments : expr
                 | arguments COMMA expr'''
    p[0] = p[1]
      
## lhs                         need
def p_lhs_field(p):
    'lhs : field_access'
    p[0] = 0
    if(p[1] == 'Error'):
        p[0] = 'Error'
def p_lhs_array(p):
    'lhs : array_access'
    p[0] = 0
    if(p[1] == 'Error'):
        p[0] = 'Error'
  
## field_access                need
def p_field_access(p):
    'field_access : primary POINT ID'
    p[0] = 0
    if(p[1] == 'Error'):
        p[0] = 'Error'
def p_field_access_1(p):
    'field_access : ID'
    p[0] = 0
      
## array_access                need
def p_array_access(p):
    'array_access : primary LSQ expr RSQ'
    p[0] = 0
    if(p[len(p) - 2] == 'Error'):
        p[0] = 'Error'
    if(p[1] == 'Error'):
        p[0] = 'Error'

## method_invocation 
def p_method_invocation_noarg(p):
    'method_invocation : field_access LPAREN RPAREN'
    p[0] = 0
    if(p[1] == 'Error'):
        p[0] = 'Error'
def p_method_invocation_arg(p):
    'method_invocation : field_access LPAREN arguments RPAREN'
    p[0] = 0
    if(p[1] == 'Error'):
        p[0] = 'Error'
    
## expression
#### arith_op
def p_expr_arith_add(p):
    'expr : expr PLUS expr'
    p[0] = p[1] + p[3]
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
def p_expr_arith_minus(p): 
    'expr : expr MINUS expr'
    p[0] = p[1] - p[3]
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
def p_expr_arith_multi(p):
    'expr : expr MULTI expr'
    p[0] = p[1] * p[3]
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
def p_expr_airth_divede(p):
    'expr : expr DIVIDE expr'
    p[0] = p[1] / p[3]
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
#### bool_op
def p_expr_bool_and(p):
    'expr : expr AND expr'
    p[0] = bool(p[1] and p[3])
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
def p_expr_bool_or(p):
    'expr : expr OR expr'
    p[0] = bool(p[1] or p[3])
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
def p_expr_bool_equal(p):
    'expr : expr EQUAL expr'
    p[0] = bool(p[1] == p[3])
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
def p_expr_bool_notequal(p):
    'expr : expr NOTEQUAL expr'
    p[0] = bool(p[1] != p[3])
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
def p_expr_bool_less(p):
    'expr : expr LESS expr'
    p[0] = bool(p[1] < p[3])
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
def p_expr_bool_greater(p):
    'expr : expr GREATER expr'
    p[0] = bool(p[1] > p[3])
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
def p_expr_bool_lessequal(p):
    'expr : expr LESSEQUAL expr'
    p[0] = bool(p[1] <= p[3])
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
def p_expr_bool_greaterequal(p):
    'expr : expr GREATEREQUAL expr'
    p[0] = bool(p[1] >= p[3])
    if(p[1] == 'Error' or p[3] == 'Error'):
        p[0] = 'Error'
#### primary
def p_expr_primary(p):
    'expr : primary'
    p[0] = p[1]
#### assign
def p_expr_assign(p):
    'expr : assign'
    p[0] = p[1]
#### newarray
def p_expr_newarray(p):
    'expr : newarray'
    p[0] = p[1]
#### unary
def p_expr_uminus(p):
    'expr : MINUS expr %prec UMINUS'
    p[0] = -p[2]
    if(p[2] == 'Error'):
        p[0] = 'Error'
def p_expr_uplus(p):
    'expr : PLUS expr %prec UPLUS'
    p[0] = p[2]
    if(p[2] == 'Error'):
        p[0] = 'Error'
def p_expr_not(p):
    'expr : NOT expr %prec NOT'
    p[0] = not bool(p[2])
    if(p[2] == 'Error'):
        p[0] = 'Error'
  
 
## newarray
def p_newarray(p):
    '''newarray : newarrayp
                | newarrayw'''
    p[0] = 'Correct'
    if(p[1] == 'Error') :
        p[0] = 'Error'
def p_newarrayw(p):
    '''newarrayw : newarrayw LSQ RSQ
                 | newarrayp LSQ RSQ'''
    p[0] = 'Correct'
    if(p[1] == 'Error') :
        p[0] = 'Error'
def p_newarrayp(p):
    '''newarrayp : NEW type LSQ expr RSQ
                 | newarrayp LSQ expr RSQ'''
    p[0] = 'Correct'
    if(p[len(p) - 2] == 'Error') :
        p[0] = 'Error'
    if(p[1] == 'Error') :
        p[0] = 'Error'
def p_newarray_error_1(p):
    '''newarrayp : NEW type error expr RSQ'''
    print("Syntax error in line %d: '[' needed" %p.lineno(1))
    p[0] = 'Error'
def p_newarray_error_2(p):
    '''newarrayp : NEW type LSQ expr error'''
    print("Syntax error in line %d: ']' needed" %p.lineno(1))
    p[0] = 'Error'
          
## assign
def p_assign_normal(p):
    'assign : lhs ASSIGN expr'
    p[0] = p[3]
    p[1] = p[3]
    if(p[1] == 'Error'):
        p[0] = 'Error'
    if(p[3] == 'Error'):
        p[0] = 'Error'
def p_assign_dadd(p):
    'assign : lhs INCREMENT'
    p[0] = p[1];
    p[1] = p[1] + 1;
    if(p[1] == 'Error'):
        p[0] = 'Error'
def p_assign_bdadd(p):
    'assign : INCREMENT lhs'
    p[0] = p[2] + 1;
    p[2] = p[2] + 1;
    if(p[2] == 'Error'):
        p[0] = 'Error'
def p_assign_dminus(p):
    'assign : lhs DECREMENT'
    p[0] = p[1];
    p[1] = p[1] - 1;
    if(p[1] == 'Error'):
        p[0] = 'Error'
def p_assign_bdminus(p):
    'assign : DECREMENT lhs'
    p[0] = p[2] - 1;
    p[2] = p[2] - 1;    
    if(p[2] == 'Error'):
        p[0] = 'Error'
    
## stmt_expr
def p_stmt_expr_assign(p):
    'stmt_expr : assign'
    p[0] = p[1]
    if(p[1] != 'Error' and p[1] != None) :
        p[0] = 'Correct'
def p_stmt_expr_method_invocation(p):
    'stmt_expr : method_invocation'
    p[0] = p[1]
    if(p[1] != 'Error' and p[1] != None) :
        p[0] = 'Correct'
def p_stmt_expr_error(p):
    'stmt_expr : error'
    print("Syntax error in line %d: statement expression syntax error!" %p.lineno(1))

def p_error(p):
    return
    

# Build the parser
