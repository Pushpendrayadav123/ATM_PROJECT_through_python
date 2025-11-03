#ATMOperations.py<---Module Name
from ATMExcept import DepositError,WithDrawError,InSuffFundError
bal=500.00 # here bal is global Variable
def deposit():
    damt=float(input("Enter Ur Deposit Amount:")) # implcitly there is a chance of occuring ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("\tUr Account xxxxxxxx123 Credited with INR:{}".format(damt))
        print("\tUr Account xxxxxxxx123 Balance after Deposit INR:{}".format(bal))

def withdraw():
    global bal
    wamt = float(input("Enter Ur Withdraw Amount:"))  # implcitly there is a chance of occuring ValueError
    if(wamt<=0):
        raise WithDrawError
    elif((wamt+500)>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("\tUr Account xxxxxxxx123 Debited with INR:{}".format(wamt))
        print("\tUr Account xxxxxxxx123 Balance after Withdraw INR:{}".format(bal))

def balenq():
    print("\tUr Account xxxxxxxx123 Balance with INR:{}".format(bal))
