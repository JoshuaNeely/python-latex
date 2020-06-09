# python-latex

LaTex has a billion different compilers with fiddly controls and lots of dependencies to install.
Turns out there is a latex python package with a nice and simple interface. No fiddling with containerization and volume mounts. No funky interface to learn.

`./compile_tex.py` will watch the current directory for _changes_ to any `.tex` file, and compile them to a `.pdf`, without all those useless intermediary files most compilers create.

Use a nice pdf viewer that auto-refreshes, like `zathura`, to continuously develop a file.
