import yaml

from BankAccount import BankAccount
from BusinessBankAccount import BusinessBankAccount
from StudentBankAccount import StudentBankAccount


def make_account(account_info):
    account_type = account_info['type']
    if account_type == 'student':
        return StudentBankAccount(account_info['id'], account_info['name'], account_info['college'])
    elif account_type == 'business':
        return BusinessBankAccount(account_info['id'], account_info['name'])
    else:
        raise TypeError()


class Bank:
    
    def __init__(self):
        self.accounts = []

    def __str__(self) -> str:
        return '\n---\n'.join(str(a) for a in self.accounts)

    def load(self, filename: str):
        with open(filename, 'r') as accounts_yaml:
            self.accounts.extend(make_account(a) for a in yaml.full_load(accounts_yaml))

    def add_account(self):
        self.accounts.append(BankAccount())

    def stats(self):
        return {'mean': 0, 'std': 1, 'p10': 0, 'median': 0, 'p90': 0}
    
    pass
