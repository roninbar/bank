from BankAccount import BankAccount


class StudentBankAccount(BankAccount):

    def __init__(self, id: str, name: str, college_name: str):
        super().__init__(id, name)
        self.college_name = college_name

    def __str__(self):
        return super().__str__() + f" ({self.college_name})"
