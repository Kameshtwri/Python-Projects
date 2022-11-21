import sys
lst = sys.argv

accBalance =  int(lst[1])
ms = []

input("Enter your 6 digit bank account number :-")
input("Enter your 4 digit pin : ")
def info():
    print("ATM : Welcome To Your Account \
\n1 - Balance Enquiry\
\n2 - Withdraw\
\n3 - Deposit Money\
\n4 - Deposit Cheque")
def atm(ch):
    global accBalance
    if ch == '1':
        print("\nYour Account Balance Is : ",accBalance)
    elif ch == '2':
        withdraw = int(input("\nEnter amount you want to withdraw in mutiple of 100 - "))
        if withdraw > accBalance:
            print("You have insufficient balance!!! Try again")
        elif withdraw < accBalance:
            check = input("\nIs this the correct amount you want to withdarw, yes, or no ? ") 
            if check =="yes":
                accBalance -= withdraw
                print("Please take your amount.\nTransaction Successful \nTHANK YOU!")
                ms.append(-1*withdraw)
            elif check == "no":
                print("Try to withdraw your money again")
    elif ch == '3':
        deposit_cash = int(input("\nEnter amount you want to deposit in multiple of 100 - "))
        check1 = input("\nIs this the correct amount you want to deposit, yes, or no ? ") 
        if check1 == "yes":
            accBalance += deposit_cash
            print("Cash deposit successfully \nTHANK YOU")
            ms.append(deposit_cash)
        elif check1 == "no":
                print("Try to deposit your money again")
    elif ch == '4':
        deposit_cheque = int(input("\nHow much money you want to deposit through Cheque - "))
        print("\nDeposit your cheque. Your money will be added in 24 hours ")
        accBalance += deposit_cheque
        print("THANK YOU")
        ms.append(deposit_cheque)
    else:
        print("WRONG CHOICE")
    
info()
choice = input("Enter Your Choice:- ")
atm(choice)
again = True 
while again:
    i = input("\nPress 1 to continue or 2 to exit from your account or \
3 to print your ministatement - ")
    if i == "1":
        print("\n")
        info()
        nchoice = input("Enter Your Choice:- ") 
        atm(nchoice)
    elif i == "2":
        break
    elif i == "3":
        if ms == []:
            print("\nMinistatement empty ")
            break
        elif ms != []:
            print("\nMINISTATEMENT OF ALL YOUR RECENT TRANSACTIONS\n")
            for j in ms:
                if j < 0:
                    print("Withdraw : ",j)
                elif j > 0:
                    print("Deposit  : ",j)
        print("\nNow your account balance is :",accBalance)
        break 
    elif i != "1" or i != "2":
        print("Wrong Choice")