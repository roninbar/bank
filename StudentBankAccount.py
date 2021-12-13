from BankAccount import BankAccount


class InsufficientFundsError(Exception):
    pass


class StudentBankAccount(BankAccount):

    def deposit(self, amount: float):
        super(StudentBankAccount, self).deposit(amount)

    def withdraw(self, amount: float):
        if self.balance >= amount:
            super(StudentBankAccount, self).withdraw(amount)
        else:
            raise InsufficientFundsError

    def __init__(self, id: str, name: str, balance: float, college_name: str):
        super(StudentBankAccount, self).__init__(id, name, balance)
        self.college_name = college_name

    def __str__(self):
        return f'{{ BankAccount: {super().__str__()}, college: "{self.college_name}" }}'
