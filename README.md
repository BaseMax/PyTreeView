# pyTree

pyTree is a python class and library to display Tree View from array, object, or JSON.

## Data structure

The following data types are currently supported:

- Array, List
- Dict
- Value, String, ...

## Using pyTree

```python
from pyTree import pyTree

result={'imports': [[['net', 'socket']], [['sys'], ['json'], ['xml']]], 'statements': [], 'module': 'main'}
pyTree().display(result)
```
Or
```python
from pyTree import pyTree

result={'imports': [[['net', 'socket']], [['sys'], ['json'], ['xml']]], 'statements': [], 'module': 'main'}
data=pyTree().get(result)
print(data)
```

## Output

```
├─ imports
│  ├─ 0
│  │  └─ 0
│  │     ├─ 0: net
│  │     └─ 1: socket
│  └─ 1
│     ├─ 0
│     │  └─ 0: sys
│     ├─ 1
│     │  └─ 0: json
│     └─ 2
│        └─ 0: xml
├─ statements: []
└─ module: main
```

---------

# Max Base

My nickname is Max, Programming language developer, Full-stack programmer. I love computer scientists, researchers, and compilers. ([Max Base](https://maxbase.org/))

## Asrez Team

A team includes some programmer, developer, designer, researcher(s) especially Max Base.

[Asrez Team](https://www.asrez.com/)

