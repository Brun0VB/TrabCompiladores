import sys
import ply.yacc as yacc

from cpm_lex import tokens

Variaveis = []

#CODIGO INICIAL
def p_main(p):
    'programa : expressoes'
    f = open("codigogerado.c", "w")
    f.write(f"#include <stdio.h>\n#include <math.h>\n\nint main(){{\n   {p[1]}\n   return 0;\n}}")
    f.close()

#NENHUMA, UMA OU MAIS EXPRESSOES
def p_expressao_void(p):
    '''
    expressoes :  
    '''
    p[0] = ""


def p_expressao(p):
    '''
    expressoes : expressao
    '''
    p[0] = p[1] + f'\n   '


def p_expressoes(p):
    '''
    expressoes : expressoes expressao  
    '''
    p[0] = p[1] + p[2] + f'\n   '

#TIPO
def p_tipo(p):
    '''
        tipo : INTEIRO 
             | REAL
             | CARACTERE
    '''
    p[0] = p[1]

#DECLARACAO VARIAVEL
def p_vardef(p):
    '''
        expressao : tipo VAR
    '''
    match p[1]:
        case 'varint':
            p[0] = f'int {p[2]};'
            Variaveis.append({'name': p[2], 'type': p[1], 'value': None})
        case 'varfloat':
            p[0] = f'float {p[2]};'
            Variaveis.append({'name': p[2], 'type': p[1], 'value': None})               
        case 'varchar':
            p[0] = f'char {p[2]};'
            Variaveis.append({'name': p[2], 'type': p[1], 'value': None})

#ATRIBUICOES INT, FLOAT, CHAR, VAR
def p_atribuicao_int(p):
    '''
        expressao : VAR ATRIBUI INTEIRODEF
    '''
    index = verificaVar(p[1])
    if index != -1:
        if(Variaveis[index]['type'] == 'varint'):           
            Variaveis[index]['value'] = p[3]
            p[0] = f'{p[1]} = {p[3]};'
        else:
            print('Erro: variavel do tipo errado')
            sys.exit(1)
    
def p_atribuicao_float(p):
    '''
        expressao : VAR ATRIBUI REALDEF
    '''
    index = verificaVar(p[1])
    if index != -1:
        if(Variaveis[index]['type'] == 'varfloat'):           
            Variaveis[index]['value'] = p[3]
        else:
            print('Erro: variavel do tipo errado')
            sys.exit(1)

    p[0] = f'{p[1]} = {p[3]};'


def p_atribuicao_char(p):
    '''
        expressao : VAR ATRIBUI CARACTEREDEF
    '''
    index = verificaVar(p[1])
    if index != -1:
        if(Variaveis[index]['type'] == 'varchar'):           
            Variaveis[index]['value'] = p[3]
        else:
            print('Erro: variavel do tipo errado')
            sys.exit(1)

    p[0] = f'{p[1]} = {p[3]};'


def p_atribuicao_var(p):
    '''
        expressao : VAR ATRIBUI VAR
    '''
    index = verificaVar(p[1])
    index2 = verificaVar(p[3])
    if index != -1:
        if index2 != -1:
            if(Variaveis[index]['type'] == Variaveis[index2]['type']):           
                Variaveis[index]['value'] = Variaveis[index2]['value']
            else:               
                print('Erro: variavel do tipo errado')
                sys.exit(1)               

    p[0] = f'{p[1]} = {p[3]};'

#ARITMETICOS
def p_operacao(p):
    '''
    expressao : VAR ATRIBUI VAR aritmeticos 
    '''
    index = verificaVar(p[1])
    index2 = verificaVar(p[3])
    if index != -1:
        if index2 != -1:
            p[0] = f'{p[1]} = {p[3]}' + p[4] + f';'


def p_aritmeticos_void(p):
    '''
    aritmeticos :   
    '''
    p[0] = ""


def p_aritmeticos(p):
    '''
    aritmeticos : aritmetico 
    '''
    p[0] = p[1] 


def p_aritmeticos_concatenacao(p):
    '''
    aritmeticos : aritmeticos aritmetico 
    '''
    p[0] = p[1] + p[2]


def p_aritmetico(p):
    '''
    aritmetico : SOMA VAR
               | SUBTRACAO VAR
               | MULTIPLICACAO VAR
               | DIVISAO VAR
               | RESTO VAR
    '''
    index = verificaVar(p[2])
    if index != -1:
        match p[1]:
            case '+':
                p[0] = f' + {p[2]}' 
            case '-':
                p[0] = f' - {p[2]}'
            case '*':
                p[0] = f' * {p[2]}'
            case '/=':
                p[0] = f' % {p[2]}'
            case '/':
                p[0] = f' / {p[2]}'
        

