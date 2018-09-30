# Yacc example
import ply.yacc as yacc
from copy import deepcopy

test=1

quad=[]
l1=[]

lcount=1

vcount=1

# Get the token map from the lexer.  This is required.
from lex_py import tokens
from lex_py import init_symbol_table
import lex_py
from lex_py import l_sym
from lex_py import current_level

start = 'class_declaration'
use_level = -1;
def p_class_declaration(p):
    'class_declaration : public class ID LBRACE field_declaration cont_field RBRACE'
    print('No error while generating intermediate code.')
def p_cont_field(p):
    '''cont_field : field_declaration cont_field
       |'''
def p_field_declaration(p):
    '''field_declaration : method_declaration
    | constructor_declaration
    | variable_declaration 
    | static statement_block
    | SEMICOLON'''
    #print('f declare')
def p_constructor_declaration(p):
    '''constructor_declaration : public ID LPAREN parameter_list RPAREN statement_block
    | public ID LPAREN RPAREN statement_block'''
def p_method_declaration(p):
    '''method_declaration : public type ID LPAREN parameter_list RPAREN statement_block
    | public type ID LPAREN RPAREN statement_block
    | public type ID LPAREN parameter_list RPAREN SEMICOLON
    | public type ID LPAREN RPAREN SEMICOLON
    | public static void main LPAREN String LBRACKET RBRACKET ID RPAREN statement_block
    '''
    #TODO: Add parameter list
    #print('m declare')

def p_statement_block(p):
    'statement_block : LBRACE statement statement_cont RBRACE'
    #lex_py.current_level += 1 
    #print('stmt block')
def p_statement_cont(p):
    '''statement_cont : statement statement_cont
       |'''
def p_statement(p):#TODO
    '''statement : variable_declaration
      | expression SEMICOLON 
      | statement_block 
      | if_statement 
      | for_statement 
      | return expression SEMICOLON
      | return SEMICOLON
      | ID COLON statement 
      | break ID SEMICOLON
      | break SEMICOLON
      | continue ID SEMICOLON 
      | continue SEMICOLON 
      | SEMICOLON 
    '''

    # '''statement : 
    #   variable_declaration
    #   | expression SEMICOLON 
    #   | statement_block 
    #   | if_statement 
    #   | for_statement 
    #   | return expression SEMICOLON
    #   | return SEMICOLON
    #   | ID COLON statement 
    #   | break ID SEMICOLON
    #   | break SEMICOLON
    #   | continue ID SEMICOLON 
    #   | continue SEMICOLON 
    #   | SEMICOLON 
    #   '''
    #print('stmt')

def p_variable_declaration(p):
    '''variable_declaration : public type variable_declarator cont_var_dec
    | type variable_declarator cont_var_dec '''
    #print("in PVD", list(p))
    global use_level
    #global lex_py.current_level;
    varib = p[2] 
    if(p[3] != None):
    	varib += p[3]
    #print(l_sym[use_level])
    #lex_py.display()
    #print("The CL is: ",use_level)
    for i in varib:
    	if(i[1] != None):
    		if(str(i[1]).find(p[1]) == -1):
    			p_error(p)
    #	print("i is: ", i)
    #	print(type(i[1]))
    	l_sym[use_level][i[0]]['data_type'] = p[1]
    #print(l_sym[use_level])
    
    	#print(i)
def p_cont_var_dec(p):
    '''cont_var_dec : COMMA variable_declarator cont_var_dec
    | SEMICOLON'''
    if(p[1] != ';'):
    	if(p[0] == None):
        	p[0] = list()
    	#p[0] += p[2]
    	if(p[2] != None):
    		p[0] += p[2]
    	if(p[3] != None):
    		p[0] += p[3]
    #print("IN CVD",list(p))
def p_variable_declarator(p):
    '''variable_declarator : ID LBRACKET RBRACKET cont_var_declarator
    | ID cont_var_declarator'''
    global use_level
    if(p[2] != '['):
    	if(p[0] == None):
    		p[0] = list()
    	p[0].append([p[1],p[2]])
		#p[0] += p[2]
    	
    	use_level = lex_py.current_level
    else:
    	if(p[0]== None):
    		p[0] = list()
    	p[0].append([p[1],p[4]])
    	use_level = lex_py.current_level
    #print("in PVDR",list(p))
