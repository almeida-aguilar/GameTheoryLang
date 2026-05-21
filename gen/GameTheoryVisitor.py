# Generated from GameTheory.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GameTheoryParser import GameTheoryParser
else:
    from GameTheoryParser import GameTheoryParser

# This class defines a complete generic visitor for a parse tree produced by GameTheoryParser.

class GameTheoryVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GameTheoryParser#program.
    def visitProgram(self, ctx:GameTheoryParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryParser#playerList.
    def visitPlayerList(self, ctx:GameTheoryParser.PlayerListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryParser#strategyList.
    def visitStrategyList(self, ctx:GameTheoryParser.StrategyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryParser#strategy.
    def visitStrategy(self, ctx:GameTheoryParser.StrategyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryParser#optionList.
    def visitOptionList(self, ctx:GameTheoryParser.OptionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryParser#payoffList.
    def visitPayoffList(self, ctx:GameTheoryParser.PayoffListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryParser#payoff.
    def visitPayoff(self, ctx:GameTheoryParser.PayoffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryParser#commandList.
    def visitCommandList(self, ctx:GameTheoryParser.CommandListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GameTheoryParser#command.
    def visitCommand(self, ctx:GameTheoryParser.CommandContext):
        return self.visitChildren(ctx)



del GameTheoryParser