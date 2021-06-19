class atm(object):
    def __init__(self ,cardNumber ,pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def cashWithdrawl(self):
        cash = 10000
        withdrawlAmount = int(input('Enter the amount you want to withdraw :'))
        
        if(withdrawlAmount > cash):
            print('You have '+ str(cash) +' rupees in your bank, cant withdraw more than that')

        else:
            cash = cash - withdrawlAmount
            print('Transaction Successful!! You have '+str(cash) + ' amount in your bank')

cardNumber = input('Enter your card number :')
pin = input('Enter your pin :')
account = atm(cardNumber, pin)
account.cashWithdrawl()