def p_cont_var_declarator(p):    
    '''cont_var_declarator : EQUAL variable_initializer
    | '''
    if(len(list(p)) > 1):
    	p[0] = p[2]


def p_variable_initializer(p):
    '''variable_initializer : expression'''
    p[0] = p[1]



def p_expression(p):
    '''expression : numeric_expression
    | testing_expression
    | ID
    | REAL_NUMBER
    | NUMBER
    | LPAREN expression RPAREN
    | expression LPAREN exp_cont RPAREN 
    '''
    global l1


    if (p[1]!=None):
        l1.append(p[1])

    p[0] = type(p[1])
    #print("exp")
    #   | logical_expression 
    #   | string_expression                            
    #   | casting_expression 
    #   | creating_expression 
    #   | literal_expression 
    #   | "null"
    #   | "this" 
    #   | ( "(" expression ")" ) 
    #   | ( expression 
    #   ( ( "(" [ arglist ] ")" ) 
    #   | ( "[" expression "]" ) 
    #   | ( "." expression ) 
    #   | ( "," expression ) 
    #   ) ) '''
def p_exp_cont(p):
    '''exp_cont : arglist
       |'''


def p_numeric_expression(p):
    '''numeric_expression : MINUS expression
    | DBPLUS expression
    | DBMINUS expression 
    | expression DBPLUS
    | expression DBMINUS 
    | expression operator expression 
    '''
    global l1
    global vcount

    l=list(p)

    #print("===========================")
    #print(l)
    #print("+++++++++++++++++++++++++++++++++++")

    q=[]
    #print("---------------")
    #print(l)
    #print("++++++++++++++++++")

    if (p[2]=="++"):

    #	print("In ++")
	#print("l1: ",l1)
	res = str("t"+str(vcount))
	vcount+=1
	#res1 = str("t"+str(vcount))
	#vcount+=1
	q=["+", l1[0], 1, res]
	quad.append(q)
	#print(q)
	q=["=", res, None, l1[0]]
    	#print(q)
	quad.append(q)
        l1.pop()
        #print("out of quad")
    elif (p[2]=="--"):


	res = str("t"+str(vcount))
	vcount+=1
	#res1 = str("t"+str(vcount))
	#vcount+=1
	q=["-", l1[0], 1, res]
	quad.append(q)
	#print(q)
	q=["=", res, None, l1[0]]
    	#print(q)
	quad.append(q)
        l1.pop()


    elif(p[2]=="="):
    	#print(l1)
        q.append("=")
        q.append(l1[1])
        q.append(None)
        q.append(l1[0])

        quad.append(q)

        l1=[]


    else:
	res = str("t"+str(vcount))
	vcount+=1
	arg1=l1.pop()
	arg2=l1.pop()
	l1.append(res)
	op=p[2]


		#print("res ", res)
		#print("arg1 ", arg1)
		#print("arg2 ", arg2)
		#print("op ", op)


	q.append(op)
	q.append(arg1)
	q.append(arg2)
	q.append(res)

	quad.append(q)



    #print('numeric exp')

def p_operator(p):
    '''operator : MINUS 
      | PLUS 
      | DIVIDE 
      | MODULO
      | TIMES
      | PLEQUAL
      | MIEQUAL
      | MTEQUAL
      | DIEQUAL
      | MOEQUAL
      | EQUAL
    '''
    p[0] = p[1]
    #print('operator')

def p_type(p):
    'type : type_specifier'
    p[0] = p[1]
    #print(p[0])
    #print('type')

def p_type_specifier(p):
    '''type_specifier : boolean 
    | byte
    | void 
    | char 
    | short 
    | int 
    | float 
    | long 
    | double 
    | class_name'''
    p[0] = p[1]
    #print(p[0])
    #print('type specifier')

def p_class_name(p):
    'class_name : ID'
    #print("Class name")

def p_arglist(p):
    '''arglist : expression cont_arglist'''
def p_cont_arglist(p):
    '''cont_arglist : COMMA expression cont_arglist
    |'''
