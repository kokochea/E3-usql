from ply import *
import ply.lex as lex
import ply.yacc as yacc
import numpy as np

reserved = {
    'TRAEME': 'TRAEME',
    'TODO': 'TODO',
    'DE LA TABLA': 'DE_LA_TABLA',
    'DONDE': 'DONDE',
    'AGRUPANDO POR': 'AGRUPANDO_POR',
    'MEZCLANDO': 'MEZCLANDO',
    'EN': 'EN',
    'LOS DISTINTOS': 'LOS_DISTINTOS',
    'CONTANDO': 'CONTANDO',
    'METE EN': 'METE_EN',
    'LOS VALORES': 'LOS_VALORES',
    'ACTUALIZA': 'ACTUALIZA',
    'SETEA': 'SETEA',
    'BORRA DE LA': 'BORRA_DE_LA',
    'ORDENA POR': 'ORDENA_POR',
    'COMO MUCHO': 'COMO_MUCHO',
    'WHERE DEL GROUP BY': 'WHERE_DEL_GROUP_BY',
    'EXISTE': 'EXISTE',
    'ENTRE': 'ENTRE',
    'PARECIDO A': 'PARECIDO_A',
    'ES NULO': 'ES_NULO',
    'CAMBIA LA TABLA': 'CAMBIA_LA_TABLA',
    'AGREGA LA COLUMNA': 'AGREGA_LA_COLUMNA',
    'ELIMINA LA COLUMNA': 'ELIMINA_LA_COLUMNA',
    'CREA LA TABLA': 'CREA_LA_TABLA',
    'TIRA LA TABLA': 'TIRA_LA_TABLA',
    'POR DEFECTO': 'POR_DEFECTO',
    'UNICO': 'UNICO',
    'CLAVE PRIMA': 'CLAVE_PRIMA',
    'CLAVE REFERENTE': 'CLAVE_REFERENTE',
    'NO NULO': 'NO_NULO',
    'TRANSFORMA A': 'TRANSFORMA_A',
    'Y': 'Y',
    'RENOMBRA': 'RENOMBRA'
}

tokens = [
    'ID', 'COMPARADORES', 'NUMBER', 'LPAREN', 'RPAREN', 'COMMA', 'STRING', 'ASTERISK'
] + list(reserved.values())

# Definir todos los tokens de USQL con sus expresiones regulares (sin espacios)
t_TRAEME = r'TRAEME'
t_TODO = r'TODO'
t_DONDE = r'DONDE'
t_MEZCLANDO = r'MEZCLANDO'
t_EN = r'EN'
t_Y = r'Y'
t_COMPARADORES = r'<=|>=|<|>|='
t_NUMBER = r'\d+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_STRING = r"'[^']*'"
t_ASTERISK = r'\*'

#Definicion de tokens con espacios
def t_METE_EN(t):
    r'METE\s+EN'
    return t

def t_LOS_VALORES(t):
    r'LOS\s+VALORES'
    return t

def t_BORRA_DE_LA(t):
    r'BORRA\s+DE\s+LA'
    return t

def t_ORDENA_POR(t):
    r'ORDENA\s+POR'
    return t

def t_WHERE_DEL_GROUP_BY(t):
    r'WHERE\s+DEL\s+GROUP\s+BY'
    return t

def t_CAMBIA_LA_TABLA(t):
    r'CAMBIA\s+LA\s+TABLA'
    return t

def t_AGREGA_LA_COLUMNA(t):
    r'AGREGA\s+LA\s+COLUMNA'
    return t

def t_ELIMINA_LA_COLUMNA(t):
    r'ELIMINA\s+LA\s+COLUMNA'
    return t

def t_CREA_LA_TABLA(t):
    r'CREA\s+LA\s+TABLA'
    return t

def t_TIRA_LA_TABLA(t):
    r'TIRA\s+LA\s+TABLA'
    return t

def t_CLAVE_PRIMA(t):
    r'CLAVE\s+PRIMA'
    return t

def t_CLAVE_REFERENTE(t):
    r'CLAVE\s+REFERENTE'
    return t

def t_NO_NULO(t):
    r'NO\s+NULO'
    return t

def t_TRANSFORMA_A(t):
    r'TRANSFORMA\s+A'
    return t

def t_DE_LA_TABLA(t):
    r'DE\s+LA\s+TABLA'
    return t

def t_AGRUPANDO_POR(t):
    r'AGRUPANDO\s+POR'
    return t

def t_LOS_DISTINTOS(t):
    r'LOS\s+DISTINTOS'
    return t

def t_RENOMBRA(t):
    r'RENOMBRA'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_\.\\;]'
    t.type = reserved.get(t.value, 'ID')
    return t


#Ignorar espacios
t_ignore = ' \t'

#Error en tokens
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la posición {t.lexpos}")
    t.lexer.skip(1)

#Reglas Gramaticas

# SELECT
def p_query_select(p):
    '''query : TRAEME seleccion DE_LA_TABLA tabla opcionales'''
    p[0] = f"SELECT {p[2]} FROM {p[4]} {p[5]}"

# INSERT
def p_query_insert(p):
    'query : METE_EN tabla LPAREN columnas RPAREN LOS_VALORES LPAREN valores RPAREN'
    p[0] = f'INSERT INTO {p[2]} ({p[4]}) VALUES ({p[8]})'

# UPDATE
def p_query_update(p):
    'query : ACTUALIZA tabla SETEA columna comparador valor opcionales'
    p[0] = f'UPDATE {p[2]} SET {p[4]} {p[5]} {p[6]} {p[7]}'

