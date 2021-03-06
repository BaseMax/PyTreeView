# PyTree-View

PyTreeView is a python class and library to display Tree View from array, object, or JSON.

> Can someone help me to publish this package in pypi? https://github.com/BaseMax/PyTreeView/issues/1

## Data structure

The following data types are currently supported:

- Array, List
- Dict
- Value, String, ...

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

## Using PyTreeView

```python
from PyTreeView import PyTreeView

result={'imports': [[['net', 'socket']], [['sys'], ['json'], ['xml']]], 'statements': [], 'module': 'main'}
PyTreeView().display(result)
```
Or
```python
from PyTreeView import PyTreeView

result={'imports': [[['net', 'socket']], [['sys'], ['json'], ['xml']]], 'statements': [], 'module': 'main'}
data=PyTreeView().get(result)
print(data)
```

---------

# Max Base

My nickname is Max, Programming language developer, Full-stack programmer. I love computer scientists, researchers, and compilers. ([Max Base](https://maxbase.org/))

## Asrez Team

A team includes some programmer, developer, designer, researcher(s) especially Max Base.

[Asrez Team](https://www.asrez.com/)

