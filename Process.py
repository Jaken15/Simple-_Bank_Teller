import datetime
from database import DataBase as db

class bank_teller:
    def __init__(self):
        
        self.account = [
            [11121,0],
            [11122,0],
            [11123,0],
            [11124,0]
        ]

        self.user_account = ""
        self.data = db()
        
    def deposit(self,pin_number,amount):
        try:
            for row in self.account:
                if pin_number == row[0]:
                    row[1] = amount
                    self.add_amount(amount,pin_number)
                    print(row)
                    return True            
            return False
        except Exception as e:
            print(e)

    def withdraw(self,pin_number,amount):
        self.validate(pin_number)
        try:
            for row in self.account:
                if pin_number == row[0]:
                    row[1] = amount
                    if amount < self.data.balance(self.user_account):
                        self.subtract_amount(amount,pin_number)
                        self.balance(self.user_account)
                        return True
            return False
        except Exception as e:
            print(e)

    def insert_transaction(self,transaction:str,pin_number):
        self.validate(pin_number)
        time = datetime.datetime.now().strftime("%I:%M %p")
        date = datetime.datetime.today().strftime("%d %m %Y")
        info = [pin_number,transaction,date,time]
        balance = 0
        try:
            for row in self.account:
                if pin_number == row[0]:
                    balance = row[1]
            info.insert(1,balance)
            self.data.Insert_data([info],self.user_account)
        except Exception as e:
            print(e)

    def view_transaction(self,pin_number):
        self.validate(pin_number)
        info = self.data.view_data(self.user_account)
        return info

    def Login(self,PinNumber):
        try:
            for row in self.account:
                if PinNumber == row[0]:
                    self.balance(PinNumber)
                    return True
            return False
        except Exception as e:
            print(e)

    def validate(self,pin_number):
        if pin_number == 11121:
            self.user_account = "user1"
        elif pin_number == 11122:
            self.user_account = "user2"
        elif pin_number == 11123:
            self.user_account = "user3"
        elif pin_number == 11124:
            self.user_account = "user4"
    
    def balance(self,pin_number):
        self.validate(pin_number)
        balance = self.data.balance(self.user_account)
        return balance
    
    def add_amount(self,Amount,pinumber):
        self.validate(pinumber)
        self.data.increment_column(self.user_account,Amount,pinumber)

    def subtract_amount(self,amount,pinumber):
        self.validate(pinumber)
        self.data.discrement_value(self.user_account,amount,pinumber)
        

app = bank_teller()
balance = db()