# mainmethod.py

Provides C-like main method support.

Sample usage:

```py
# file: script.py
from mainmethod import mainmethod

@mainmethod
def main():
    print('hello, world!')
```

Running the script defined above will execute the method `main`.
```
$ python script.py
hello, world
```

No more need for
```py
if __name__ == '__main__':
    main()
```

The decorator inspects the method marked as main and supports these signatures;
1. `main()`.                        -> No command line arguments.
2. `main(argv)` (or `main(args)`)   -> Get `sys.argv` passed to the main method call.

```py
from mainmethod import mainmethod

@mainmethod
def main(argv):
    message = 'hello, world'

    if '--loud' in argv:
        message = message.upper()

    print(message)
```

The decorator also automatically gathers the return value from the main method and uses it as the return status code.
