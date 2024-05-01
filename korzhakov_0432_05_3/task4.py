class Wallet:
    payment_system = "KorzhakovPay"

    def __init__(self, name: str, currency: str):
        self._balance = 0
        self.name = name
        if currency not in ("Ruble", "USD", "EUR"):
            raise ValueError("Неподдерживаемая валюта")
        self.currency = currency

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма для пополнения должна быть положительной")
        self._balance += amount
        print(f"Баланс кошелька {self.name} успешно пополнен на {amount} {self.currency}")

    def pay(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма для оплаты должна быть положительной")
        if self._balance >= amount:
            self._balance -= amount
            print(f"Оплата с кошелька {self.name} успешно произведена в размере {amount} {self.currency}")
        else:
            print("Недостаточно средств для оплаты")

    def balance_info(self):
        print(f"Баланс кошелька {self.name}: {self._balance} {self.currency}")

    def remove_account(self):
        del self

    def __del__(self):
        print(f"Аккаунт {self.name} удален")
