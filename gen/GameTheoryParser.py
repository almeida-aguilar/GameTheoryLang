# Generated from GameTheory.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,87,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,3,2,38,8,2,1,3,1,3,1,3,1,3,3,3,44,
        8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,3,5,62,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,85,8,6,1,6,0,0,7,0,2,4,6,8,
        10,12,0,0,87,0,14,1,0,0,0,2,29,1,0,0,0,4,37,1,0,0,0,6,43,1,0,0,0,
        8,45,1,0,0,0,10,61,1,0,0,0,12,84,1,0,0,0,14,15,5,1,0,0,15,16,5,19,
        0,0,16,17,5,2,0,0,17,18,5,18,0,0,18,19,5,13,0,0,19,20,5,18,0,0,20,
        21,5,3,0,0,21,22,3,2,1,0,22,23,3,2,1,0,23,24,5,4,0,0,24,25,3,6,3,
        0,25,26,5,5,0,0,26,27,3,10,5,0,27,28,5,0,0,1,28,1,1,0,0,0,29,30,
        5,18,0,0,30,31,5,14,0,0,31,32,3,4,2,0,32,3,1,0,0,0,33,34,5,20,0,
        0,34,35,5,13,0,0,35,38,3,4,2,0,36,38,5,20,0,0,37,33,1,0,0,0,37,36,
        1,0,0,0,38,5,1,0,0,0,39,40,3,8,4,0,40,41,3,6,3,0,41,44,1,0,0,0,42,
        44,1,0,0,0,43,39,1,0,0,0,43,42,1,0,0,0,44,7,1,0,0,0,45,46,5,18,0,
        0,46,47,5,20,0,0,47,48,5,13,0,0,48,49,5,18,0,0,49,50,5,20,0,0,50,
        51,5,14,0,0,51,52,5,16,0,0,52,53,5,21,0,0,53,54,5,13,0,0,54,55,5,
        21,0,0,55,56,5,17,0,0,56,9,1,0,0,0,57,58,3,12,6,0,58,59,3,10,5,0,
        59,62,1,0,0,0,60,62,1,0,0,0,61,57,1,0,0,0,61,60,1,0,0,0,62,11,1,
        0,0,0,63,64,5,6,0,0,64,65,5,16,0,0,65,85,5,17,0,0,66,67,5,7,0,0,
        67,68,5,16,0,0,68,85,5,17,0,0,69,70,5,8,0,0,70,71,5,16,0,0,71,85,
        5,17,0,0,72,73,5,9,0,0,73,74,5,16,0,0,74,85,5,17,0,0,75,76,5,10,
        0,0,76,77,5,16,0,0,77,85,5,17,0,0,78,79,5,11,0,0,79,80,5,16,0,0,
        80,81,5,12,0,0,81,82,5,15,0,0,82,83,5,21,0,0,83,85,5,17,0,0,84,63,
        1,0,0,0,84,66,1,0,0,0,84,69,1,0,0,0,84,72,1,0,0,0,84,75,1,0,0,0,
        84,78,1,0,0,0,85,13,1,0,0,0,4,37,43,61,84
    ]

