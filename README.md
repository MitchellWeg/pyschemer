# PySchemer

A database schema visualization tool

## Usage
This app will try to create an ERD from an existing database. It tries to achieve this by asking the database about certain things, namely tables (their names and fields), and their relationships with other tables (foreign keys).

When you want to implement it for another SQL dialect, some fields might need to be overridden:
* Database.get_tables
* Database.describe_tables
* Database.get_relationships

See the examples directory for a working example for [MonetDB](https://monetdb.org/)

## Installation

### From pip

`pip install pyschemer`

### From source

Clone the repo, and run `pip install .` from within the cloned repo.

The installation of `pygraphviz` might fail on an M1 Mac, in that case run:

```bash
pip install --global-option=build_ext --global-option="-I$(brew --prefix graphviz)/include" --global-option="-L$(brew --prefix graphviz)/lib" pygraphviz
```

and run `pip install .` again.