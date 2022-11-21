class Nom:
    nom_list = []
    ivotes = []
    def __init__(self,no_nominee):
        self.no_nominee = no_nominee
    
    def nomverify(self):
        k=0
        for i in range(1,no_nominee+1):
            print("Name of",i,"nominee - ",end='')
            n = input()
            Nom.nom_list.append(n)
            Nom.ivotes.append(k)
           
           
    def nomdisplay(self):
        print("\n---------------------------------")
        print("List of nominees for election ")
        for i in Nom.nom_list:
            print(i)
        print("\n---------------------------------")
            
class Voter:
    vot_list = []
    def __init__(self,no_voter):
        self.no_voter = no_voter
        
    def voterverify(self):
        for n in range(1,no_voter+1):
            print("Voter-Id of",n,"voter - ",end='')
            n =  input()
            if n not in Voter.vot_list:
                Voter.vot_list.append(n)
            else:
                print("Voter already in the voter list")
    
    def voterdisplay(self):
        print("\n------------------------------------")
        print("List of Voter-id's ")
        for i in Voter.vot_list:
            print(i)
        print("\n------------------------------------")
            
class Votingsystem(Nom,Voter):
    def __init__(self):
        pass
    
    def vote(self):
        while Voter.vot_list != []:
            print("Enter your Voter-Id - ",end='')
            self.id = input()
            if self.id in Voter.vot_list:
                print("You are a Voter, you can Vote.")
                for i in range(1,len(Nom.nom_list)+1):
                    print("Press",i,"for",Nom.nom_list[i-1])
                print("\n----------------------------------")
                vote = int(input("Enter your valuable vote - "))
                if vote<=len(Nom.nom_list):
                    Voter.vot_list.remove(self.id)
                    Nom.ivotes[vote-1] += 1
                    print(Nom.nom_list[vote-1],"Thank you for giving me your precious vote\n")
                elif vote>len(Nom.nom_list):
                    print("\nCheck your pressed key")
                    print("You have one more chance only - ")
                    for i in range(1,len(Nom.nom_list)+1):
                        print("Press",i,"for",Nom.nom_list[i-1])
                    print("\n----------------------------------")
                    vote1 = int(input("Enter your valuable vote - "))
                    if vote1<=len(Nom.nom_list):
                        Voter.vot_list.remove(self.id)
                        Nom.ivotes[vote1-1] += 1
                        print(Nom.nom_list[vote1-1],"Thank you for giving me your precious vote")
                    else:
                        Voter.vot_list.remove(self.id)
                        print("You entered wrong key again. Vote Wasted!!!")
                else:
                    print("You are not a voter OR you have already voted ")
                print("\n")  
                #print(Nom.ivotes)
                print("Voters remaining to vote",Voter.vot_list)
            else:
                print("\nYour Voter-id is not listed in voter list, You can't vote!!! OR you have already voted!!!\n")  
                
    def result(self):
        print("Voting Session is over -")
        maxvotes1 = max(Nom.ivotes)
        index = 0
        maxvotes = Nom.ivotes.index(max(Nom.ivotes))
        print(Nom.nom_list[maxvotes],"Wins the elections")        
            
no_nominee = int(input("How many nominees are there for election - "))
nomobj = Nom(no_nominee)
nomobj.nomverify()
nomobj.nomdisplay()

no_voter = int(input("How many voters are there for election - "))
voterobj = Voter(no_voter)
voterobj.voterverify()
voterobj.voterdisplay()

vsobj = Votingsystem()
vsobj.vote()
vsobj.result()