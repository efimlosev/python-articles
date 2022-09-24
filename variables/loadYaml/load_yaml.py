import yaml
with open("my_vars.yaml") as j:
    structure = yaml.safe_load(j)
print(structure)
secret_keys = structure['Section1']['my_super_var24']
print(type(secret_keys))
