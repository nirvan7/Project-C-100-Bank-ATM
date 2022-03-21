class Atm:
    def __init__(self,cardno,pinno,balance) :
        self.cardno=cardno
        self.pinno=pinno
        self.balance=balance
      
    def start(self):
       print(f"You are Withdrawing cash....")
       withdrawal=int(input("Enter amount to Withdraw "))
       nemMoney=self.balance-withdrawal
       print(f"Money after Withdrawl is",nemMoney)   
    
atm=Atm(1234567,7777777,10000)
Atm.start(atm)

