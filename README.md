# Schemer

A database schema visualization tool


## Installation

### From source

Clone the repo, and run `pip install .` from within the cloned repo.

The installation of `pygraphviz` might fail on an M1 Mac, in that case run:

```bash
pip install --global-option=build_ext --global-option="-I$(brew --prefix graphviz)/include" --global-option="-L$(brew --prefix graphviz)/lib" pygraphviz
```

and run `pip install .` again.