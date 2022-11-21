class Password:
    up = 0
    lc = 0
    num = 0
    sc = 0
    def __init__(self,pswrd):
        self.pswrd = pswrd
        
    def check(self):
        sch = {"!",'"',"#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","}","/","~"}
        try:
            assert len(self.pswrd) >= 8
        except AssertionError :
            raise Exception("There's at least 8 characters in your password. Press ctrl+f11 to enter again")
        try:
            for i in range(len(self.pswrd)):
                if self.pswrd[i].isupper():
                    Password.up = 1 
            assert Password.up == 1
        except AssertionError:
            raise Exception("Password must contain upper case character. Press ctrl+f11 to enter again")
        
        try:
            for i in range(len(self.pswrd)):
                if self.pswrd[i].islower():
                    Password.lc = 1 
            assert Password.lc == 1
        except AssertionError:
            raise Exception("Password must contain lower case character. Press ctrl+f11 to enter again")
        try:
            for i in range(len(self.pswrd)):
                if self.pswrd[i].isnumeric():
                    Password.num= 1 
            assert Password.num == 1
        except AssertionError:
            raise Exception("Password must contain numeric character. Press ctrl+f11 to enter again")
        
        try:
            for i in range(len(self.pswrd)):
                if self.pswrd[i] in sch:
                    Password.sc = 1
            assert Password.sc == 1
        except AssertionError:
            raise Exception("Password must contain special character. Press ctrl+f11 to enter again")
        else:
            print("YOUR PASSWORD IS VALID \nPASSWORD SAVED")
        
        #if Password.up == 0 and Password.lc == 0 and Password.num == 0 and Password.sc == 0:
        #    print("YOUR PASSWORD IS VALID \nPASSWORD SAVED")

pss = input("Enter your password. Password must contain a number, \
special character, upper and lower case letter :- ")
obj = Password(pss)
obj.check()