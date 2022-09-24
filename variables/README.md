# How to load variables in your Python project

## Why should we do  this?
Before talking  about how to pass variables to your project let us think why you should do this,at least I thnink of these two reasons, and please correct me if I am wrong.

- Security, if  keep your acces keys in the code eventually, they would leak.
- Flexibility, it much easier test your code if youcan just substitute values of your variables.

So let us begin.


One way to load data would be importing a dummy class where, variables.py  python file that has that dummy class and main.py the main program.

**variables.py**

```python
class Variables:
    my_super_secret_var1 = "Top Secret"
    my_super_var2  = 1
```
**main.py**

```python
from variables import *

for ii in dir(Variables):
    if not ii.startswith('__'):
        print(f"Variable: {ii}, Value: {getattr(Variables, ii)})")

my_local_var = Variables().my_super_secret_var1

print(my_local_var)
```

The other way is simply load a text file and parse it by built-n method

**basic.py**
``` python
my_vars = {}
with open("my_vars.txt") as v:
    for line in v:
        k, v = line.strip().replace('"', '').split('=')
        my_vars[k] = v

for k, v in my_vars.items():
    print(f"Variable: {k} Variable Values: {v}")
```
**my_vars.txt**
``` text
    my_super_secret_var1="Top Secret"
    my_super_var2 = 1
```
Similarly, we  can load, Json, Yaml files or handle parsing configs using configparser module. Let us explore these options.

[configparser](https://docs.python.org/3/library/configparser.html)

**config_parser.py**
```python
from configparser import ConfigParser

parser = ConfigParser()
parser.read("my_vars.ini")
for section in parser.sections():
    for option in parser.options(section):
        print(f"Variable: {option} Variable value: {parser.get(section, option)}")
```

**my_vars.ini**
```text
[Section1]

my_super_secret_var3="Top Secret"
my_super_var24=1

```