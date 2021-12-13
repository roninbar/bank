import pandas as pd
import yaml

from BankAccount import BankAccount
from BusinessBankAccount import BusinessBankAccount
from StudentBankAccount import StudentBankAccount


def make_account(account_info):
    account_type = account_info['type']
    if account_type == 'student':
        return StudentBankAccount(account_info['id'],
                                  account_info['name'],
                                  account_info['balance'],
                                  account_info['college'])
    elif account_type == 'business':
        return BusinessBankAccount(account_info['id'], account_info['name'], account_info['balance'])
    else:
        raise TypeError()


class Bank:
    _accounts: list[BankAccount]

    def __init__(self):
        self._accounts = []

    def __str__(self) -> str:
        return f"[{', '.join(str(a) for a in self._accounts)}]"

    def __getitem__(self, id: str):
        return next(a for a in self._accounts if a.id == id)

    def load(self, filename: str):
        with open(filename, 'r') as accounts_yaml:
            self._accounts.extend(make_account(a) for a in yaml.full_load(accounts_yaml))

    def add_account(self, account: BankAccount):
        self._accounts.append(account)

    def stats(self):
        balances = pd.Series(a.balance for a in self._accounts)
        return {
            'mean': balances.mean(),
            'median': balances.median(),
            'standard_deviation': balances.std(),
            'q0.1': balances.quantile(0.1),
            'q0.9': balances.quantile(0.9),
        }
