from ply import *
import ply.lex as lex
import ply.yacc as yacc
import numpy as np


def run():

    lexer = lex.lex()
    parser = yacc.yacc()
    while True:
        try:
            s = input('input > ')
        except EOFError:
            break
        print(parser.parse(s)) 