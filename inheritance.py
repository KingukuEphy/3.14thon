class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money (self,amount,recipient):
        if self.account_balance >= amount:
            self.account_balance -=amount
            print(f"{amount} KES send to {recipient}  ")
        else:
            print("Insufficient amount send ")

class PersonalMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,id_no):
        super().__init__(account_balance,phone_number,)
        self.id_no=id_no

    def buyairtime (self,amount):
        self.account_balance -= amount
        print(f"{amount} KES airtime bought successfully")

class BusinessMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,business_id):
        super().__init__(account_balance,phone_number)
        self.business_id = business_id
    def receive_payment (self,amount):
        self.account_balance += amount
        print(f"{amount} KES received from a customer")

personal=PersonalMpesa(2000,725145604,43823372)
personal.send_money(300,722630485)
personal.buyairtime(100)

business=BusinessMpesa(3000,734546635,54335657)
business.send_money(2500,722630485)
business.receive_payment(30000)
