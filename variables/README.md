# How to load variables in your Python project

## Why should we do  this?
Before talking  about how to pass variables to your project let us think why you should do this, I can think of these two reasons.
- Security: if you keep your access keys in the code, eventually they will leak.
- Flexibility: it is much easier test your code if you can just substitute values of your variables.

Onward.

## Load data from a file
One way to load data is importing a dummy class, where variables.py  python file that has that dummy class and main.py is the main program.

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

<span style="color:red">**Warning** </span> Both Json and Yaml libraries warn about loading file from unknown sources.

[json](https://docs.python.org/3/library/json.html)

**load_json.py**
```python
import json
with open("my_vars.json") as j:
    structure = json.load(j)
print(structure)
secret_keys = structure['Section1']['my_super_secret_var3']
```
**my_vars.json**
```json
{
  "Section1": {
    "my_super_secret_var3": "Top Secret",
    "my_super_var24": 1
  }
}
```

[pyyaml](https://pyyaml.org/)

```python
import yaml
with open("my_vars.yaml") as y:
    structure = yaml.safe_load(y)
print(structure)
secret_keys = structure['Section1']['my_super_var24']
```
```yaml
---
Section1:
  my_super_secret_var3: Top Secret
  my_super_var24: 1
```
## Use environment variables

[os](https://docs.python.org/3/library/os.html)

```bash
> export my_super_secret_var3="Top secret"simply 
>  env| grep my_super_secret_var3
my_super_secret_var3=Top secret
```
**environ.py**
```python
from os import environ
secret_key = environ['my_super_secret_var3']
print(secret_key)
```

## We can also pass a variable to the script using command line arguments.
The following example assumes that you use exactly one argument. argv[0] always represents the script name, similar to shells

[sys](https://docs.python.org/3/library/sys.html)

**command_line.py**
```python
from sys import argv, exit

if len(argv) < 2:
    print("You do not pass anything")
    exit(1)
my_secret = argv[1]
print(my_secret)
```
``` bash
>python3 command_line.py  "dada"
dada
>python3 command_line.py  "dada"
dada
>python3 command_line.py 
You do not pass anything
>echo $?
1
>python3 command_line.py  "dada"
dada
>echo $?
0
>

```
Though much easier use [argparse](https://docs.python.org/3/library/argparse.html) and not trying  to write your own sys.argv parser

**arg.py**

```python
import argparse
parser = argparse.ArgumentParser(description="just example")
parser.add_argument('--var', help="my favorite variable")
parser.add_argument('--int', type=int, help="my favorite integer")
args = parser.parse_args()
print(args.var, args.int)
```
```bash
>python3 arg.py 
None None
>python3 arg.py  --help
usage: arg.py [-h] [--var VAR] [--int INT]

just example

options:
  -h, --help  show this help message and exit
  --var VAR   my favorite variable
  --int INT   my favorite integer
>python3 arg.py  --var "dadada"
dadada None

 ```



