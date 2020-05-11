

### get current module path
```python
import os
os.path.abspath(__file__)
```

### change working dir
```python
import os
os.chdir("foo/bar")
```

### get command line arguments
```python
import argparse
import os
parser = argparse.ArgumentParser()
parser.add_argument("url", help="video url")
parser.add_argument("-o", "--output", help="output folder for downloading", default=".")
parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")  # flag, if specified True
args = parser.parse_args()
output = os.path.abspath(args.output)
print(f"start downloading video on {args.url} to {output}")
```

**Default parameter values are evaluated from left to right when the function definition is executed.**
 
This means that the expression is evaluated once, when the function is defined, and that the same “pre-computed” value 
is used for each call. This is especially important to understand when a default parameter is a mutable object, such as 
a list or a dictionary: if the function modifies the object (e.g. by appending an item to a list), the default value is 
in effect modified. This is generally not what was intended. A way around this is to use None as the default, and 
explicitly test for it in the body of the function, e.g.:

```python
def whats_on_the_telly(penguin=None):
    if penguin is None:
        penguin = []
    penguin.append("property of the zoo")
    return penguin
```