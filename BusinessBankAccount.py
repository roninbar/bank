from BankAccount import BankAccount


class BusinessInfo:

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f'{{ id: "{self.id}", name: "{self.name}" }}'


class BusinessBankAccount(BankAccount):

    def deposit(self, amount: float):
        super(BusinessBankAccount, self).deposit(amount)

    def withdraw(self, amount: float):
        super(BusinessBankAccount, self).withdraw(amount)

    def __init__(self, id: str, name: str, balance: float):
        super(BusinessBankAccount, self).__init__(id, name, balance)
        self.business_info = BusinessInfo(id, name)

    def __str__(self):
        return f'{{ super: {super().__str__()}, business_info: {self.business_info} }}'