# DELETE
def p_query_delete(p):
    '''query : BORRA_DE_LA tabla opcionales'''
    p[0] = f'DELETE FROM {p[2]} {p[3]}'

# ALTER TABLE
def p_query_alter_table(p):
    '''query : CAMBIA_LA_TABLA tabla alter_opcionales'''
    p[0] = f'ALTER TABLE {p[2]} {p[3]}'

# Opcionales for SELECT, UPDATE, and DELETE clauses
def p_opcionales(p):
    '''opcionales : where opcionales
                  | group opcionales
                  | having opcionales
                  | join opcionales
                  | empty'''
    if len(p) > 2:
        p[0] = f"{p[1]} {p[2]}"
    else:
        p[0] = ''

# JOIN clause
def p_join(p):
    '''join : MEZCLANDO tabla EN columna comparador columna
            | empty'''
    if len(p) > 2:
        p[0] = f'JOIN {p[2]} ON {p[4]} {p[5]} {p[6]}'
    else:
        p[0] = ''

# GROUP BY clause
def p_group(p):
    '''group : AGRUPANDO_POR columna
             | empty'''
    if len(p) > 2:
        p[0] = f"GROUP BY {p[2]}"
    else:
        p[0] = ''

# HAVING clause
def p_having(p):
    '''having : WHERE_DEL_GROUP_BY condicion
              | WHERE_DEL_GROUP_BY seleccion
              | empty'''
    if len(p) > 2:
        p[0] = f"HAVING {p[2]}"
    else:
        p[0] = ''

# WHERE clause
def p_where(p):
    '''where : DONDE condicion
             | empty'''
    if len(p) > 2:
        p[0] = f"WHERE {p[2]}"
    else:
        p[0] = ''

# ADD COLUMN for ALTER TABLE
def p_add(p):
    '''add : AGREGA_LA_COLUMNA columna tipo_dato constraint'''
    p[0] = f'ADD COLUMN {p[2]} {p[3]} {p[4]}'

# Define DROP COLUMN for ALTER TABLE
def p_drop_column(p):
    '''drop_column : ELIMINA_LA_COLUMNA columna
                   | empty'''
    if len(p) > 2:
        p[0] = f'DROP COLUMN {p[2]}'
    else:
        p[0] = ''

def p_condicion(p):
    '''condicion : columna comparador valor
                 | columna ENTRE valor COMMA valor
                 | columna ENTRE valor Y valor'''
    if len(p) == 4:
        p[0] = f"{p[1]} {p[2]} {p[3]}"
    else:
        p[0] = f"{p[1]} BETWEEN {p[3]} AND {p[5]}"

def p_rename(p):
    '''rename : RENOMBRA columna valor
            | empty'''
    if len(p) > 2:
        p[0] = f'RENAME {p[2]} {p[3]}'
    else:
        p[0] = ''

def p_create(p):
    '''create : CREA_LA_TABLA tabla
            | empty'''
    if len(p) > 2:
        p[0] = f'CREATE TABLE {p[2]} {p[3]}'
    else:
        p[0] = ''

def p_drop_table(p):
    '''drop_table : TIRA_LA_TABLA tabla
            | empty'''
    if len(p) > 2:
        p[0] = f'DROP TABLE {p[2]}'
    else:
        p[0] = ''

def p_alter_opcionales(p):
    '''alter_opcionales : add alter_opcionales
                | create alter_opcionales
                | drop_table alter_opcionales
                | drop_column alter_opcionales
                | empty'''
    if len(p) > 2:
        p[0] = f"{p[1]} {p[2]}"
    else:
        p[0] = ''

def p_seleccion(p):
    '''seleccion : TODO
                 | columna
                 | LOS_DISTINTOS columna
                 | CONTANDO LPAREN ASTERISK RPAREN 
                 | CONTANDO LPAREN TODO RPAREN'''
    if p[1] == 'TODO':
        p[0] = '*'
    elif p[1] == "LOS_DISTINTOS":
        p[0] = f'DISTINCT {p[2]}'
    elif p[1] == "CONTANDO" and (p[3] == '*' or p[3] == "TODO"):
        p[0] = 'COUNT(*)'
    else:
        p[0] = p[1]


def p_tabla(p):
    'tabla : ID'
    p[0] = p[1]

def p_columna(p):
    '''columna : ID'''
    p[0] = p[1]

def p_columnas(p):
    '''columnas : columna
                | columna COMMA columnas'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"

def p_comparador(p):
    '''comparador : COMPARADORES
                    | empty'''
    p[0] = p[1]

def p_valor(p):
    '''valor : NUMBER
             | ID
             | STRING
             | LPAREN valor RPAREN'''
    p[0] = p[1]

def p_valores(p):
    '''valores : valor
               | valor COMMA valores'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]}, {p[3]}"

def p_tipo_dato(p):
    '''tipo_dato : ID LPAREN NUMBER RPAREN
                 | ID'''
    if len(p) == 5:
        p[0] = f"{p[1]}({p[3]})"
    else:
        p[0] = p[1]
        
def p_constraint(p):
    '''constraint : NO_NULO
                  | empty'''
    if len(p) > 1 and p[1] == 'NO_NULO':
        p[0] = 'NOT NULL'
    else:
        p[0] = ''

def p_empty(p):
    'empty : '
    p[0] = ''

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

lexer = lex.lex()
parser = yacc.yacc()

def run():
    while True:
            try:
                s = input('input > ')
            except EOFError:
                break
            print(parser.parse(s)) 

if __name__ == '__main__':

    # lexer.input("METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25)")
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break
    #     print(tok)

    while True:
        try:
            s = input('input > ')
        except EOFError:
            break
        print(parser.parse(s))