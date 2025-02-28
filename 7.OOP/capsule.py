class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # Private variable
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.__balance

# 객체 생성
account = BankAccount(1000)

# 메서드 사용
account.deposit(500)
account.withdraw(200)
print(account.get_balance()) # result: 1300

# 직접 접근 시도(에러 발생)