import sys
import os
from antlr4 import CommonTokenStream, FileStream, Token
from GameTheoryLexer import GameTheoryLexer
from GameTheoryParser import GameTheoryParser
from antlr4.error.ErrorListener import ErrorListener


# ─────────────────────────────────────────────
# Error listener personalizado
# ─────────────────────────────────────────────

class ErrorCollector(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            "line"   : line,
            "column" : column,
            "symbol" : offendingSymbol.text if offendingSymbol else "?",
            "msg"    : msg
        })


# ─────────────────────────────────────────────
# Mostrar tokens
# ─────────────────────────────────────────────

def mostrar_tokens(stream, lexer):
    print("\n" + "═" * 55)
    print("  FASE 1 — LEXER (tokens)")
    print("═" * 55)
    print(f"  {'#':<5} {'TIPO':<20} {'VALOR':<20} {'LÍNEA'}")
    print("  " + "─" * 51)

    for i, token in enumerate(stream.tokens):
        if token.type == Token.EOF:
            print(f"  {i:<5} {'EOF':<20} {'<fin>':<20} {token.line}")
            break

        nombre = GameTheoryLexer.symbolicNames[token.type] \
                 if token.type < len(GameTheoryLexer.symbolicNames) \
                 else f"TYPE_{token.type}"
        valor  = repr(token.text)
        print(f"  {i:<5} {nombre:<20} {valor:<20} {token.line}")


# ─────────────────────────────────────────────
# Mostrar árbol de parseo
# ─────────────────────────────────────────────

def mostrar_arbol(tree, parser, indent=0):
    from antlr4 import TerminalNode
    prefijo = "  " + "│  " * indent

    if isinstance(tree, TerminalNode):
        token  = tree.getSymbol()
        nombre = GameTheoryLexer.symbolicNames[token.type] \
                 if token.type < len(GameTheoryLexer.symbolicNames) \
                 else "TOKEN"
        print(f"{prefijo}└─ [TERMINAL] {nombre} = {repr(token.text)}  (línea {token.line})")
    else:
        nombre_regla = parser.ruleNames[tree.getRuleIndex()]
        print(f"{prefijo}├─ [{nombre_regla}]")
        for hijo in tree.getChildren():
            mostrar_arbol(hijo, parser, indent + 1)


# ─────────────────────────────────────────────
# Mostrar errores
# ─────────────────────────────────────────────

def mostrar_errores(errores_lexer, errores_parser):
    total = len(errores_lexer) + len(errores_parser)
    print("\n" + "═" * 55)
    print(f"  ERRORES ({total} encontrados)")
    print("═" * 55)

    if not errores_lexer and not errores_parser:
        print("  ✓ Sin errores léxicos ni sintácticos.")
        return

    for e in errores_lexer:
        print(f"  [LÉXICO]   línea {e['line']}:{e['column']} — símbolo '{e['symbol']}' — {e['msg']}")

    for e in errores_parser:
        print(f"  [SINTAXIS] línea {e['line']}:{e['column']} — símbolo '{e['symbol']}' — {e['msg']}")


# ─────────────────────────────────────────────
# Mostrar resumen
# ─────────────────────────────────────────────

def mostrar_resumen(stream, errores_lexer, errores_parser):
    total_tokens = sum(1 for t in stream.tokens if t.type != Token.EOF)
    print("\n" + "═" * 55)
    print("  RESUMEN")
    print("═" * 55)
    print(f"  Tokens reconocidos : {total_tokens}")
    print(f"  Errores léxicos    : {len(errores_lexer)}")
    print(f"  Errores sintácticos: {len(errores_parser)}")
    estado = "✓ OK" if not errores_lexer and not errores_parser else "✗ FALLÓ"
    print(f"  Estado             : {estado}")
    print("═" * 55 + "\n")


# ─────────────────────────────────────────────
# Análisis principal
# ─────────────────────────────────────────────

def analizar(archivo):
    if not os.path.exists(archivo):
        print(f"[ERROR] Archivo no encontrado: {archivo}")
        sys.exit(1)

    if not archivo.endswith(".gt"):
        print(f"[ADVERTENCIA] El archivo '{archivo}' no tiene extensión .gt")

    print("\n" + "═" * 55)
    print(f"  Archivo : {archivo}")
    print("═" * 55)

    # Leer archivo
    entrada = FileStream(archivo, encoding="utf-8")

    # ── Lexer ──
    lexer             = GameTheoryLexer(entrada)
    error_lexer       = ErrorCollector()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_lexer)

    stream = CommonTokenStream(lexer)
    stream.fill()
    mostrar_tokens(stream, lexer)

    # ── Parser ──
    stream.seek(0)
    parser             = GameTheoryParser(stream)
    error_parser       = ErrorCollector()
    parser.removeErrorListeners()
    parser.addErrorListener(error_parser)

    tree = parser.program()

    print("\n" + "═" * 55)
    print("  FASE 2 — PARSER (árbol de parseo)")
    print("═" * 55)
    print("\n  Árbol compacto:")
    print("  " + tree.toStringTree(recog=parser))
    print("\n  Árbol expandido:")
    mostrar_arbol(tree, parser)

    # ── Errores y resumen ──
    mostrar_errores(error_lexer.errors, error_parser.errors)
    mostrar_resumen(stream, error_lexer.errors, error_parser.errors)


# ─────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python driver.py <archivo.gt>")
        sys.exit(1)

    analizar(sys.argv[1])
