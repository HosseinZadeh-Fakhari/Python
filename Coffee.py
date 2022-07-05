
from random import randint as R
import time

class Amir_Hossein_Hossein_Zadeh_Fakhari_Coffee_Shop :
    Menu={'1- Mocha': 4.25 ,'2- Caramel Latte':4.25 ,'3- Espresso': 3 ,'4- Earl Grey': 3.25 ,'5- Green Tea': 3.25 ,'6- Orange juice': 3.5 ,'7- Croissant':4.45 ,'8- Muffin': 3.6 } 
    ShomareSefaresh=[]
    GheimatSefaresh=[]
    TedadeSefaresh=[]
    GheimateKol =[]
    Q=1

    def __init__(self,Name,Familyname):
        self.X=Name
        self.Y=Familyname

    def place_order(self):
       

        self.majmoeeGheimat = 0

        
        while True : 
            time.sleep(3)
            for ii in self.Menu:{
              print(ii)}
            time.sleep(5)
            print('\nLotfan ghazayeh khod ra entekhab konid.\n')
            S=input('Vaghti ke sefareshetan tamam shod benevisid : "yes"\n')

            if S.lower() =='yes':
                print('Mamnon . Az asre khod lezat bebarid !')
                break
            else: 
                try:
                    if (int(S)>0 and int(S)<9) :
                        s=int(S)

                    if s == 1 :
                        self.ShomareSefaresh.append('Mocha')
                        self.GheimatSefaresh.append(4.25)
                    
                    elif s == 2 :
                        self.ShomareSefaresh.append('Caramel Latte')
                        self.GheimatSefaresh.append(4.25)
                    
                    elif s == 3 :
                        self.ShomareSefaresh.append('Espresso')
                        self.GheimatSefaresh.append(3)
                    
                    elif s == 4 :
                        self.ShomareSefaresh.append('Earl Grey')
                        self.GheimatSefaresh.append(3.25) 
                    
                    elif s == 5 :
                        self.ShomareSefaresh.append('Green Tea')
                        self.GheimatSefaresh.append(3.25)
                   
                    elif s == 6 :
                        self.ShomareSefaresh.append('Orange juice')
                        self.GheimatSefaresh.append(3.5)
                    
                    elif s == 7 :
                        self.ShomareSefaresh.append('Croissant')
                        self.GheimatSefaresh.append(4.45)

                    elif s == 8 :
                        self.ShomareSefaresh.append('Muffin')
                        self.GheimatSefaresh.append(3.6)
                    T=input('Chand ta? : ' )
                    try :
                        self.TedadeSefaresh.append(int(T))  
                    except : 
                        print('Yek chizi eshtebeh shode !')
                except : 
                    print ('Dar menu nist !')
            print("Chizi digar mikhahid ?")

        for ee in range(len(self.TedadeSefaresh )) :
            self.GheimateKol.append(self.GheimatSefaresh[ee] * self.TedadeSefaresh[ee])

        for v in range(len(self.GheimateKol)) :
            self.majmoeeGheimat= self.GheimateKol[v] + self.majmoeeGheimat


    def GuessingGame(self): 
        
        self.majmoeeGheimatBaTakhfif = self.majmoeeGheimat
        time.sleep(1.5)
        print('\U0001F3B0	')
        time.sleep(1.5)


        print('Lotfan jabeyeh khod ra entekhab konid sepas adade kenare on ra vared konid.')
        N=1
        for i in range(1,11):  
            for j in range(1,11): 
                if j != 10 and i == 1:
                    print(f' {N}- ({i},{j})',end='    ')
                elif j != 10 and i != 10:
                    print(f'{N}- ({i},{j})',end='    ')
                elif i == 10 and j==9:
                    print(f'{N}- ({i},{j})',end='  ')
                elif i == 10:
                    print(f'{N}- ({i},{j})',end='   ')
                else:    
                    print(f'{N}- ({i},{j})')
                N+=1
  
        K=R(1,100)
        print('\nAgar nemitavanid edame bedahid lotfan benevisid "end game" .')
        for r in range(100):
            J=input()
            try :
                J=int(J)
                print('Komak => ',end='')

                if J==K:  
                    print('Movafagh shdid !! ','  \U0001F389' ,'  \U0001F386','  \U0001F387')
                    time.sleep(5)
                    break

                elif (K > J) : 

                    if (K // 10 == J // 10) and (K % 10 > J % 10) :
                        if J % 10 == 0 :
                            print ('LEFT DOWN')
                        else :
                            print('RIGHT')

                    elif (K % 10 > J % 10) and (J % 10 > 0) :
                        print('RIGHT DOWN')

                    elif (K % 10 < J % 10) and (K % 10 > 0) :
                        print('LEFT DOWN')

                    elif (K % 10 == J % 10) : 
                        print('DOWN')

                    elif (K % 10 > J % 10) and (J % 10 == 0) and (K//10 > J//10) :
                        print('LEFT DOWN') 
                        
                    elif (K % 10 < J % 10) and (K % 10 == 0) and (K//10 > J//10) :
                        if ((J//10)+1 == K//10) :
                            print('RIGHT')
                        else:
                            print('RIGHT DOWN')

                    elif (K//10 == (J//10)-1) :
                        print('RIGHT')

                elif (K < J) :

                    if (K // 10 == J // 10) and (K % 10 < J % 10) :
                        if K%10 ==0:
                            print('RTGHT UP')
                        else : print('LEFT')

                    elif (K % 10 > J % 10) and (J % 10 > 0) :
                        print('RIGHT UP')

                    elif (K % 10 < J % 10) and (K % 10 > 0) :
                        print('LEFT UP')

                    elif (K % 10 == J % 10) :
                        print('UP')

                    elif (K % 10 > J % 10) and (J % 10 == 0) and (J//10 > K//10) :
                        if (J//10 == (K//10)+1) :
                            print('LEFT')
                        else: 
                            print('LEFT UP')
                
                    elif (K % 10 < J % 10) and (K % 10 == 0) and (J//10 > K//10) :
                        print('RIGHT UP')

                    elif (J//10 == (K//10)-1) :
                        print('LEFT')

                r+=1
                self.Q+=1
                # print('Computer choose = > ',K)
                print ('Edame midahid ? "yes" ya "no" \nAgar yes adadi digar benevisid , Agar no benevisid "end game".')
            except : 
                self.Q = 0
                self.majmoeeGheimatBaTakhfif = 0
                print('Mamnon hastim az idk ki dar in bazi sherekat kardid.')
                break
        
        if self.Q==1:
            print('100% takhfif bordid !')
            self.majmoeeGheimatBaTakhfif =- self.majmoeeGheimatBaTakhfif

        elif self.Q>=2   and   self.Q<=4:
            print('50% takhfif bordid !')
            self.majmoeeGheimatBaTakhfif =- (self.majmoeeGheimatBaTakhfif)/2

        elif self.Q==6   or   self.Q==5:
            print('10% takhfif bordid !')
            self.majmoeeGheimatBaTakhfif =- (self.majmoeeGheimatBaTakhfif)/10

        elif self.Q>6 : 
            print('10% ',end='bishtar bayad pol bedahid !')
            self.majmoeeGheimatBaTakhfif =+ (self.majmoeeGheimatBaTakhfif)/10

    def request_bill (self):
        print('\n','------------------------------------------------------------')

        print('\nNam : ',self.X)
        print('Name fhanevadegi  : ',self.Y)
        print('List sefaresh shoma be hamrahe gheimate : ','\U0001F9FE','\n')
        print('Name ghaza   Gheimat   Tedad   Gheimat kol')
        for w in (range(len(self.ShomareSefaresh))) :
            print(f'{w+1}- {self.ShomareSefaresh[w]} : {self.GheimatSefaresh[w]}  ,  {self.TedadeSefaresh[w]}  =>  {self.GheimateKol[w]}')
        print('------------------------------------------------------------')
        
        print('\nMajmoee gheimat => ' , self.majmoeeGheimat )
        print('Takhfife gerefte shode az bazi : ', self.majmoeeGheimatBaTakhfif )
        print('Majmoee gheimat baad az takhfif => ',self.majmoeeGheimat + self.majmoeeGheimatBaTakhfif)
        print('\nMamnon hastim az in ke cafe ma ra entekhab kardid',' \U0001F64F','\n')







def Karbar (X,Y):
    sd = Amir_Hossein_Hossein_Zadeh_Fakhari_Coffee_Shop(X , Y )

    sd.place_order()
    uo=input ('Bazie hads adad sherekat mikonid?\nAgar bishtar az 6 bar javab bedahid  bayad 10 darsad bishtar pol bedahid \nAgar "no" benevisid "no" : ')
    sd.majmoeeGheimatBaTakhfif=0
    uo.lower()
    if uo !='no':
        sd.GuessingGame()
    sd.request_bill()
Karbar(input('Lotfan name khod ra vared konid : '),input('\nlotfan name khanevadegi khod ra vared konid : '))

