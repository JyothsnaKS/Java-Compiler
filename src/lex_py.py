from __future__ import print_function
import ply.lex as lex

current_level = -1 #At 0 symbol_table will have the keywords
l_sym = []

# List of reserved words
reserved = [
   'short','return', 'if', 'then', 'else', 'for', 'long', 'int', 'float', 'double', 'void', 'main', 'String', 'new', 'static', 'break', 'boolean', 'byte','char','class', 'continue','final', 'import', 'public', 'private','protected','println','next','nextInt','nextFloat','nextDouble','Scanner'
]

# List of token names. Always required
tokens = [
   'NUMBER', 'REAL_NUMBER',
   'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',
   'PLEQUAL','MIEQUAL','MTEQUAL', 'DIEQUAL', 'MOEQUAL',
   'LT', 'GT', 'LTE', 'GTE',
   'LPAREN', 'RPAREN',
   'STRING', 'CHAR',
   'ID',
   'DBEQUAL','NEQUAL',
   'EQUAL',
   'SEMICOLON', 'COMMA', 'COLON',
   'LBRACE', 'RBRACE',
   'DBPLUS', 'DBMINUS',
   'LBRACKET', 'RBRACKET'
] + reserved

# Regular expression rules for simple tokens
t_DBEQUAL = r'=='
t_NEQUAL = r'!='
t_DBPLUS  = r'\+\+'
t_DBMINUS = r'--'
t_LT      = r'<'
t_GT      = r'>'
t_LTE     = r'<='
t_GTE     = r'>='
t_EQUAL   = '='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MODULO  = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_SEMICOLON = r';'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA   = r','
t_COLON = r':'
t_PLEQUAL = r'\+='
t_MIEQUAL = r'-='
t_MTEQUAL = r'\*='
t_DIEQUAL = r'/='
t_MOEQUAL = r'%='

# Check for multi line comments	
def t_ignore_multi_comments(t):
	r'/\*(\s|.|\n)*\*/'

# Check for single line comments	
def t_ignore_single_comments(t):
	r'//.*\n'

def t_STRING(t):
	r'".*"'
	return t

def t_CHAR(t):
	r'\'.\''
	return t
	
def t_ID(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	if t.value in reserved:
		t.type = t.value
		return t
	if t.value not in l_sym[current_level].keys():
		#print("In lex",current_level,t.value)
		symbol_table_entry = dict()
		symbol_table_entry['token_type'] = 'ID' 
		symbol_table_entry['data_type'] = None    
		symbol_table_entry['value'] = None
		symbol_table_entry['lineno'] = t.lineno
		symbol_table_entry['lexpos'] = t.lexpos			
		l_sym[current_level][t.value] = symbol_table_entry
		
	return t

# A regular expression for float
def t_REAL_NUMBER(t):
	r'\d+\.\d+'
	t.value = float(t.value)   
	return t

# A regular expression for integers
def t_NUMBER(t):
	r'\d+'  
	t.value = int(t.value) 
	return t

def t_LBRACE(t):
	r'{'
	global current_level
	current_level = current_level + 1
	symbol_table = dict()
	l_sym.append(symbol_table)#
	return t
	
def t_RBRACE(t):
	r'}'
	#display()
	global current_level
	current_level = current_level - 1
	#print("in RB",len(l_sym[-1].keys()))
	if(len(l_sym[-1].keys()) == 0):
		del l_sym[-1]
	return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character "+t.value[0])
    t.lexer.skip(1)

# Init symbol_table
def init_symbol_table():
	global current_level

	current_level +=1
	symbol_table = dict()
	l_sym.append(symbol_table)

	for keyword in reserved:
		l_sym[0][keyword]= {'token_type':'KEYWORD'}

# Tokenize input
def get_tokens():	
	while True:
		tok = lexer.token()
		if not tok: 
			break      # No more input
		print(tok)

def display():
	print('SYMBOL TABLE:\n')
	#Prints symbol_table
	for i in range(len(l_sym)):
		print(str(i+1)+':')
		entry = l_sym[i]
		for key in entry:
			print(key+': ',end='')
			print(entry[key])
		print('\n')
		
data = '''
public class abc {
    public static void main(String[] args){
      int a,b,c;
      for(int i = 0; i < 10; i++)
      {
          int d;
      }
      if( 1 > 2)
      {
          int hiran;
      }
    }
    public int name(int a)
    {
        int j;
        return j;
    }
}    
'''

#init_symbol_table()

# Build the lexer
lexer = lex.lex()

# Give the lexer the input
#lexer.input(data)

#get_tokens()

#display()