def p_testing_expression(p):
    '''testing_expression : expression GT expression
    | expression LT expression
    | expression GTE expression
    | expression LTE expression
    | expression DBEQUAL expression
    | expression NEQUAL expression'''


    q=[]
    global quad
    global vcount
    global l1

    l=list(p)

    #print(l)

    if (p[2]!="="):


		res = str("t"+str(vcount))
		vcount+=1
		arg1=l1.pop()
		arg2=l1.pop()
		l1.append(res)
		op=p[2]

		q.append(op)
		q.append(arg1)
		q.append(arg2)
		q.append(res)
		quad.append(q)
		#print(quad)


    #print("te")
def p_parameter_list(p):
    '''parameter_list : parameter cont_param'''
def p_cont_param(p):
    '''cont_param : COMMA parameter cont_param
    |'''
def p_parameter(p):
    '''parameter : type ID
       | type ID LBRACKET RBRACKET''' 
def p_if_statement(p):
    '''if_statement : if LPAREN if_part_1 RPAREN statement action1
    | if LPAREN if_part_1 RPAREN statement action1 else statement action2'''
    #lex_py.current_level += 1
    #print("if statement")
    #print(list(p))
    if (len(list(p))==7):
        #if - else
    	quad.pop(len(quad)-2)
        pass
def p_if_part_1(p):
    '''if_part_1 : expression
    '''
    global l1


    global quad
    q=["ifFalse", l1[0], "goto", str("L"+str(lcount))]
    quad.append(q)
    l1.pop()
def p_action1(p):
    '''action1 : '''
    global lcount
    global quad



    label=(str("L"+str(lcount)))

    lcount+=1



    q=["goto",None,None,str("L"+str(lcount))]

    quad.append(q)

    q=["Label",None,None,label]
    quad.append(q)    

def p_action2(p):
    '''action2 : '''
    global lcount
    global quad

    label=(str("L"+str(lcount)))
    lcount+=1

    #q=["goto",None,None,str("L"+str(lcount))]
    #quad.append(q)

    q=["Label",None,None,label]
    quad.append(q) 
    
def p_for_statement(p):
    'for_statement : for LPAREN for_part_1 for_part_2 SEMICOLON for_part_3 RPAREN statement'
   # print("FOR CL",lex_py.current_level)
    #lex_py.current_level += 1
    #print("FOR CL AFTER",lex_py.current_level)    
	#print("for stmt")

    global lcount
    global quad

    label=(str("L"+str(lcount)))
    lcount+=1

    q=["goto",None,None,str("L"+str(lcount-2))]
    quad.append(q)

    q=["Label",None,None,label]
    quad.append(q)


def p_for_part_1(p):
    '''for_part_1 : variable_declaration
       | expression SEMICOLON
       | SEMICOLON'''
    global lcount
    label=(str("L"+str(lcount)))
    lcount+=1

    q=["Label",None,None,label]
    quad.append(q)

    #print("fp1")
def p_for_part_2(p):
    '''for_part_2 : expression
       |'''
    #print("fp2")

    global l1


    global quad
    q=["ifFalse", l1[0], "goto", str("L"+str(lcount))]
    quad.append(q)
    l1.pop()

def p_for_part_3(p):
    '''for_part_3 : expression
       |'''
    #print("fp2")


def p_error(p):
    print(p)
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

init_symbol_table()

#display()

# while True:
#    try:
#        s = input('java > ')
#    except EOFError:
#        break
#    if not s: 
#        continue
#    result = parser.parse(s)
#    print(result)

s = '''
public class abc {
    public static void main(String[] args){

	int i;

	q=1+2+2;

        a=q+1;

	for (i=0; i<10; i++)
	{
		int z,x,y;
		z=x+y;
	}

	for (j=0; j<100; j++)
	{
		int h,v;
		h=h+v;
	}
        if(a>q)	
	{
		a = a+1;
	}
	}


}    
'''
result = parser.parse(s)

print("\n")

def print_quad():
	global quad
	print("QUAD TABLE\n")
	for i in range(0, len(quad)):
	    print(i, "  ", quad[i])
#print_quad()

def make_leaders():
	global quad
	temp_quad=deepcopy(quad)
	leaders=[0]
	blocks=[]
	for i in range(0, len(quad)):
		if (quad[i][0]=="goto"):
			leaders.append(i+1)
		elif (quad[i][0]=="Label"):
			leaders.append(i)
	fin=list(set(leaders))
	fin.sort()
	return fin

