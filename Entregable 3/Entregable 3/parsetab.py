
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ACTUALIZA AGREGA_LA_COLUMNA AGRUPANDO_POR ASTERISK BORRA_DE_LA CAMBIA_LA_TABLA CLAVE_PRIMA CLAVE_REFERENTE COMMA COMO_MUCHO COMPARADORES CONTANDO CREA_LA_TABLA DE_LA_TABLA DONDE ELIMINA_LA_COLUMNA EN ENTRE ES_NULO EXISTE ID LOS_DISTINTOS LOS_VALORES LPAREN METE_EN MEZCLANDO NO_NULO NUMBER ORDENA_POR PARECIDO_A POR_DEFECTO RENOMBRA RPAREN SETEA STRING TIRA_LA_TABLA TODO TRAEME TRANSFORMA_A UNICO WHERE_DEL_GROUP_BY Yquery : TRAEME seleccion DE_LA_TABLA tabla opcionalesquery : METE_EN tabla LPAREN columnas RPAREN LOS_VALORES LPAREN valores RPARENquery : ACTUALIZA tabla SETEA columna comparador valor opcionalesquery : BORRA_DE_LA tabla opcionalesquery : CAMBIA_LA_TABLA tabla alter_opcionalesopcionales : where opcionales\n                  | group opcionales\n                  | having opcionales\n                  | join opcionales\n                  | emptyjoin : MEZCLANDO tabla EN columna comparador columna\n            | emptygroup : AGRUPANDO_POR columna\n             | emptyhaving : WHERE_DEL_GROUP_BY condicion\n              | WHERE_DEL_GROUP_BY seleccion\n              | emptywhere : DONDE condicion\n             | emptyadd : AGREGA_LA_COLUMNA columna tipo_dato constraintdrop_column : ELIMINA_LA_COLUMNA columna\n                   | emptycondicion : columna comparador valor\n                 | columna ENTRE valor COMMA valor\n                 | columna ENTRE valor Y valorrename : RENOMBRA columna valor\n            | emptycreate : CREA_LA_TABLA tabla\n            | emptydrop_table : TIRA_LA_TABLA tabla\n            | emptyalter_opcionales : add alter_opcionales\n                | create alter_opcionales\n                | drop_table alter_opcionales\n                | drop_column alter_opcionales\n                | emptyseleccion : TODO\n                 | columna\n                 | LOS_DISTINTOS columna\n                 | CONTANDO LPAREN ASTERISK RPAREN \n                 | CONTANDO LPAREN TODO RPARENtabla : IDcolumna : IDcolumnas : columna\n                | columna COMMA columnascomparador : COMPARADORES\n                    | emptyvalor : NUMBER\n             | ID\n             | STRING\n             | LPAREN valor RPARENvalores : valor\n               | valor COMMA valorestipo_dato : ID LPAREN NUMBER RPAREN\n                 | IDconstraint : NO_NULO\n                  | emptyempty : '
    
