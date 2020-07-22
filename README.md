# pyTree

pyTree is a python class and library to display Tree from array, object, or JSON.

## Using pyTree

```python
result={'imports': [[['net', 'socket']], [['sys'], ['json'], ['xml']]], 'statements': [], 'module': 'main'}
# print(result)
# tree=pyTree().parse(result)
# print(tree)
pyTree().display(result)
```

## Output

```
\├─ imports
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
