# ATMProjectDemo.py<--Main Program
from ATMExcept import DepositError, WithDrawError, InSuffFundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
while(True):
    try:
        menu()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tDon't Deposit -Ve amd Zero Values")
                except ValueError:
                    print("\tDont Try to deposit alnums,strs and symbols")
            case 2:
                try:
                    withdraw()
                except WithDrawError:
                    print("\tDon't Withdraw -Ve amd Zero Values")
                except ValueError:
                    print("\tDont Try to withdraw alnums,strs and symbols")
                except InSuffFundError:
                    print("\tUr Account does not contains Funds--Read Python Notes")
            case 3:
                balenq()
            case 4:
                print("Thx for using this Project")
                break
            case _:
                print("\tUr Selection of Operation is wrong-try again")
    except ValueError:
        print("\tDon't enter alnums,strs and symbols for Choice--try again")