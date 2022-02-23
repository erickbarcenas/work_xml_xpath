# Reading XML files

Learning to read XML files and the use of xpath

## Running the program

From within the project's root directory, start the game with `$ python main.py your_filename.xml your_path_expresion`. You will need to install python if you haven't already.

# Examples

```
python main.py bookstore.xml "//book/price | //book/price"
```

```
python main.py bookstore.xml "//title | //price"
```

```
python main.py bookstore.xml "/bookstore/book/title | //price"

```

## Reference sources
https://lxml.de/installation.html

https://www.w3schools.com/xml/default.asp

https://www.w3schools.com/xml/xpath_syntax.asp
