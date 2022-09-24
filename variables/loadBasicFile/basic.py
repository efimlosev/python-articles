my_vars = {}
with open("my_vars.txt") as v:
    for line in v:
        k, v = line.strip().replace('"', '').split('=')
        my_vars[k] = v

for k, v in my_vars.items():
    print(f"Variable: {k} Variable Value: {v}")