def make_blocks():
	global quad
	blocks=[]
	fin=make_leaders()

	for i in range(0, len(fin)-1):
		q=[fin[i], fin[i+1]-1]
		blocks.append(q)
	blocks.append([fin[-1], len(quad)-1])

	return blocks

def optimization():

	global quad

### Constant Folding and Constant Propogation
	blocks=make_blocks()

	for i in range(len(blocks)):
		constant_folding(blocks[i])
		const_prop(blocks[i])
		blocks=make_blocks()
	#print(blocks)

### Loop Optimization

	
	#print(blocks)

	# Create a list of loops.
	l_loop = loop_block(blocks)
	for i in range(len(l_loop)):
		loop_op(l_loop[i])
		l_loop = loop_block(blocks)

def loop_block(blocks):
	blocks=make_blocks()
	l_loop = []
	for i in blocks:
		if (i[0]==i[1]):
			pass

		if ( (quad[i[0]][0] == "Label") and (quad[i[0]][3] == quad[i[1]][3]) and quad[i[1]][0] == "goto" ):
			l_loop.append(i)
	#print("lloop is: ",l_loop)
	return l_loop	
	

def loop_op(block):
	
	global quad

	start = block[0]
	end = block[1]
	if(quad[start+1][1] % 2 !=0):
		return 
	quad[start+1][1] /= 2
	i = start + 5
	dup = []
	while( i < end):
		dup.append(quad[i])
		i+=1
	#print(dup)

	for i in dup:
		quad.insert(end-1, i)



def check(num):
	if ( (str(type(num))=="<type 'int'>") or (str(type(num))=="<type 'float'>") ):
		return True
	return False


def constant_folding(block):
	global quad

	#print(block)

	start = block[0]
	end = block[1]
	for i in range(start,end+1):
		if(quad[i][0] == '+' or quad[i][0] == '-' or quad[i][0] == '*' or quad[i][0] == '/'):
			if(check(quad[i][1]) and check(quad[i][2])):
				if(quad[i][0]== '+'):
					val = quad[i][2] + quad[i][1]
				elif(quad[i][0]== '-'):
					val = quad[i][2] - quad[i][1]
				elif(quad[i][0]== '*'):
					val = quad[i][2] * quad[i][1]
				elif(quad[i][0]== '/'):
					if (quad[i][1]==0):
						p_error("divide by zero error")
					else:
						val = quad[i][2] / quad[i][1]

				quad[i][0] = '='
				quad[i][1] = val
				quad[i][2] = None


def const_prop(block):
	global quad

	start=block[0]
	end=block[1]

	l_const=[]
	done_var=[]

	#print(quad)

	for i in range (0, len(quad)):
		if ((quad[i][0]=="=") and check(quad[i][1])):
			#if (quad[i][3][0]=='t'):
			l_const.append([quad[i][3], quad[i][1]])

	while(True):
		for i in range(0, len(l_const)):
			#print(l_const[i])
			if (l_const[i] in done_var):
				pass

			for j in range(0, len(quad)):

				if (quad[j][1]==l_const[i][0]):
					quad[j][1]=l_const[i][1]

				elif (quad[j][2]==l_const[i][0]):
					quad[j][2]=l_const[i][1]


		done_var+=l_const		
		dum=[]
		for i in done_var:
			if i not in dum:
				dum.append(i)
		done_var=deepcopy(dum)
		
		l_const=[]

		constant_folding(block)


		for i in range (0, len(quad)):
			if ((quad[i][0]=="=") and check(quad[i][1])):
				#if (quad[i][3][0]=='t'):
				l_const.append([quad[i][3], quad[i][1]])
		#print(l_const)
		#print(done_var)
		if (len(l_const)==len(done_var)):
			break

	#print("++++++++++++++++++++++++++++++++++++")
	#print(done_var)
	rem_ind=[]
	for i in done_var:
		for j in range (0, len(quad)):
			if (i[0]==quad[j][3]):
				if (quad[j][3][0]=='t'):
					rem_ind.append(j)
	rem_ind.sort(reverse=True)

	for i in rem_ind:
		quad.pop(i)

	

print_quad()
optimization()
print_quad()
lex_py.display()
