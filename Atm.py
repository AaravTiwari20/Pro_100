class Atm:
    def __init__ (self, CardNumber, Pin):
        self.CardNumber = CardNumber
        self.Pin = Pin

    def BalanceEnquiry(self):
        print("Your Balance In Your Account Is : 1000")

    def CashWithrawl(self, Amount):
        new_amount = 1000-Amount
        print("You Withrawed : "  + str(Amount) +  "Your Remaining Balance Is : "  + str(new_amount))

def main():
    name = input("Enter Your Full Name : ")
    CardNumber = input("Enter Your CardNumber : ")
    Pin = ("Enter Your Pin : ")
    new_user = Atm(CardNumber, Pin)

    print("What You Want To Do Choose Below")
    print("(1)BalanceEnquiry")
    print("(2)CashWithrawal")
    choose = int(input("Choose What You Want To Do : "))

    if(choose == 1):
        new_user.BalanceEnquiry()
    if(choose == 2):
        Amount = int(input("Enter The Amount You Want To Withraw : "))
        new_user.CashWithrawl(Amount)

if __name__ == "__main__":
    main()    
