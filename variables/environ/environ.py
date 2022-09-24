"""
> export my_super_secret_var3="Top secret"
>  env| grep my_super_secret_var3
my_super_secret_var3=Top secret
"""

from os import environ
secret_key = environ['my_super_secret_var3']
print(secret_key)
