# Game Theory Programming Language (GTPL)

[Español](#español) | [English](#english)

---

## English

Game Theory Programming Language is a domain-specific language for defining and analyzing strategic games between two players.

### What is it?

A declarative language that allows you to write game theory models simply and analyze them automatically.

### What is it for?

- Define games between two players
- Calculate Nash equilibria
- Identify dominant strategies
- Analyze Pareto optimality
- Calculate minimax/maximin strategies
- Simulate game dynamics

### Syntax

```gt
game PrisonersDilemma

players A, B

strategies
    A: cooperate, defect
    B: cooperate, defect

payoffs
    A cooperate, B cooperate : 3, 3
    A cooperate, B defect    : 0, 5
    A defect,    B cooperate : 5, 0
    A defect,    B defect    : 1, 1

analyze
    nash
    dominant
    pareto
    simulate 50
```

### Analysis Commands

- `nash` - Find Nash equilibria
- `dominant` - Identify dominant strategies
- `pareto` - Find Pareto optimal outcomes
- `minimax` - Calculate minimax strategy
- `maximin` - Calculate maximin strategy
- `simulate N` - Run N simulations

### Status

🚧 In development - Currently supports 2 players

---

## Español

Game Theory Programming Language es un lenguaje de dominio específico para definir y analizar juegos estratégicos entre dos jugadores.

### ¿Qué es?

Un lenguaje declarativo que permite escribir modelos de teoría de juegos de forma simple y analizarlos automáticamente.

### ¿Para qué?

- Definir juegos entre dos jugadores
- Calcular equilibrios de Nash
- Identificar estrategias dominantes
- Analizar optimalidad de Pareto
- Calcular estrategias minimax/maximin
- Simular dinámicas de juego

### Sintaxis

```gt
game PrisonersDilemma

players A, B

strategies
    A: cooperate, defect
    B: cooperate, defect

payoffs
    A cooperate, B cooperate : 3, 3
    A cooperate, B defect    : 0, 5
    A defect,    B cooperate : 5, 0
    A defect,    B defect    : 1, 1

analyze
    nash
    dominant
    pareto
    simulate 50
```

### Comandos de Análisis

- `nash` - Encontrar equilibrios de Nash
- `dominant` - Identificar estrategias dominantes
- `pareto` - Encontrar resultados óptimos de Pareto
- `minimax` - Calcular estrategia minimax
- `maximin` - Calcular estrategia maximin
- `simulate N` - Ejecutar N simulaciones

### Estado

🚧 En desarrollo - Por ahora soporta 2 jugadores