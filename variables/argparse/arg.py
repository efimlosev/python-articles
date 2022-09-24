import argparse
parser = argparse.ArgumentParser(description="just example")
parser.add_argument('--var', help="my favorite variable")
parser.add_argument('--int', type=int, help="my favorite integer")
args = parser.parse_args()
print(args.var, args.int)
