from BankAccount import BankAccount


class InsufficientFundsError(Exception):
    pass


class StudentBankAccount(BankAccount):

    def __init__(self, id: str, name: str, balance: float, college_name: str):
        super().__init__(id, name, balance)
        self.college_name = college_name

    def __str__(self):
        return f'{{ BankAccount: {super().__str__()}, college: "{self.college_name}" }}'

    def withdraw(self, amount: float):
        if self.balance >= amount:
            super().withdraw(amount)
        else:
            raise InsufficientFundsError


