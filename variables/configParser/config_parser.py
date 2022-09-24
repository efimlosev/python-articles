from configparser import ConfigParser

parser = ConfigParser()
parser.read("my_vars.ini")
for section in parser.sections():
    for option in parser.options(section):
        print(f"Variable: {option} Variable value: {parser.get(section, option)}")
