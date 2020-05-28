
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightLEAKleftORleftANDrightNOTnonassocEQUALSNEQLTGTLTEGTEleftPLUSMINUSleftTIMESDIVIDErightUMINUSAND ASSIGN BOOL COLON COMMA DIVIDE ELSE EQUALS FALSE GT GTE HASHTAG ID IF INPUT LBRACE LEAK LPAREN LSQBRACKET LT LTE MAIN MINUS NEQ NOT NUM NUMBER OR OUTPUT PLUS RBRACE RPAREN RSQBRACKET SEMICOLON TIMES TRUEprog : funcs\n            | HASHTAG ID NUMBER funcsfuncs : func funcs\n             | emptyfunc : ID arglist LBRACE funcbody RBRACE\n            | MAIN LPAREN RPAREN LBRACE stms RBRACEfuncbody : stms expression\n                | expressionarglist : LPAREN RPAREN\n               | LPAREN arg args RPARENargs : COMMA arg args\n            | emptyarg : IDstms : stms stm\n            | stmstm : ID ASSIGN expression SEMICOLON\n           | ID INPUT NUMBER COLON type SEMICOLON\n           | ID OUTPUT ID SEMICOLONtype : BOOL\n            | NUMexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression EQUALS expression\n                  | expression NEQ expression\n                  | expression LT expression\n                  | expression GT expression\n                  | expression LTE expression\n                  | expression GTE expression\n                  | expression OR expression\n                  | expression AND expression\n                  | TRUE\n                  | FALSE\n                  | NUMBER\n                  | MINUS expression %prec UMINUS\n                  | NOT expressionexpression : LEAK expressionexpression : IDexpression : LPAREN expression RPARENexpression : IF LPAREN expression RPAREN LBRACE expression RBRACE ELSE LBRACE expression RBRACEexpression : ID LPAREN exps RPAREN\n                  | ID LPAREN RPARENexps : expression\n            | expression COMMA expsempty :'
    