#RELACIONAIS
def p_relacao(p):
    '''
        relacao : VAR IGUALDADE VAR
                | VAR MAIOR VAR
                | VAR MENOR VAR
                | VAR MAIORIGUAL VAR
                | VAR MENORIGUAL VAR
                | VAR DIFERENTE VAR
    '''
    match p[2]:
        case '==':
            p[0] = f'{p[1]} == {p[3]}'
        case '>':
            p[0] = f'{p[1]} > {p[3]}'
        case '<':
            p[0] = f'{p[1]} < {p[3]}'
        case '>=':
            p[0] = f'{p[1]} >= {p[3]}'
        case '<=':
            p[0] = f'{p[1]} <= {p[3]}'
        case '!!':
            p[0] = f'{p[1]} != {p[3]}'


#LOGICOS
def p_teste(p):
    '''
    teste : relacao logicos
          | negacao logicos
    '''
    p[0] = p[1] + p[2]

def p_logicos_void(p):
    '''
    logicos :   
    '''
    p[0] = ""


def p_logicos(p):
    '''
    logicos : logico
    '''
    p[0] = p[1] 


def p_logicos_concatenacao(p):
    '''
    logicos : logicos logico 
    '''
    p[0] = p[1] + p[2]

def p_logico(p):
    '''
    logico : E relacao
           | E negacao
           | OU relacao
           | OU negacao
    '''
    match p[1]:
        case 'and':
            p[0] = f' && {p[2]}'
        case 'or':
            p[0] = f' || {p[2]}'

def p_negacao(p):
    '''
    negacao : NAO VAR
    '''
    index = verificaVar(p[2])
    if index != -1:        
        p[0] = f'!{p[2]}'    


#ENTRADA E SAIDA
def p_admissao(p):
    '''
    expressao : ENTRADA ABREPARENTESES VAR FECHAPARENTESES
    '''
    index = verificaVar(p[3])
    if index != -1:
        match Variaveis[index]['type']:
            case 'varint':
                p[0] = f'scanf("%d", &{p[3]});'
            case 'varfloat':
                p[0] = f'scanf("%f", &{p[3]});'
            case 'varchar':
                p[0] = f'scanf("%c", &{p[3]});'

def p_retirada(p):
    '''
    expressao : SAIDA ABREPARENTESES VAR FECHAPARENTESES
    '''
    index = verificaVar(p[3])
    if index != -1:
        match Variaveis[index]['type']:
            case 'varint':
                p[0] = f'printf("%d\\n",{p[3]});'
            case 'varfloat':
                p[0] = f'printf("%f\\n",{p[3]});'
            case 'varchar':
                p[0] = f'printf("%c\\n",{p[3]});'

#IF ELSE
def p_condicional(p):
    '''
    expressao : SE ABREPARENTESES teste FECHAPARENTESES COMECO expressoes FIM
    '''
    p[0] = f'if({p[3]}){{\n   {p[6]}}}'

def p_alternativo(p):
    '''
    expressao : SE ABREPARENTESES teste FECHAPARENTESES COMECO expressoes FIM SENAO COMECO expressoes FIM
    '''
    p[0] = f'if({p[3]}){{\n   {p[6]}}}\n'
    p[0] += f'   else{{\n   {p[10]}}}'


#WHILE
def p_repeticaoenquanto(p):
   '''
   expressao : ENQUANTO ABREPARENTESES teste FECHAPARENTESES COMECO expressoes FIM 
   '''
   p[0] = f'while({p[3]}){{\n   {p[6]}}}'


#FOR
def p_maismenos(p):
    '''
    maismenos : SOMA
              | SUBTRACAO
    '''
    p[0] = p[1]

def p_comparacao(p):
    '''
    comparacao : MAIOR
               | MENOR
               | MAIORIGUAL
               | MENORIGUAL
    '''
    p[0] = p[1]


def p_repeticaodurante(p):
    '''
    expressao : DURANTE ABREPARENTESES INTEIRODEF PONTOEVIRGULA maismenos PONTOEVIRGULA INTEIRODEF PONTOEVIRGULA comparacao PONTOEVIRGULA INTEIRODEF FECHAPARENTESES COMECO expressoes FIM
    '''
    p[0] = f'for(int i = {p[3]}; i {p[9]} {p[11]}; i {p[5]}= {p[7]}){{\n   {p[14]}}}'  #for(int i = 0, i < 10, i++)
    

#VERIFICAR SE A VARIAVEL EXISTE NO VETOR 
def verificaVar(name):
    index = 0
    for v in Variaveis:
        if v['name'] == name:
            return index
        index += 1
    return -1


parser = yacc.yacc()

from exemplos import interpretar

resultado = parser.parse(interpretar)