grammar GameTheory;

// ===== Parser =====

program
    : GAME GAME_ID
      PLAYERS playerList
      STRATEGIES strategyList
      PAYOFFS payoffList
      ANALYZE commandList
      EOF
    ;

playerList
    : PLAYER_ID COMMA playerList
    | PLAYER_ID
    ;


strategyList
    : strategy strategyList
    | strategy
    ;

strategy
    : PLAYER_ID COLON optionList
    ;

optionList
    : OPTION_ID COMMA optionList
    | OPTION_ID
    ;

payoffList
    : payoff payoffList
    |
    ;

payoff
    :  outcomeDecisionList COLON outcomeValueList
    ;

outcomeDecisionList
    : PLAYER_ID OPTION_ID COMMA outcomeDecisionList
    | PLAYER_ID OPTION_ID
    ;

outcomeValueList
    : NUMBER COMMA outcomeValueList
    | NUMBER
    ;

commandList
    : command commandList
    |
    ;

command
    : NASH
    | DOMINANT
    | PARETO
    | MINIMAX
    | MAXIMIN
    | SIMULATE NUMBER
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

// Símbolos
COMMA  : ','  ;
COLON  : ':'  ;

// Tokens generales
PLAYER_ID   : [A-Z]                     ;
GAME_ID     : [A-Z][a-zA-Z0-9_]+        ;
OPTION_ID : [a-z][a-zA-Z0-9_]*        ;
NUMBER     : '-'? [0-9]+ ('.' [0-9]+)? ;

// Ignorados
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '#' ~[\r\n]* -> skip ;
