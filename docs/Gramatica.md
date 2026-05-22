# Gramática
Un poco de contexto de este proyecto, esta es prácticamente la tercera y esperemos ultima iteración de un proyecto académico de copiladores.

La sintaxis fue definida con ayuda de Claude, fue refinada por mi persona en algo de 2 días. La gramática está en su estado final, a partir de aquí ya no habrán más cambios.

¿Qué hizo la IA y que cambie?

Pues muchas cosas, para comenzar, si se toma la molestia de ver el historial de cambios, antes se hacia uso de paréntesis, tanto como para los payoffs y los parámetros de **un solo comando**, así que consideré que tenerlos era innecesario.

Antes el numero de parámetros era hard-code, en que sentido, la limitación de solo 2 jugadores estaba explicito en la gramática, pero ahora es una lista con N jugadores, porqué?, porque esto debería ir en el analizador semántico, no en el grammar, más que todo porque quiero tirar errores con datos productivos, como, "hey, aquí solo puede tener 2 jugadores".

Todo fue migrado a List, ya no hay estructuras Hard Coded, es decir, ahora es una gramática de libre contexto. Lo único hard-coded es la extructura del lenguaje, que eso sí se lo quiero dejar a el analizador semántico.