_lr_action_items = {'TRAEME':([0,],[2,]),'METE_EN':([0,],[3,]),'ACTUALIZA':([0,],[4,]),'BORRA_DE_LA':([0,],[5,]),'CAMBIA_LA_TABLA':([0,],[6,]),'$end':([1,8,12,14,16,17,19,23,24,25,26,27,28,33,34,35,36,37,38,43,49,50,51,52,53,55,56,57,58,60,61,62,63,65,66,67,68,69,70,79,80,83,84,85,86,88,91,92,93,96,104,105,106,107,108,109,],[0,-37,-43,-42,-58,-58,-39,-4,-58,-58,-58,-58,-10,-5,-58,-58,-58,-58,-22,-58,-6,-7,-8,-9,-18,-13,-15,-16,-38,-32,-33,-34,-35,-28,-30,-21,-1,-40,-41,-58,-55,-58,-48,-49,-50,-23,-20,-56,-57,-3,-51,-24,-25,-11,-54,-2,]),'TODO':([2,20,31,],[8,45,8,]),'LOS_DISTINTOS':([2,31,],[10,10,]),'CONTANDO':([2,31,],[11,11,]),'ID':([2,3,4,5,6,10,12,18,21,22,29,30,31,32,39,40,41,42,48,54,58,64,72,73,74,75,76,77,78,87,90,95,98,99,100,110,],[12,14,14,14,14,12,-43,14,12,12,12,12,12,14,12,14,14,12,-58,-58,-58,80,12,85,-46,-47,85,85,12,85,-58,85,85,85,12,85,]),'DE_LA_TABLA':([7,8,9,12,19,69,70,],[18,-37,-38,-43,-39,-40,-41,]),'DONDE':([8,12,14,16,19,24,25,26,27,28,43,53,55,56,57,58,69,70,83,84,85,86,88,104,105,106,107,],[-37,-43,-42,29,-39,29,29,29,29,-12,29,-18,-13,-15,-16,-38,-40,-41,29,-48,-49,-50,-23,-51,-24,-25,-11,]),'AGRUPANDO_POR':([8,12,14,16,19,24,25,26,27,28,43,53,55,56,57,58,69,70,83,84,85,86,88,104,105,106,107,],[-37,-43,-42,30,-39,30,30,30,30,-12,30,-18,-13,-15,-16,-38,-40,-41,30,-48,-49,-50,-23,-51,-24,-25,-11,]),'WHERE_DEL_GROUP_BY':([8,12,14,16,19,24,25,26,27,28,43,53,55,56,57,58,69,70,83,84,85,86,88,104,105,106,107,],[-37,-43,-42,31,-39,31,31,31,31,-12,31,-18,-13,-15,-16,-38,-40,-41,31,-48,-49,-50,-23,-51,-24,-25,-11,]),'MEZCLANDO':([8,12,14,16,19,24,25,26,27,28,43,53,55,56,57,58,69,70,83,84,85,86,88,104,105,106,107,],[-37,-43,-42,32,-39,32,32,32,32,-12,32,-18,-13,-15,-16,-38,-40,-41,32,-48,-49,-50,-23,-51,-24,-25,-11,]),'LPAREN':([11,12,13,14,48,54,58,73,74,75,76,77,80,81,87,95,98,99,110,],[20,-43,21,-42,-58,-58,-58,87,-46,-47,87,87,94,95,87,87,87,87,87,]),'COMMA':([12,47,84,85,86,89,103,104,],[-43,72,-48,-49,-50,98,110,-51,]),'RPAREN':([12,44,45,46,47,82,84,85,86,97,101,102,103,104,111,],[-43,69,70,71,-44,-45,-48,-49,-50,104,108,109,-52,-51,-53,]),'COMPARADORES':([12,48,54,58,90,],[-43,74,74,74,74,]),'NUMBER':([12,48,54,58,73,74,75,76,77,87,94,95,98,99,110,],[-43,-58,-58,-58,84,-46,-47,84,84,84,101,84,84,84,84,]),'STRING':([12,48,54,58,73,74,75,76,77,87,95,98,99,110,],[-43,-58,-58,-58,86,-46,-47,86,86,86,86,86,86,86,]),'ENTRE':([12,54,58,],[-43,77,77,]),'AGREGA_LA_COLUMNA':([12,14,17,34,35,36,37,38,65,66,67,79,80,91,92,93,108,],[-43,-42,39,39,39,39,39,-22,-28,-30,-21,-58,-55,-20,-56,-57,-54,]),'CREA_LA_TABLA':([12,14,17,34,35,36,37,38,65,66,67,79,80,91,92,93,108,],[-43,-42,40,40,40,40,40,-22,-28,-30,-21,-58,-55,-20,-56,-57,-54,]),'TIRA_LA_TABLA':([12,14,17,34,35,36,37,38,65,66,67,79,80,91,92,93,108,],[-43,-42,41,41,41,41,41,-22,-28,-30,-21,-58,-55,-20,-56,-57,-54,]),'ELIMINA_LA_COLUMNA':([12,14,17,34,35,36,37,38,65,66,67,79,80,91,92,93,108,],[-43,-42,42,42,42,42,42,-22,-28,-30,-21,-58,-55,-20,-56,-57,-54,]),'SETEA':([14,15,],[-42,22,]),'EN':([14,59,],[-42,78,]),'ASTERISK':([20,],[44,]),'LOS_VALORES':([71,],[81,]),'NO_NULO':([79,80,108,],[92,-55,-54,]),'Y':([84,85,86,89,104,],[-48,-49,-50,99,-51,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'query':([0,],[1,]),'seleccion':([2,31,],[7,57,]),'columna':([2,10,21,22,29,30,31,39,42,72,78,100,],[9,19,47,48,54,55,58,64,67,47,90,107,]),'tabla':([3,4,5,6,18,32,40,41,],[13,15,16,17,43,59,65,66,]),'opcionales':([16,24,25,26,27,43,83,],[23,49,50,51,52,68,96,]),'where':([16,24,25,26,27,43,83,],[24,24,24,24,24,24,24,]),'group':([16,24,25,26,27,43,83,],[25,25,25,25,25,25,25,]),'having':([16,24,25,26,27,43,83,],[26,26,26,26,26,26,26,]),'join':([16,24,25,26,27,43,83,],[27,27,27,27,27,27,27,]),'empty':([16,17,24,25,26,27,34,35,36,37,43,48,54,58,79,83,90,],[28,38,28,28,28,28,38,38,38,38,28,75,75,75,93,28,75,]),'alter_opcionales':([17,34,35,36,37,],[33,60,61,62,63,]),'add':([17,34,35,36,37,],[34,34,34,34,34,]),'create':([17,34,35,36,37,],[35,35,35,35,35,]),'drop_table':([17,34,35,36,37,],[36,36,36,36,36,]),'drop_column':([17,34,35,36,37,],[37,37,37,37,37,]),'columnas':([21,72,],[46,82,]),'condicion':([29,31,],[53,56,]),'comparador':([48,54,58,90,],[73,76,76,100,]),'tipo_dato':([64,],[79,]),'valor':([73,76,77,87,95,98,99,110,],[83,88,89,97,103,105,106,103,]),'constraint':([79,],[91,]),'valores':([95,110,],[102,111,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> query","S'",1,None,None,None),
  ('query -> TRAEME seleccion DE_LA_TABLA tabla opcionales','query',5,'p_query_select','ESP_ENG.py',153),
  ('query -> METE_EN tabla LPAREN columnas RPAREN LOS_VALORES LPAREN valores RPAREN','query',9,'p_query_insert','ESP_ENG.py',158),
  ('query -> ACTUALIZA tabla SETEA columna comparador valor opcionales','query',7,'p_query_update','ESP_ENG.py',163),
  ('query -> BORRA_DE_LA tabla opcionales','query',3,'p_query_delete','ESP_ENG.py',168),
  ('query -> CAMBIA_LA_TABLA tabla alter_opcionales','query',3,'p_query_alter_table','ESP_ENG.py',173),
  ('opcionales -> where opcionales','opcionales',2,'p_opcionales','ESP_ENG.py',178),
  ('opcionales -> group opcionales','opcionales',2,'p_opcionales','ESP_ENG.py',179),
  ('opcionales -> having opcionales','opcionales',2,'p_opcionales','ESP_ENG.py',180),
  ('opcionales -> join opcionales','opcionales',2,'p_opcionales','ESP_ENG.py',181),
  ('opcionales -> empty','opcionales',1,'p_opcionales','ESP_ENG.py',182),
  ('join -> MEZCLANDO tabla EN columna comparador columna','join',6,'p_join','ESP_ENG.py',190),
  ('join -> empty','join',1,'p_join','ESP_ENG.py',191),
  ('group -> AGRUPANDO_POR columna','group',2,'p_group','ESP_ENG.py',199),
  ('group -> empty','group',1,'p_group','ESP_ENG.py',200),
  ('having -> WHERE_DEL_GROUP_BY condicion','having',2,'p_having','ESP_ENG.py',208),
  ('having -> WHERE_DEL_GROUP_BY seleccion','having',2,'p_having','ESP_ENG.py',209),
  ('having -> empty','having',1,'p_having','ESP_ENG.py',210),
  ('where -> DONDE condicion','where',2,'p_where','ESP_ENG.py',218),
  ('where -> empty','where',1,'p_where','ESP_ENG.py',219),
  ('add -> AGREGA_LA_COLUMNA columna tipo_dato constraint','add',4,'p_add','ESP_ENG.py',227),
  ('drop_column -> ELIMINA_LA_COLUMNA columna','drop_column',2,'p_drop_column','ESP_ENG.py',232),
  ('drop_column -> empty','drop_column',1,'p_drop_column','ESP_ENG.py',233),
  ('condicion -> columna comparador valor','condicion',3,'p_condicion','ESP_ENG.py',240),
  ('condicion -> columna ENTRE valor COMMA valor','condicion',5,'p_condicion','ESP_ENG.py',241),
  ('condicion -> columna ENTRE valor Y valor','condicion',5,'p_condicion','ESP_ENG.py',242),
  ('rename -> RENOMBRA columna valor','rename',3,'p_rename','ESP_ENG.py',249),
  ('rename -> empty','rename',1,'p_rename','ESP_ENG.py',250),
  ('create -> CREA_LA_TABLA tabla','create',2,'p_create','ESP_ENG.py',257),
  ('create -> empty','create',1,'p_create','ESP_ENG.py',258),
  ('drop_table -> TIRA_LA_TABLA tabla','drop_table',2,'p_drop_table','ESP_ENG.py',265),
  ('drop_table -> empty','drop_table',1,'p_drop_table','ESP_ENG.py',266),
  ('alter_opcionales -> add alter_opcionales','alter_opcionales',2,'p_alter_opcionales','ESP_ENG.py',273),
  ('alter_opcionales -> create alter_opcionales','alter_opcionales',2,'p_alter_opcionales','ESP_ENG.py',274),
  ('alter_opcionales -> drop_table alter_opcionales','alter_opcionales',2,'p_alter_opcionales','ESP_ENG.py',275),
  ('alter_opcionales -> drop_column alter_opcionales','alter_opcionales',2,'p_alter_opcionales','ESP_ENG.py',276),
  ('alter_opcionales -> empty','alter_opcionales',1,'p_alter_opcionales','ESP_ENG.py',277),
  ('seleccion -> TODO','seleccion',1,'p_seleccion','ESP_ENG.py',284),
  ('seleccion -> columna','seleccion',1,'p_seleccion','ESP_ENG.py',285),
  ('seleccion -> LOS_DISTINTOS columna','seleccion',2,'p_seleccion','ESP_ENG.py',286),
  ('seleccion -> CONTANDO LPAREN ASTERISK RPAREN','seleccion',4,'p_seleccion','ESP_ENG.py',287),
  ('seleccion -> CONTANDO LPAREN TODO RPAREN','seleccion',4,'p_seleccion','ESP_ENG.py',288),
  ('tabla -> ID','tabla',1,'p_tabla','ESP_ENG.py',300),
  ('columna -> ID','columna',1,'p_columna','ESP_ENG.py',304),
  ('columnas -> columna','columnas',1,'p_columnas','ESP_ENG.py',308),
  ('columnas -> columna COMMA columnas','columnas',3,'p_columnas','ESP_ENG.py',309),
  ('comparador -> COMPARADORES','comparador',1,'p_comparador','ESP_ENG.py',316),
  ('comparador -> empty','comparador',1,'p_comparador','ESP_ENG.py',317),
  ('valor -> NUMBER','valor',1,'p_valor','ESP_ENG.py',321),
  ('valor -> ID','valor',1,'p_valor','ESP_ENG.py',322),
  ('valor -> STRING','valor',1,'p_valor','ESP_ENG.py',323),
  ('valor -> LPAREN valor RPAREN','valor',3,'p_valor','ESP_ENG.py',324),
  ('valores -> valor','valores',1,'p_valores','ESP_ENG.py',328),
  ('valores -> valor COMMA valores','valores',3,'p_valores','ESP_ENG.py',329),
  ('tipo_dato -> ID LPAREN NUMBER RPAREN','tipo_dato',4,'p_tipo_dato','ESP_ENG.py',336),
  ('tipo_dato -> ID','tipo_dato',1,'p_tipo_dato','ESP_ENG.py',337),
  ('constraint -> NO_NULO','constraint',1,'p_constraint','ESP_ENG.py',344),
  ('constraint -> empty','constraint',1,'p_constraint','ESP_ENG.py',345),
  ('empty -> <empty>','empty',0,'p_empty','ESP_ENG.py',352),
]
