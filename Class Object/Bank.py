class Bank:
    def __init__(self,balance) -> None:
     self.balance = balance
     self.min_withdarw = 100
     self.max_withdarw = 100000

    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
       if amount > 0:
          self.balance += amount
    def withdraw(self, amount):
       if amount <self.min_withdarw:
          print(f'you can waithdraw below {self.min_withdarw}')
       elif amount > self.max_withdarw:
          print(f'bank fokir hoye jabe,you can not withdraw more than {self.max_withdarw}')
       else:
          self.balance -= amount
          print(f'here is your money {amount}')
          print(f'your after withdraw {self.get_balance()}')

brac = Bank(15000)
brac.withdraw(25)
brac.withdraw(250000000)
brac.withdraw(1000)

dbbl = Bank(5000)
dbbl.deposite(2000)
dbbl.deposite(2000)
print(dbbl.get_balance())

          