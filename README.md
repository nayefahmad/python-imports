# python-imports
Experimenting with ways to import in python

Reference: [Understanding Python imports, __init__.py and pythonpath — once and for all](https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355)

## Problem 1
Assume this directory structure: 

```
- python-imports (root)
  - scripts 
    - ex1.py
    - ex2.py
- README.md 
```

`ex2.py` imports from `ex1.py` using `import ex1` 

**Running `ex1.py` and `ex2.py` from command line: Works!**
```
$ cd scripts
$ python -m ex1  # works
$ python -m ex2  # works  
```
From the link above: 
> The output from sys.path will always contain the current directory at index 0! The current directory being the one where the script being run resides.
This is the reason importing is fairly straightforward when both the caller and callee modules reside within the same directory.


**Running `ex1.py` and `ex2.py` using PyCharm GUI: Works!**
- From editor window, right-click and select "Run", or hit `Ctrl + Shift + F10`
- Also works if using debugger.
- This works because the IDE knows to add the location of the file to `sys.path`. 
Note that the following is the first line of output when run:
  
```
C:\Users\vr229e\AppData\Local\r-miniconda\python.exe C:/Nayef/python-imports/scripts/ex2.py
```

**Running `ex1.py` and `ex2.py` using PyCharm console: Doesn't work!**
- In `ex2.py`, place cursor on the line `import ex1`, and hit `Ctrl + Enter` to run. 
  This will fail.
- This doesn't work because the Console doesn't know about the `scripts` subfolder.
Note that it outputs a line like this: 
  
```python
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Nayef\\python-imports', 'C:/Nayef/python-imports'])
```

- If you print `sys.path` in the console, you'll see that it doesn't include `C:/Nayef/python-imports/scripts/`
- To fix this, you can just run this in console: `sys.path.append('scripts')`.

## Conclusion
Running from command line (or using GUI to mimic this) will know which directory
the current script resides in, and will have no problem importing other scripts 
in the same directory. 

However, when running line-by-line in the PyCharm console, we may need to 
use `sys.path.append()` to add the sub-directory name. By default, the console 
only knows about the root directory. 

### Notes 
- `os.path.dirname(__file__)` works when run from CLI, but not when run line-by-line in 
PyCharm console. 
  

## Problem 2
