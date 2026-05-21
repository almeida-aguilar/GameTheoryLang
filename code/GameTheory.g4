grammar GameTheory;

// ===== Parser =====

program
    : GAME GAME_ID
      PLAYERS PLAYER_ID COMMA PLAYER_ID
      STRATEGIES strategy strategy
      PAYOFFS payoffList
      ANALYZE commandList
      EOF
    ;

strategy
    : PLAYER_ID COLON strategyList
    ;

strategyList
    : STRATEGY_ID COMMA strategyList
    | STRATEGY_ID
    ;

payoffList
    : payoff payoffList
    |
    ;

payoff
    : PLAYER_ID STRATEGY_ID COMMA PLAYER_ID STRATEGY_ID COLON LPAREN NUMBER COMMA NUMBER RPAREN
    ;

commandList
    : command commandList
    |
    ;

command
    : NASH     LPAREN RPAREN
    | DOMINANT LPAREN RPAREN
    | PARETO   LPAREN RPAREN
    | MINIMAX  LPAREN RPAREN
    | MAXIMIN  LPAREN RPAREN
    | SIMULATE LPAREN ROUNDS EQUAL NUMBER RPAREN
    ;

// ===== Lexer =====

// Keywords
GAME       : 'game'       ;
PLAYERS    : 'players'    ;
STRATEGIES : 'strategies' ;
PAYOFFS    : 'payoffs'    ;
ANALYZE    : 'analyze'    ;
NASH       : 'nash'       ;
DOMINANT   : 'dominant'   ;
PARETO     : 'pareto'     ;
MINIMAX    : 'minimax'    ;
MAXIMIN    : 'maximin'    ;
SIMULATE   : 'simulate'   ;
ROUNDS     : 'rounds'     ;

// Símbolos
COMMA  : ','  ;
COLON  : ':'  ;
EQUAL  : '='  ;
LPAREN : '('  ;
RPAREN : ')'  ;

// Tokens generales
PLAYER_ID   : [A-Z]                ;
GAME_ID     : [A-Z][a-zA-Z0-9_]+  ;
STRATEGY_ID : [a-z][a-zA-Z0-9_]*  ;
NUMBER      : [0-9]+ ('.' [0-9]+)? ;

// Ignorados
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;
