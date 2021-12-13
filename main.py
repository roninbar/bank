import argparse

from Bank import Bank

parser = argparse.ArgumentParser(description='Calculate statistics about bank accounts.')
parser.add_argument('--yaml', '-y',
                    dest='yaml',
                    default='./accounts.yaml',
                    help='Path of YAML file containing accounts')
args = parser.parse_args()

bank = Bank()

bank.load(args.yaml)

print(bank)

print(bank.stats())
