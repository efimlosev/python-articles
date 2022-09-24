import json
with open("my_vars.json") as j:
    structure = json.load(j)
print(structure)
secret_keys = structure['Section1']['my_super_secret_var3']
print(secret_keys)