# Generated from code/GameTheory.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GameTheoryParser import GameTheoryParser
else:
    from GameTheoryParser import GameTheoryParser

# This class defines a complete listener for a parse tree produced by GameTheoryParser.
class GameTheoryListener(ParseTreeListener):

    # Enter a parse tree produced by GameTheoryParser#program.
    def enterProgram(self, ctx:GameTheoryParser.ProgramContext):
        pass

    # Exit a parse tree produced by GameTheoryParser#program.
    def exitProgram(self, ctx:GameTheoryParser.ProgramContext):
        pass


    # Enter a parse tree produced by GameTheoryParser#strategy.
    def enterStrategy(self, ctx:GameTheoryParser.StrategyContext):
        pass

    # Exit a parse tree produced by GameTheoryParser#strategy.
    def exitStrategy(self, ctx:GameTheoryParser.StrategyContext):
        pass


    # Enter a parse tree produced by GameTheoryParser#strategyList.
    def enterStrategyList(self, ctx:GameTheoryParser.StrategyListContext):
        pass

    # Exit a parse tree produced by GameTheoryParser#strategyList.
    def exitStrategyList(self, ctx:GameTheoryParser.StrategyListContext):
        pass


    # Enter a parse tree produced by GameTheoryParser#payoffList.
    def enterPayoffList(self, ctx:GameTheoryParser.PayoffListContext):
        pass

    # Exit a parse tree produced by GameTheoryParser#payoffList.
    def exitPayoffList(self, ctx:GameTheoryParser.PayoffListContext):
        pass


    # Enter a parse tree produced by GameTheoryParser#payoff.
    def enterPayoff(self, ctx:GameTheoryParser.PayoffContext):
        pass

    # Exit a parse tree produced by GameTheoryParser#payoff.
    def exitPayoff(self, ctx:GameTheoryParser.PayoffContext):
        pass


    # Enter a parse tree produced by GameTheoryParser#commandList.
    def enterCommandList(self, ctx:GameTheoryParser.CommandListContext):
        pass

    # Exit a parse tree produced by GameTheoryParser#commandList.
    def exitCommandList(self, ctx:GameTheoryParser.CommandListContext):
        pass


    # Enter a parse tree produced by GameTheoryParser#command.
    def enterCommand(self, ctx:GameTheoryParser.CommandContext):
        pass

    # Exit a parse tree produced by GameTheoryParser#command.
    def exitCommand(self, ctx:GameTheoryParser.CommandContext):
        pass



del GameTheoryParser