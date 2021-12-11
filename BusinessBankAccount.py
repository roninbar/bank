from BankAccount import BankAccount


class BusinessInfo:
    
    def __init__(self, bid: str, name: str):
        self.id = bid
        self.name = name
        
    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class BusinessBankAccount(BankAccount):

    def __init__(self, id: str, name: str):
        super().__init__(id, name)
        self.business_info = BusinessInfo(id, name)
        
    def __str__(self):
        return super().__str__() + f" ({self.business_info})"

