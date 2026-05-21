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
        4,1,19,96,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,39,8,1,1,2,1,2,1,2,1,2,3,
        2,45,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,55,8,4,1,5,1,5,1,5,
        1,5,3,5,61,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,73,8,
        7,1,8,1,8,1,8,1,8,3,8,79,8,8,1,9,1,9,1,9,1,9,3,9,85,8,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,3,10,94,8,10,1,10,0,0,11,0,2,4,6,8,10,12,
        14,16,18,20,0,0,96,0,22,1,0,0,0,2,38,1,0,0,0,4,44,1,0,0,0,6,46,1,
        0,0,0,8,54,1,0,0,0,10,60,1,0,0,0,12,62,1,0,0,0,14,72,1,0,0,0,16,
        78,1,0,0,0,18,84,1,0,0,0,20,93,1,0,0,0,22,23,5,1,0,0,23,24,5,15,
        0,0,24,25,5,2,0,0,25,26,3,2,1,0,26,27,5,3,0,0,27,28,3,4,2,0,28,29,
        5,4,0,0,29,30,3,10,5,0,30,31,5,5,0,0,31,32,3,18,9,0,32,33,5,0,0,
        1,33,1,1,0,0,0,34,35,5,14,0,0,35,36,5,12,0,0,36,39,3,2,1,0,37,39,
        5,14,0,0,38,34,1,0,0,0,38,37,1,0,0,0,39,3,1,0,0,0,40,41,3,6,3,0,
        41,42,3,4,2,0,42,45,1,0,0,0,43,45,3,6,3,0,44,40,1,0,0,0,44,43,1,
        0,0,0,45,5,1,0,0,0,46,47,5,14,0,0,47,48,5,13,0,0,48,49,3,8,4,0,49,
        7,1,0,0,0,50,51,5,16,0,0,51,52,5,12,0,0,52,55,3,8,4,0,53,55,5,16,
        0,0,54,50,1,0,0,0,54,53,1,0,0,0,55,9,1,0,0,0,56,57,3,12,6,0,57,58,
        3,10,5,0,58,61,1,0,0,0,59,61,1,0,0,0,60,56,1,0,0,0,60,59,1,0,0,0,
        61,11,1,0,0,0,62,63,3,14,7,0,63,64,5,13,0,0,64,65,3,16,8,0,65,13,
        1,0,0,0,66,67,5,14,0,0,67,68,5,16,0,0,68,69,5,12,0,0,69,73,3,14,
        7,0,70,71,5,14,0,0,71,73,5,16,0,0,72,66,1,0,0,0,72,70,1,0,0,0,73,
        15,1,0,0,0,74,75,5,17,0,0,75,76,5,12,0,0,76,79,3,16,8,0,77,79,5,
        17,0,0,78,74,1,0,0,0,78,77,1,0,0,0,79,17,1,0,0,0,80,81,3,20,10,0,
        81,82,3,18,9,0,82,85,1,0,0,0,83,85,1,0,0,0,84,80,1,0,0,0,84,83,1,
        0,0,0,85,19,1,0,0,0,86,94,5,6,0,0,87,94,5,7,0,0,88,94,5,8,0,0,89,
        94,5,9,0,0,90,94,5,10,0,0,91,92,5,11,0,0,92,94,5,17,0,0,93,86,1,
        0,0,0,93,87,1,0,0,0,93,88,1,0,0,0,93,89,1,0,0,0,93,90,1,0,0,0,93,
        91,1,0,0,0,94,21,1,0,0,0,8,38,44,54,60,72,78,84,93
    ]

