class BankAccount:
    
    def __init__(self, id: str, name: str, balance: float = 0):
        self.id = id
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{{ id: "{self.id}", name: "{self.name}", balance: {self.balance} }}'
    
    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

