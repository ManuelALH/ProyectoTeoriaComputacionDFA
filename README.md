# Automata Finito Determinista

Proyecto Final basado en [Automata](https://github.com/caleb531/automata) libreria de Python

## Prerequisitos

[Automata](https://github.com/caleb531/automata)\
`pip install automata-lib`\
`pip install pandas`\
`pip install graphviz`\
`pip install colormath`\
`pip install jupyterlab`

## Contenido

- [Visual Automata](#automata-finito-determinista)
  - [Prerequisitos](#prerequisitos)
  - [Contenido](#contenido)
    - [VisualDFA](#visualdfa)
      - [Importar](#importar)
      - [Instanciando DFAs](#instanciando-dfas)
      - [Convertir](#convertir)
      - [DFA Minimo](#dfa-minimo)
      - [Tabla Transiciones](#tabla-transiciones)
      - [Comprobar Entradas](#comprobar-entradas)
      - [Mostrar Diagramas](#mostrar-diagramas)
  - [Autor](#autor)

### VisualDFA

#### Importar

Importar las clases para el DFA

```python
from automata.fa.dfa import DFA

from visual_automata.fa.dfa import VisualDFA
```

#### Instanciando DFAs

Definir un automata finito que acepta cualquier cadena que termina con 00 o 11

```python
dfa = VisualDFA(
    states={"q0", "q1", "q2", "q3", "q4"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": "q3", "1": "q1"},
        "q1": {"0": "q3", "1": "q2"},
        "q2": {"0": "q3", "1": "q2"},
        "q3": {"0": "q4", "1": "q1"},
        "q4": {"0": "q4", "1": "q1"},
    },
    initial_state="q0",
    final_states={"q2", "q4"},
)
```

#### Convertir

Los automatas pueden ser convertidos a una libreria propia desarrollada para su visualizacion

Definir un automata finito que acepta cualquier cadena que termina con 00 o 11

```python
dfa = DFA(
    states={"q0", "q1", "q2", "q3", "q4"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": "q3", "1": "q1"},
        "q1": {"0": "q3", "1": "q2"},
        "q2": {"0": "q3", "1": "q2"},
        "q3": {"0": "q4", "1": "q1"},
        "q4": {"0": "q4", "1": "q1"},
    },
    initial_state="q0",
    final_states={"q2", "q4"},
)
```

Convertir el automata 

```python
dfa = VisualDFA(dfa)
```

#### DFA Minimo

Crea un Automata Finito Determinista Minimo, acepta las mismas entradas que el anterior. Los estados inalcanzables son removidos, y los equivalentes salen.

```python
new_dfa = VisualDFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'0', '1'},
    transitions={
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q2', '1': 'q1'}
    },
    initial_state='q0',
    final_states={'q1'}
)
```

```python
new_dfa.table
```

```text
      0    1
→q0  q0  *q1
*q1  q0   q2
q2   q2  *q1
```

```python
new_dfa.show_diagram()
```

![alt text](https://github.com/ManuelALH/ProyectoTeoriaComputacionDFA/blob/main/images/new_dfa.png?raw=true "new_dfa")

```python
minimal_dfa = VisualDFA.minify(new_dfa)
minimal_dfa.show_diagram()
```

![alt text](https://github.com/ManuelALH/ProyectoTeoriaComputacionDFA/blob/main/images/minimal_dfa.png?raw=true "minimal_dfa")

```python
minimal_dfa.table
```

```text
                0        1
→{q0,q2}  {q0,q2}      *q1
*q1       {q0,q2}  {q0,q2}
```

#### Tabla Transiciones

Muestra la tabla de transiciones para el automata dado

```python
dfa.table
```

```text
       0    1
→q0   q3   q1
q1    q3  *q2
*q2   q3  *q2
q3   *q4   q1
*q4  *q4   q1
```

#### Comprobar entradas

`1001` No termina con `00` o `11`, asi que es `Rechazada`

```python
dfa.input_check("1001")
```

```text
          [Rejected]                         
Step: Current state: Input symbol: New state:
1                →q0             1         q1
2                 q1             0         q3
3                 q3             0        *q4
4                *q4             1         q1
```

`10011` termina con `11`, asi que es `Aceptada`

```python
dfa.input_check("10011")
```

```text
          [Accepted]                         
Step: Current state: Input symbol: New state:
1                →q0             1         q1
2                 q1             0         q3
3                 q3             0        *q4
4                *q4             1         q1
5                 q1             1        *q2
```

#### Mostrar Diagrama

```python
dfa.show_diagram()
```

![alt text](https://github.com/ManuelALH/ProyectoTeoriaComputacionDFA/blob/main/images/dfa.png?raw=true "dfa")

El metodo `show_diagram` tambien acepta cadenas de entrada, y retornara un grafico con flechas `Rojas` para resultados `Rechazados` y flechas color `Verde` para resultados `Aceptados`. Tambien mostrara una tabla con el orden de los estados. Los estados en esta tabla corresponderan con el  `[numero]` sobre cada flecha.


```python
dfa.show_diagram("1001")
```

```text
          [Rejected]                         
Step: Current state: Input symbol: New state:
1                →q0             1         q1
2                 q1             0         q3
3                 q3             0        *q4
4                *q4             1         q1
```

![alt text](https://github.com/ManuelALH/ProyectoTeoriaComputacionDFA/blob/main/images/dfa_1001.png?raw=true "dfa_1001")

```python
dfa.show_diagram("10011")
```

```text
          [Accepted]                         
Step: Current state: Input symbol: New state:
1                →q0             1         q1
2                 q1             0         q3
3                 q3             0        *q4
4                *q4             1         q1
5                 q1             1        *q2
```

![alt text](https://github.com/ManuelALH/ProyectoTeoriaComputacionDFA/blob/main/images/dfa_10011.png?raw=true "dfa_10011")

## Autor

- **[Lepiz Hernandez Manuel Alejandro](https://github.com/ManuelALH)**