class GameTheoryParser ( Parser ):

    grammarFileName = "GameTheory.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'game'", "'players'", "'strategies'", 
                     "'payoffs'", "'analyze'", "'nash'", "'dominant'", "'pareto'", 
                     "'minimax'", "'maximin'", "'simulate'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "GAME", "PLAYERS", "STRATEGIES", "PAYOFFS", 
                      "ANALYZE", "NASH", "DOMINANT", "PARETO", "MINIMAX", 
                      "MAXIMIN", "SIMULATE", "COMMA", "COLON", "PLAYER_ID", 
                      "GAME_ID", "OPTION_ID", "NUMBER", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_playerList = 1
    RULE_strategyList = 2
    RULE_strategy = 3
    RULE_optionList = 4
    RULE_payoffList = 5
    RULE_payoff = 6
    RULE_outcomeDesitionList = 7
    RULE_outcomeValueList = 8
    RULE_commandList = 9
    RULE_command = 10

    ruleNames =  [ "program", "playerList", "strategyList", "strategy", 
                   "optionList", "payoffList", "payoff", "outcomeDesitionList", 
                   "outcomeValueList", "commandList", "command" ]

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
    COMMA=12
    COLON=13
    PLAYER_ID=14
    GAME_ID=15
    OPTION_ID=16
    NUMBER=17
    WS=18
    COMMENT=19

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

        def playerList(self):
            return self.getTypedRuleContext(GameTheoryParser.PlayerListContext,0)


        def STRATEGIES(self):
            return self.getToken(GameTheoryParser.STRATEGIES, 0)

        def strategyList(self):
            return self.getTypedRuleContext(GameTheoryParser.StrategyListContext,0)


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
            self.state = 22
            self.match(GameTheoryParser.GAME)
            self.state = 23
            self.match(GameTheoryParser.GAME_ID)
            self.state = 24
            self.match(GameTheoryParser.PLAYERS)
            self.state = 25
            self.playerList()
            self.state = 26
            self.match(GameTheoryParser.STRATEGIES)
            self.state = 27
            self.strategyList()
            self.state = 28
            self.match(GameTheoryParser.PAYOFFS)
            self.state = 29
            self.payoffList()
            self.state = 30
            self.match(GameTheoryParser.ANALYZE)
            self.state = 31
            self.commandList()
            self.state = 32
            self.match(GameTheoryParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlayerListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAYER_ID(self):
            return self.getToken(GameTheoryParser.PLAYER_ID, 0)

        def COMMA(self):
            return self.getToken(GameTheoryParser.COMMA, 0)

        def playerList(self):
            return self.getTypedRuleContext(GameTheoryParser.PlayerListContext,0)


        def getRuleIndex(self):
            return GameTheoryParser.RULE_playerList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayerList" ):
                listener.enterPlayerList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayerList" ):
                listener.exitPlayerList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlayerList" ):
                return visitor.visitPlayerList(self)
            else:
                return visitor.visitChildren(self)




    def playerList(self):

        localctx = GameTheoryParser.PlayerListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_playerList)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(GameTheoryParser.PLAYER_ID)
                self.state = 35
                self.match(GameTheoryParser.COMMA)
                self.state = 36
                self.playerList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(GameTheoryParser.PLAYER_ID)
                pass


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

        def strategy(self):
            return self.getTypedRuleContext(GameTheoryParser.StrategyContext,0)


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
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.strategy()
                self.state = 41
                self.strategyList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.strategy()
                pass


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

        def optionList(self):
            return self.getTypedRuleContext(GameTheoryParser.OptionListContext,0)


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
        self.enterRule(localctx, 6, self.RULE_strategy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(GameTheoryParser.PLAYER_ID)
            self.state = 47
            self.match(GameTheoryParser.COLON)
            self.state = 48
            self.optionList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTION_ID(self):
            return self.getToken(GameTheoryParser.OPTION_ID, 0)

        def COMMA(self):
            return self.getToken(GameTheoryParser.COMMA, 0)

        def optionList(self):
            return self.getTypedRuleContext(GameTheoryParser.OptionListContext,0)


        def getRuleIndex(self):
            return GameTheoryParser.RULE_optionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptionList" ):
                listener.enterOptionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptionList" ):
                listener.exitOptionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionList" ):
                return visitor.visitOptionList(self)
            else:
                return visitor.visitChildren(self)




    def optionList(self):

        localctx = GameTheoryParser.OptionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_optionList)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(GameTheoryParser.OPTION_ID)
                self.state = 51
                self.match(GameTheoryParser.COMMA)
                self.state = 52
                self.optionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(GameTheoryParser.OPTION_ID)
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
        self.enterRule(localctx, 10, self.RULE_payoffList)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.payoff()
                self.state = 57
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

        def outcomeDesitionList(self):
            return self.getTypedRuleContext(GameTheoryParser.OutcomeDesitionListContext,0)


        def COLON(self):
            return self.getToken(GameTheoryParser.COLON, 0)

        def outcomeValueList(self):
            return self.getTypedRuleContext(GameTheoryParser.OutcomeValueListContext,0)


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
        self.enterRule(localctx, 12, self.RULE_payoff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.outcomeDesitionList()
            self.state = 63
            self.match(GameTheoryParser.COLON)
            self.state = 64
            self.outcomeValueList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutcomeDesitionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAYER_ID(self):
            return self.getToken(GameTheoryParser.PLAYER_ID, 0)

        def OPTION_ID(self):
            return self.getToken(GameTheoryParser.OPTION_ID, 0)

        def COMMA(self):
            return self.getToken(GameTheoryParser.COMMA, 0)

        def outcomeDesitionList(self):
            return self.getTypedRuleContext(GameTheoryParser.OutcomeDesitionListContext,0)


        def getRuleIndex(self):
            return GameTheoryParser.RULE_outcomeDesitionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutcomeDesitionList" ):
                listener.enterOutcomeDesitionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutcomeDesitionList" ):
                listener.exitOutcomeDesitionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutcomeDesitionList" ):
                return visitor.visitOutcomeDesitionList(self)
            else:
                return visitor.visitChildren(self)




    def outcomeDesitionList(self):

        localctx = GameTheoryParser.OutcomeDesitionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_outcomeDesitionList)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.match(GameTheoryParser.PLAYER_ID)
                self.state = 67
                self.match(GameTheoryParser.OPTION_ID)
                self.state = 68
                self.match(GameTheoryParser.COMMA)
                self.state = 69
                self.outcomeDesitionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(GameTheoryParser.PLAYER_ID)
                self.state = 71
                self.match(GameTheoryParser.OPTION_ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutcomeValueListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(GameTheoryParser.NUMBER, 0)

        def COMMA(self):
            return self.getToken(GameTheoryParser.COMMA, 0)

        def outcomeValueList(self):
            return self.getTypedRuleContext(GameTheoryParser.OutcomeValueListContext,0)


        def getRuleIndex(self):
            return GameTheoryParser.RULE_outcomeValueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutcomeValueList" ):
                listener.enterOutcomeValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutcomeValueList" ):
                listener.exitOutcomeValueList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOutcomeValueList" ):
                return visitor.visitOutcomeValueList(self)
            else:
                return visitor.visitChildren(self)




    def outcomeValueList(self):

        localctx = GameTheoryParser.OutcomeValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_outcomeValueList)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(GameTheoryParser.NUMBER)
                self.state = 75
                self.match(GameTheoryParser.COMMA)
                self.state = 76
                self.outcomeValueList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(GameTheoryParser.NUMBER)
                pass


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
        self.enterRule(localctx, 18, self.RULE_commandList)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 8, 9, 10, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.command()
                self.state = 81
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
        self.enterRule(localctx, 20, self.RULE_command)
        try:
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(GameTheoryParser.NASH)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.match(GameTheoryParser.DOMINANT)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(GameTheoryParser.PARETO)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.match(GameTheoryParser.MINIMAX)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.match(GameTheoryParser.MAXIMIN)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 6)
                self.state = 91
                self.match(GameTheoryParser.SIMULATE)
                self.state = 92
                self.match(GameTheoryParser.NUMBER)
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





