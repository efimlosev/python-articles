from sys import argv, exit

if len(argv) < 2:
    print("You do not pass anything")
    exit(1)
my_secret = argv[1]
print(my_secret)
