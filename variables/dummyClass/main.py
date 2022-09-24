from variables import *

for ii in dir(Variables):
    if not ii.startswith('__'):
        print(f"Variable: {ii}, Value: {getattr(Variables, ii)})")


my_local_var = Variables().my_super_secret_var1

print(my_local_var)

