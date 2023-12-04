import ply.lex as lex

reservado = {
    'varint' : 'INTEIRO',
    'varfloat' : 'REAL',
    'varchar' : 'CARACTERE',
    'in' : 'ENTRADA',
    'out' : 'SAIDA',
    'if' : 'SE',
    'else' : 'SENAO',
    'while' : 'ENQUANTO',
    'for' : 'DURANTE',
    'and' : 'E',
    'or' : 'OU',
    'not' : 'NAO',

}

tokens = [
    'ATRIBUI',
    'IGUALDADE',
    'MAIORIGUAL',
    'MENORIGUAL',
    'MENOR',
    'MAIOR',
    'DIFERENTE',   
    'SOMA',
    'SUBTRACAO', 
    'MULTIPLICACAO', 
    'DIVISAO',
    'RESTO', 
    'SEPARADOR',
    'ABREPARENTESES',
    'FECHAPARENTESES',
    'PONTOEVIRGULA',
    'ASPAS',
    'COMECO',
    'FIM',
    'INTEIRODEF',
    'REALDEF',
    'CARACTEREDEF',
    'VAR',
    'VARDEF',
] + list(reservado.values())

t_ATRIBUI = r':='
t_IGUALDADE = r'==' 
t_MAIORIGUAL = r'<='  
t_MENORIGUAL = '>='
t_MENOR = r'<'
t_MAIOR = r'>'
t_DIFERENTE = r'\!\!'
t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_RESTO = r'/='
t_SEPARADOR = r'\.'
t_ABREPARENTESES = r'\(' 
t_FECHAPARENTESES = r'\)'
t_PONTOEVIRGULA = r'\;'
t_ASPAS = r'\"'
t_COMECO = r'\{'
t_FIM = r'\}'

def t_REALDEF(t):
    r'[+|-]?\d+\.\d+'
    #r'[+|-]?\d+' + t_SEPARADOR + r'\d+' 
    t.type = reservado.get(t.value, 'REALDEF')
    return t

def t_INTEIRODEF(t):
    r'[+|-]?\d+' 
    t.type = reservado.get(t.value, 'INTEIRODEF')
    return t




def t_CARACTEREDEF(t):
    r'\'[a-zA-Z0-9]\''
    t.type = reservado.get(t.value, 'CARACTEREDEF')
    return t

def t_VAR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reservado.get(t.value, 'VAR')
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Define a rule so we can track line numbers
def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

# Error handling rule       
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()