class GameTheoryParser ( Parser ):

    grammarFileName = "GameTheory.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'game'", "'players'", "'strategies'", 
                     "'payoffs'", "'analyze'", "'nash'", "'dominant'", "'pareto'", 
                     "'minimax'", "'maximin'", "'simulate'", "'rounds'", 
                     "','", "':'", "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "GAME", "PLAYERS", "STRATEGIES", "PAYOFFS", 
                      "ANALYZE", "NASH", "DOMINANT", "PARETO", "MINIMAX", 
                      "MAXIMIN", "SIMULATE", "ROUNDS", "COMMA", "COLON", 
                      "EQUAL", "LPAREN", "RPAREN", "PLAYER_ID", "GAME_ID", 
                      "STRATEGY_ID", "NUMBER", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_strategy = 1
    RULE_strategyList = 2
    RULE_payoffList = 3
    RULE_payoff = 4
    RULE_commandList = 5
    RULE_command = 6

    ruleNames =  [ "program", "strategy", "strategyList", "payoffList", 
                   "payoff", "commandList", "command" ]

    EOF = Token.EOF
    GAME=1
    PLAYERS=2
    STRATEGIES=3
    PAYOFFS=4
    ANALYZE=5
    NASH=6
    DOMINANT=7
    PARETO=8
    MINIMAX=9
    MAXIMIN=10
    SIMULATE=11
    ROUNDS=12
    COMMA=13
    COLON=14
    EQUAL=15
    LPAREN=16
    RPAREN=17
    PLAYER_ID=18
    GAME_ID=19
    STRATEGY_ID=20
    NUMBER=21
    WS=22
    COMMENT=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GAME(self):
            return self.getToken(GameTheoryParser.GAME, 0)

        def GAME_ID(self):
            return self.getToken(GameTheoryParser.GAME_ID, 0)

        def PLAYERS(self):
            return self.getToken(GameTheoryParser.PLAYERS, 0)

        def PLAYER_ID(self, i:int=None):
            if i is None:
                return self.getTokens(GameTheoryParser.PLAYER_ID)
            else:
                return self.getToken(GameTheoryParser.PLAYER_ID, i)

        def COMMA(self):
            return self.getToken(GameTheoryParser.COMMA, 0)

        def STRATEGIES(self):
            return self.getToken(GameTheoryParser.STRATEGIES, 0)

        def strategy(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GameTheoryParser.StrategyContext)
            else:
                return self.getTypedRuleContext(GameTheoryParser.StrategyContext,i)


        def PAYOFFS(self):
            return self.getToken(GameTheoryParser.PAYOFFS, 0)

        def payoffList(self):
            return self.getTypedRuleContext(GameTheoryParser.PayoffListContext,0)


        def ANALYZE(self):
            return self.getToken(GameTheoryParser.ANALYZE, 0)

        def commandList(self):
            return self.getTypedRuleContext(GameTheoryParser.CommandListContext,0)


        def EOF(self):
            return self.getToken(GameTheoryParser.EOF, 0)

        def getRuleIndex(self):
            return GameTheoryParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = GameTheoryParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(GameTheoryParser.GAME)
            self.state = 15
            self.match(GameTheoryParser.GAME_ID)
            self.state = 16
            self.match(GameTheoryParser.PLAYERS)
            self.state = 17
            self.match(GameTheoryParser.PLAYER_ID)
            self.state = 18
            self.match(GameTheoryParser.COMMA)
            self.state = 19
            self.match(GameTheoryParser.PLAYER_ID)
            self.state = 20
            self.match(GameTheoryParser.STRATEGIES)
            self.state = 21
            self.strategy()
            self.state = 22
            self.strategy()
            self.state = 23
            self.match(GameTheoryParser.PAYOFFS)
            self.state = 24
            self.payoffList()
            self.state = 25
            self.match(GameTheoryParser.ANALYZE)
            self.state = 26
            self.commandList()
            self.state = 27
            self.match(GameTheoryParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrategyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAYER_ID(self):
            return self.getToken(GameTheoryParser.PLAYER_ID, 0)

        def COLON(self):
            return self.getToken(GameTheoryParser.COLON, 0)

        def strategyList(self):
            return self.getTypedRuleContext(GameTheoryParser.StrategyListContext,0)


        def getRuleIndex(self):
            return GameTheoryParser.RULE_strategy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrategy" ):
                listener.enterStrategy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrategy" ):
                listener.exitStrategy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrategy" ):
                return visitor.visitStrategy(self)
            else:
                return visitor.visitChildren(self)




    def strategy(self):

        localctx = GameTheoryParser.StrategyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_strategy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(GameTheoryParser.PLAYER_ID)
            self.state = 30
            self.match(GameTheoryParser.COLON)
            self.state = 31
            self.strategyList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StrategyListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRATEGY_ID(self):
            return self.getToken(GameTheoryParser.STRATEGY_ID, 0)

        def COMMA(self):
            return self.getToken(GameTheoryParser.COMMA, 0)

        def strategyList(self):
            return self.getTypedRuleContext(GameTheoryParser.StrategyListContext,0)


        def getRuleIndex(self):
            return GameTheoryParser.RULE_strategyList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrategyList" ):
                listener.enterStrategyList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrategyList" ):
                listener.exitStrategyList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStrategyList" ):
                return visitor.visitStrategyList(self)
            else:
                return visitor.visitChildren(self)




    def strategyList(self):

        localctx = GameTheoryParser.StrategyListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_strategyList)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(GameTheoryParser.STRATEGY_ID)
                self.state = 34
                self.match(GameTheoryParser.COMMA)
                self.state = 35
                self.strategyList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(GameTheoryParser.STRATEGY_ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PayoffListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def payoff(self):
            return self.getTypedRuleContext(GameTheoryParser.PayoffContext,0)


        def payoffList(self):
            return self.getTypedRuleContext(GameTheoryParser.PayoffListContext,0)


        def getRuleIndex(self):
            return GameTheoryParser.RULE_payoffList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPayoffList" ):
                listener.enterPayoffList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPayoffList" ):
                listener.exitPayoffList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayoffList" ):
                return visitor.visitPayoffList(self)
            else:
                return visitor.visitChildren(self)




    def payoffList(self):

        localctx = GameTheoryParser.PayoffListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_payoffList)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.payoff()
                self.state = 40
                self.payoffList()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PayoffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAYER_ID(self, i:int=None):
            if i is None:
                return self.getTokens(GameTheoryParser.PLAYER_ID)
            else:
                return self.getToken(GameTheoryParser.PLAYER_ID, i)

        def STRATEGY_ID(self, i:int=None):
            if i is None:
                return self.getTokens(GameTheoryParser.STRATEGY_ID)
            else:
                return self.getToken(GameTheoryParser.STRATEGY_ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GameTheoryParser.COMMA)
            else:
                return self.getToken(GameTheoryParser.COMMA, i)

        def COLON(self):
            return self.getToken(GameTheoryParser.COLON, 0)

        def LPAREN(self):
            return self.getToken(GameTheoryParser.LPAREN, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(GameTheoryParser.NUMBER)
            else:
                return self.getToken(GameTheoryParser.NUMBER, i)

        def RPAREN(self):
            return self.getToken(GameTheoryParser.RPAREN, 0)

        def getRuleIndex(self):
            return GameTheoryParser.RULE_payoff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPayoff" ):
                listener.enterPayoff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPayoff" ):
                listener.exitPayoff(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPayoff" ):
                return visitor.visitPayoff(self)
            else:
                return visitor.visitChildren(self)




    def payoff(self):

        localctx = GameTheoryParser.PayoffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_payoff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(GameTheoryParser.PLAYER_ID)
            self.state = 46
            self.match(GameTheoryParser.STRATEGY_ID)
            self.state = 47
            self.match(GameTheoryParser.COMMA)
            self.state = 48
            self.match(GameTheoryParser.PLAYER_ID)
            self.state = 49
            self.match(GameTheoryParser.STRATEGY_ID)
            self.state = 50
            self.match(GameTheoryParser.COLON)
            self.state = 51
            self.match(GameTheoryParser.LPAREN)
            self.state = 52
            self.match(GameTheoryParser.NUMBER)
            self.state = 53
            self.match(GameTheoryParser.COMMA)
            self.state = 54
            self.match(GameTheoryParser.NUMBER)
            self.state = 55
            self.match(GameTheoryParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self):
            return self.getTypedRuleContext(GameTheoryParser.CommandContext,0)


        def commandList(self):
            return self.getTypedRuleContext(GameTheoryParser.CommandListContext,0)


        def getRuleIndex(self):
            return GameTheoryParser.RULE_commandList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommandList" ):
                listener.enterCommandList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommandList" ):
                listener.exitCommandList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommandList" ):
                return visitor.visitCommandList(self)
            else:
                return visitor.visitChildren(self)




    def commandList(self):

        localctx = GameTheoryParser.CommandListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_commandList)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8, 9, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.command()
                self.state = 58
                self.commandList()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NASH(self):
            return self.getToken(GameTheoryParser.NASH, 0)

        def LPAREN(self):
            return self.getToken(GameTheoryParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(GameTheoryParser.RPAREN, 0)

        def DOMINANT(self):
            return self.getToken(GameTheoryParser.DOMINANT, 0)

        def PARETO(self):
            return self.getToken(GameTheoryParser.PARETO, 0)

        def MINIMAX(self):
            return self.getToken(GameTheoryParser.MINIMAX, 0)

        def MAXIMIN(self):
            return self.getToken(GameTheoryParser.MAXIMIN, 0)

        def SIMULATE(self):
            return self.getToken(GameTheoryParser.SIMULATE, 0)

        def ROUNDS(self):
            return self.getToken(GameTheoryParser.ROUNDS, 0)

        def EQUAL(self):
            return self.getToken(GameTheoryParser.EQUAL, 0)

        def NUMBER(self):
            return self.getToken(GameTheoryParser.NUMBER, 0)

        def getRuleIndex(self):
            return GameTheoryParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommand" ):
                return visitor.visitCommand(self)
            else:
                return visitor.visitChildren(self)




    def command(self):

        localctx = GameTheoryParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_command)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(GameTheoryParser.NASH)
                self.state = 64
                self.match(GameTheoryParser.LPAREN)
                self.state = 65
                self.match(GameTheoryParser.RPAREN)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(GameTheoryParser.DOMINANT)
                self.state = 67
                self.match(GameTheoryParser.LPAREN)
                self.state = 68
                self.match(GameTheoryParser.RPAREN)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 69
                self.match(GameTheoryParser.PARETO)
                self.state = 70
                self.match(GameTheoryParser.LPAREN)
                self.state = 71
                self.match(GameTheoryParser.RPAREN)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(GameTheoryParser.MINIMAX)
                self.state = 73
                self.match(GameTheoryParser.LPAREN)
                self.state = 74
                self.match(GameTheoryParser.RPAREN)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.match(GameTheoryParser.MAXIMIN)
                self.state = 76
                self.match(GameTheoryParser.LPAREN)
                self.state = 77
                self.match(GameTheoryParser.RPAREN)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 78
                self.match(GameTheoryParser.SIMULATE)
                self.state = 79
                self.match(GameTheoryParser.LPAREN)
                self.state = 80
                self.match(GameTheoryParser.ROUNDS)
                self.state = 81
                self.match(GameTheoryParser.EQUAL)
                self.state = 82
                self.match(GameTheoryParser.NUMBER)
                self.state = 83
                self.match(GameTheoryParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





