class User:
    myatm = None
    card_amount = 100
    atm_amount = 400

    def __init__(self, name):
        self.name = name

    def operate_atm(self):
        myatm = Atm(self.card_amount, self.atm_amount, self.name)


class Atm:




    def __init__(self, card_amount, atm_amount, name):
        self.user = name
        self.answer = input("Hello there, what would you like to do today? Deposit | Withdraw | Statement | Exit\n")
        self.card_amount = card_amount
        self.atm_amount = atm_amount

        while True:
            if (self.answer == "deposit" or self.answer == 'Deposit'):
                self.deposit()
            elif(self.answer == "withdrawal" or self.answer == "Withdrawal"):
                self.withdrawal()
            elif(self.answer == "statement" or self.answer == "Statement"):
                self.statement()
            else:
                print("Thank you {}".format(self.user))

            newsesh = input("Would you like to make another transaction? y/n\n")
            if (newsesh == 'y' or newsesh == 'Y'):
                self.answer = input("What would you like to do today? Deposit | Withdraw | Statement | Exit\n")
            else:
                exit()




    def deposit(self):
        deposit_amount = int(input("Enter how much you would like to deposit: "))
        self.card_amount -= deposit_amount
        self.atm_amount += deposit_amount

    def withdrawal(self):
        withdrawal_amount = int(input("Enter how much you would like to withdraw: "))
        if ((self.atm_amount - withdrawal_amount) < 0):
            print("Not enough funds")
        else:
            self.card_amount += withdrawal_amount
            self.atm_amount -= withdrawal_amount

    def statement(self):
        print("Amount on Card: {}".format(self.card_amount))
        print("Amount on Atm: {}".format(self.atm_amount))



def main():
    name = input("Enter your name: ")
    newuser = User(name)

    newuser.operate_atm()

    # while True:
    #     answer = input("Would you like to make operate atm again: y/n \n")
    #     if (answer == "y" or answer == 'Y'):
    #         newuser.operate_atm()
    #         Atm.statement()
    #     else:
    #         Atm.statement()
    #         exit()



if __name__ == '__main__':
    main()
