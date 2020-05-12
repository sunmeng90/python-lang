# Python programming language

## FAQ

### expand tuple as function parameters

When specifying a list or tuple with * as an argument, it is expanded and each element is passed to each argument.

```python
def func(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

l = ['one', 'two', 'three']

func(*l)
# one
# two
# three

func(*['one', 'two', 'three'])
# one
# two
# three

t = ('one', 'two', 'three')

func(*t)
# one
# two
# three

func(*('one', 'two', 'three'))
# one
# two
# three
```

If the number of elements does not match the number of arguments, TypeError will occur.

```python
# func(*['one', 'two'])
# TypeError: func() missing 1 required positional argument: 'arg3'

# func(*['one', 'two', 'three', 'four'])
# TypeError: func() takes 3 positional arguments but 4 were given
```

#### With default arguments

If the function has default arguments, the default arguments will be used if the number of elements is insufficient. 
If there are many elements, `TypeError` will occur.

```python
def func_default(arg1=1, arg2=2, arg3=3):
    print(arg1)
    print(arg2)
    print(arg3)

func_default(*['one', 'two'])
# one
# two
# 3

func_default(*['one'])
# one
# 2
# 3

# func_default(*['one', 'two', 'three', 'four'])
# TypeError: func_default() takes from 0 to 3 positional arguments but 4 were given
```


### Expand the dictionary (dict) with **

```python
def func(arg1, arg2, arg3):
    print(arg1)
    print(arg2)
    print(arg3)

d = {'arg1': 'one', 'arg2': 'two', 'arg3': 'three'}

func(**d)
# one
# two
# three

func(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three'})
# one
# two
# three
```

If there is no key that matches the argument name, or if there is a key that does not match the argument name, TypeError will occur.

```python
# func(**{'arg1': 'one', 'arg2': 'two'})
# TypeError: func() missing 1 required positional argument: 'arg3'

# func(**{'arg1': 'one', 'arg2': 'two', 'arg3': 'three', 'arg4': 'four'})
# TypeError: func() got an unexpected keyword argument 'arg4'
```

#### With default arguments

If the function has default arguments, only the value of the argument name matching the dictionary key is updated.

```python
def func_default(arg1=1, arg2=2, arg3=3):
    print(arg1)
    print(arg2)
    print(arg3)

func_default(**{'arg1': 'one'})
# one
# 2
# 3

func_default(**{'arg2': 'two', 'arg3': 'three'})
# 1
# two
# three

# func_default(**{'arg1': 'one', 'arg4': 'four'})
# TypeError: func_default() got an unexpected keyword argument 'arg4'
```
### function annotation or type hints

[PEP 484 -- Type Hints](https://www.python.org/dev/peps/pep-0484/) 
[PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/)

syntax:

- Parameters

```python
def foo(a: expression, b: expression = 5):
    ...
```

- Return Values

how to annotate the type of a function's return value.

```python
def sum() -> expression:
    ...
```

That is, the parameter list can now be followed by a literal -> and a Python expression. Like the annotations for 
parameters, this expression will be evaluated when the function definition is executed.


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

### set default values for function parameter

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

the following example cause error: ❌

```python
def whats_on_the_telly(penguin=[]):
    penguin.append("property of the zoo")
    return penguin
```

### `list.sort()` vs `sorted()`

- `list.sort()` method modifies the list in-place. 
- `sorted()` function builds a new sorted list from an iterable.

### iterator

[Python Iterators](https://www.programiz.com/python-programming/iterator)

Python **iterator object** must implement two special methods, `__iter__()` and `__next__()`, collectively called the **iterator protocol**.

The `iter()` function (which in turn calls the `__iter__()` method) returns an iterator from them.

#### How for loop actually works?

```python
for element in iterable:
    # do something with element
```

Is actually implemented as.

```python
# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break
```

So internally, the `for` loop creates an iterator object, `iter_obj` by calling `iter()` on the iterable.


### generator

There is a lot of work in building an iterator in Python. We have to implement a class with __iter__() and __next__() 
method, keep track of internal states, and raise StopIteration when there are no values to be returned.

This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by 
generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

#### why generator [Python Generators](https://www.programiz.com/python-programming/generator)

[How to Use Generators and yield in Python](https://realpython.com/introduction-to-python-generators/)
[A Curious Course on Coroutines and Concurrency](http://www.dabeaz.com/coroutines/)
##### Easy to Implement

Generators can be implemented in a clear and concise way as compared to their iterator class counterpart.

##### Memory Efficient

A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an 
overkill, if the number of items in the sequence is very large.

Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a time.

##### Represent Infinite Stream

Generators are excellent mediums to represent an infinite stream of data. Infinite streams cannot be stored in memory, 
and since generators produce only one item at a time, they can represent an infinite stream of data.

##### Pipelining Generators

Multiple generators can be used to pipeline a series of operations. This is best illustrated using an example.

Suppose we have a generator that produces the numbers in the Fibonacci series. And we have another generator for squaring numbers.

If we want to find out the sum of squares of numbers in the Fibonacci series, we can do it in the following way by pipelining 
the output of generator functions together.

```python
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))
```