_lr_action_items = {'HASHTAG':([0,],[3,]),'ID':([0,3,5,10,13,14,22,24,25,29,30,31,34,36,37,38,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,61,64,87,89,90,92,98,99,103,],[4,8,4,17,4,20,20,-15,57,57,57,57,17,65,57,57,71,-5,-14,57,57,57,57,57,57,57,57,57,57,57,57,57,65,-6,57,-16,-18,57,-17,57,]),'MAIN':([0,5,13,41,87,],[7,7,7,-5,-6,]),'$end':([0,1,2,5,6,11,13,19,41,87,],[-46,0,-1,-46,-4,-3,-46,-2,-5,-6,]),'LPAREN':([4,7,14,20,22,24,25,29,30,31,32,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,57,61,89,90,92,98,99,103,],[10,12,31,37,31,-15,31,31,31,31,61,31,31,-14,31,31,31,31,31,31,31,31,31,31,31,31,37,31,31,-16,-18,31,-17,31,]),'NUMBER':([8,14,22,24,25,29,30,31,37,38,39,43,44,45,46,47,48,49,50,51,52,53,54,55,61,89,90,92,98,99,103,],[13,28,28,-15,28,28,28,28,28,28,70,-14,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-16,-18,28,-17,28,]),'LBRACE':([9,15,18,62,93,102,],[14,-9,36,-10,98,103,]),'RPAREN':([10,12,16,17,26,27,28,33,35,37,56,57,58,59,60,63,66,67,68,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,94,105,],[15,18,-46,-13,-33,-34,-35,62,-12,67,-36,-39,-37,-38,84,-46,88,-43,-44,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-40,93,-11,-42,-45,-41,]),'TRUE':([14,22,24,25,29,30,31,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,61,89,90,92,98,99,103,],[26,26,-15,26,26,26,26,26,26,-14,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-16,-18,26,-17,26,]),'FALSE':([14,22,24,25,29,30,31,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,61,89,90,92,98,99,103,],[27,27,-15,27,27,27,27,27,27,-14,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-16,-18,27,-17,27,]),'MINUS':([14,20,22,23,24,25,26,27,28,29,30,31,37,38,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,89,90,92,98,99,100,103,104,105,],[25,-39,25,45,-15,25,-33,-34,-35,25,25,25,25,25,45,-14,25,25,25,25,25,25,25,25,25,25,25,25,-36,-39,45,45,45,25,-43,45,45,-21,-22,-23,-24,45,45,45,45,45,45,45,45,-40,45,-42,25,-16,-18,25,-17,45,25,45,-41,]),'NOT':([14,22,24,25,29,30,31,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,61,89,90,92,98,99,103,],[29,29,-15,29,29,29,29,29,29,-14,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-16,-18,29,-17,29,]),'LEAK':([14,22,24,25,29,30,31,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,61,89,90,92,98,99,103,],[30,30,-15,30,30,30,30,30,30,-14,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-16,-18,30,-17,30,]),'IF':([14,22,24,25,29,30,31,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,61,89,90,92,98,99,103,],[32,32,-15,32,32,32,32,32,32,-14,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-16,-18,32,-17,32,]),'COMMA':([16,17,26,27,28,56,57,58,59,63,67,68,72,73,74,75,76,77,78,79,80,81,82,83,84,88,105,],[34,-13,-33,-34,-35,-36,-39,-37,-38,34,-43,89,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-40,-42,-41,]),'PLUS':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,44,-33,-34,-35,44,-36,-39,44,44,44,-43,44,44,-21,-22,-23,-24,44,44,44,44,44,44,44,44,-40,44,-42,44,44,-41,]),'TIMES':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,46,-33,-34,-35,46,-36,-39,46,46,46,-43,46,46,46,46,-23,-24,46,46,46,46,46,46,46,46,-40,46,-42,46,46,-41,]),'DIVIDE':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,47,-33,-34,-35,47,-36,-39,47,47,47,-43,47,47,47,47,-23,-24,47,47,47,47,47,47,47,47,-40,47,-42,47,47,-41,]),'EQUALS':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,48,-33,-34,-35,48,-36,-39,48,48,48,-43,48,48,-21,-22,-23,-24,None,None,None,None,None,None,48,48,-40,48,-42,48,48,-41,]),'NEQ':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,49,-33,-34,-35,49,-36,-39,49,49,49,-43,49,49,-21,-22,-23,-24,None,None,None,None,None,None,49,49,-40,49,-42,49,49,-41,]),'LT':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,50,-33,-34,-35,50,-36,-39,50,50,50,-43,50,50,-21,-22,-23,-24,None,None,None,None,None,None,50,50,-40,50,-42,50,50,-41,]),'GT':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,51,-33,-34,-35,51,-36,-39,51,51,51,-43,51,51,-21,-22,-23,-24,None,None,None,None,None,None,51,51,-40,51,-42,51,51,-41,]),'LTE':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,52,-33,-34,-35,52,-36,-39,52,52,52,-43,52,52,-21,-22,-23,-24,None,None,None,None,None,None,52,52,-40,52,-42,52,52,-41,]),'GTE':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,53,-33,-34,-35,53,-36,-39,53,53,53,-43,53,53,-21,-22,-23,-24,None,None,None,None,None,None,53,53,-40,53,-42,53,53,-41,]),'OR':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,54,-33,-34,-35,54,-36,-39,-37,54,54,-43,54,54,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-40,54,-42,54,54,-41,]),'AND':([20,23,26,27,28,42,56,57,58,59,60,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,100,104,105,],[-39,55,-33,-34,-35,55,-36,-39,-37,55,55,-43,55,55,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,55,-32,-40,55,-42,55,55,-41,]),'RBRACE':([20,21,23,24,26,27,28,42,43,56,57,58,59,64,67,72,73,74,75,76,77,78,79,80,81,82,83,84,88,90,92,99,100,104,105,],[-39,41,-8,-15,-33,-34,-35,-7,-14,-36,-39,-37,-38,87,-43,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-40,-42,-16,-18,-17,101,105,-41,]),'ASSIGN':([20,65,],[38,38,]),'INPUT':([20,65,],[39,39,]),'OUTPUT':([20,65,],[40,40,]),'SEMICOLON':([26,27,28,56,57,58,59,67,69,71,72,73,74,75,76,77,78,79,80,81,82,83,84,88,95,96,97,105,],[-33,-34,-35,-36,-39,-37,-38,-43,90,92,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-40,-42,99,-19,-20,-41,]),'COLON':([70,],[91,]),'BOOL':([91,],[96,]),'NUM':([91,],[97,]),'ELSE':([101,],[102,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'funcs':([0,5,13,],[2,11,19,]),'func':([0,5,13,],[5,5,5,]),'empty':([0,5,13,16,63,],[6,6,6,35,35,]),'arglist':([4,],[9,]),'arg':([10,34,],[16,63,]),'funcbody':([14,],[21,]),'stms':([14,36,],[22,64,]),'expression':([14,22,25,29,30,31,37,38,44,45,46,47,48,49,50,51,52,53,54,55,61,89,98,103,],[23,42,56,58,59,60,68,69,72,73,74,75,76,77,78,79,80,81,82,83,85,68,100,104,]),'stm':([14,22,36,64,],[24,43,24,43,]),'args':([16,63,],[33,86,]),'exps':([37,89,],[66,94,]),'type':([91,],[95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> funcs','prog',1,'p_prog','Parser.py',11),
  ('prog -> HASHTAG ID NUMBER funcs','prog',4,'p_prog','Parser.py',12),
  ('funcs -> func funcs','funcs',2,'p_funcs','Parser.py',24),
  ('funcs -> empty','funcs',1,'p_funcs','Parser.py',25),
  ('func -> ID arglist LBRACE funcbody RBRACE','func',5,'p_func','Parser.py',33),
  ('func -> MAIN LPAREN RPAREN LBRACE stms RBRACE','func',6,'p_func','Parser.py',34),
  ('funcbody -> stms expression','funcbody',2,'p_funcbody','Parser.py',49),
  ('funcbody -> expression','funcbody',1,'p_funcbody','Parser.py',50),
  ('arglist -> LPAREN RPAREN','arglist',2,'p_arglist','Parser.py',58),
  ('arglist -> LPAREN arg args RPAREN','arglist',4,'p_arglist','Parser.py',59),
  ('args -> COMMA arg args','args',3,'p_args','Parser.py',67),
  ('args -> empty','args',1,'p_args','Parser.py',68),
  ('arg -> ID','arg',1,'p_arg','Parser.py',76),
  ('stms -> stms stm','stms',2,'p_stms','Parser.py',81),
  ('stms -> stm','stms',1,'p_stms','Parser.py',82),
  ('stm -> ID ASSIGN expression SEMICOLON','stm',4,'p_stm','Parser.py',90),
  ('stm -> ID INPUT NUMBER COLON type SEMICOLON','stm',6,'p_stm','Parser.py',91),
  ('stm -> ID OUTPUT ID SEMICOLON','stm',4,'p_stm','Parser.py',92),
  ('type -> BOOL','type',1,'p_type','Parser.py',109),
  ('type -> NUM','type',1,'p_type','Parser.py',110),
  ('expression -> expression PLUS expression','expression',3,'p_expression_arithmetic','Parser.py',127),
  ('expression -> expression MINUS expression','expression',3,'p_expression_arithmetic','Parser.py',128),
  ('expression -> expression TIMES expression','expression',3,'p_expression_arithmetic','Parser.py',129),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_arithmetic','Parser.py',130),
  ('expression -> expression EQUALS expression','expression',3,'p_expression_arithmetic','Parser.py',131),
  ('expression -> expression NEQ expression','expression',3,'p_expression_arithmetic','Parser.py',132),
  ('expression -> expression LT expression','expression',3,'p_expression_arithmetic','Parser.py',133),
  ('expression -> expression GT expression','expression',3,'p_expression_arithmetic','Parser.py',134),
  ('expression -> expression LTE expression','expression',3,'p_expression_arithmetic','Parser.py',135),
  ('expression -> expression GTE expression','expression',3,'p_expression_arithmetic','Parser.py',136),
  ('expression -> expression OR expression','expression',3,'p_expression_arithmetic','Parser.py',137),
  ('expression -> expression AND expression','expression',3,'p_expression_arithmetic','Parser.py',138),
  ('expression -> TRUE','expression',1,'p_expression_arithmetic','Parser.py',139),
  ('expression -> FALSE','expression',1,'p_expression_arithmetic','Parser.py',140),
  ('expression -> NUMBER','expression',1,'p_expression_arithmetic','Parser.py',141),
  ('expression -> MINUS expression','expression',2,'p_expression_arithmetic','Parser.py',142),
  ('expression -> NOT expression','expression',2,'p_expression_arithmetic','Parser.py',143),
  ('expression -> LEAK expression','expression',2,'p_expression_leak','Parser.py',164),
  ('expression -> ID','expression',1,'p_expression_id','Parser.py',170),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','Parser.py',175),
  ('expression -> IF LPAREN expression RPAREN LBRACE expression RBRACE ELSE LBRACE expression RBRACE','expression',11,'p_expression_if','Parser.py',180),
  ('expression -> ID LPAREN exps RPAREN','expression',4,'p_expression_func_call','Parser.py',189),
  ('expression -> ID LPAREN RPAREN','expression',3,'p_expression_func_call','Parser.py',190),
  ('exps -> expression','exps',1,'p_exps','Parser.py',202),
  ('exps -> expression COMMA exps','exps',3,'p_exps','Parser.py',203),
  ('empty -> <empty>','empty',0,'p_empty','Parser.py',212),
]