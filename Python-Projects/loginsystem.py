#Login system
#check if there is account or not
#if not make an account
#then ask what you want to save in a text file
#then  take the text, store it in text file
#then close the account

class AccountCheck:
    
    def accountcheck(self):
        checkid = 0
        checkps = 0
        print("Login into your account.\n")
        email = input("Enter your Email-ID - ")
        
        rd = open("loginsystem.txt","r+")
        d = rd.readlines()
        #print(d)
        rd.truncate()
        for lines in d:
            if email in lines:
                checkid = 1
        if checkid == 0:
            print("\nEmail-Id doesn't exist")
            return 0
        while checkps == 0:
            ps = input("Enter your Password - ")  
            for pw in d: 
                #ps = input("Enter your Password - ") 
                if ps in pw:
                    checkps = 1
            if checkps == 1:
                print("Account Opened!!!")
            elif ps == 'exit':
                return 0
            else:
                print("\nPassword Invalid. Enter again or type 'exit' to exit")
        rd.close()
    
            


class NewAccount:
    up = 0
    lc = 0
    num = 0
    sc = 0
    pswrd = " "
    pswrd_confirm = " "
    Firstname = " "
    Lastname = " "
    DOB = " "
    
    def __init__(self,email):
        self.email = email
    
    def BasicDetails(self):
        NewAccount.Firstname = input("Enter your First name :- ")
        NewAccount.Lastname = input("Enter your Last name :- ")
        NewAccount.DOB = input("Enter your DOB :- ")
        
    def check(self):   
        sch = {"!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","}","/","~"}
        l = 0
        counter = 0
        while counter == 0:
            print("\nCreate your password")
            NewAccount.pswrd = str(input("Passwords must have upper and lower case letters, at least 1 number and special character, \
not match or contain email, and be at least 8 characters long. :- "))
            for i in NewAccount.pswrd:
                l = l+1
            if l < 8:
                print("There's at least 8 characters in your password.")
            
            for i in range(len(self.pswrd)):
                if NewAccount.pswrd[i].isupper():
                    NewAccount.up = 1 
            if NewAccount.up == 0 :
                print("Password must contain upper case character.")
            
            for i in range(len(self.pswrd)): 
                if NewAccount.pswrd[i].islower():
                    NewAccount.lc = 1
            if NewAccount.lc == 0:
                print("Password must contain lower case character.")
        
            for i in range(len(self.pswrd)):
                if NewAccount.pswrd[i].isnumeric():
                    NewAccount.num= 1 
            if NewAccount.num == 0:
                print("Password must contain numeric character.")
            
            for i in range(len(self.pswrd)):
                if NewAccount.pswrd[i] in sch:
                    NewAccount.sc = 1
            if NewAccount.sc == 0:
                print("Password must contain special character.")
            if NewAccount.up == 1 and NewAccount.lc == 1 and NewAccount.num == 1 and NewAccount.sc == 1:
                #print("\nACCOUNT CREATED!")
                counter += 1
                
            counter2 = 0
            if counter == 1:
                while counter2 == 0:
                    NewAccount.pswrd_confirm = input("Confirm password - ")
                    if NewAccount.pswrd_confirm == NewAccount.pswrd:
                        counter2 += 1
                        print("\nACCOUNT CREATED!")
                    else:
                        print("\nPlease enter the same password as above -")
                
                
    def storeid(self):
        data_id = [self.email] 
        sid = open("loginsystem.txt","r+")
        for em in data_id:
            sid.read()
            sid.write('\n')
            sid.write(em)
            sid.truncate()
        sid.close()
        
    def storepw(self):
        data_pw = [NewAccount.pswrd]
        spw = open("loginsystem.txt","r+")
        for em in data_pw:
            spw.read()
            spw.write('\n')
            spw.write(em)
            spw.truncate()
        spw.close()
            
        
    
accountobj = AccountCheck()
accountobj.accountcheck() 

yes = input("\nDo you want to make a new account ?, Say(yes/no) - ")
if yes == "yes":
    
    email = str(input("\nEnter your Email-ID - "))
    
    newaccountobj = NewAccount(email)
    newaccountobj.BasicDetails()
    newaccountobj.check()
    newaccountobj.storeid()
    newaccountobj.storepw()
    login = input("\nDo you want to login into your account ?, Say(yes/no) - ")
    print()
    if login == "yes":
        accountobj.accountcheck()