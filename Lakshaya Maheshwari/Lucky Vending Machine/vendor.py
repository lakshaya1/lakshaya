import random
from random import randint
import os
import os.path

flag1=True
flag2=True
flag3=True
flag4=True
flag5=True
flag6=True
class player:
    player_name = "Bot"
    player_nprizes =2
    player_money = 100.0
    player_prize="book,pen"
    def set_player_details(self,name, nprizes, money,prize):

        self.player_name = name
        self.player_nprizes = nprizes
        self.player_money = money
        self.player_prize=prize
        fw = open(self.player_name, 'w')
        fw.write(self.player_name+" "+str(self.player_nprizes)+" "+str(self.player_money)+"\n")
        fw.write(self.player_prize)
        fw.close()
    def get_player_details(self):

        print("Player Name:"+self.player_name)
        print("Player No of Prizes:"+str(self.player_nprizes))
        print("Player Money:"+str(self.player_money))
        print("Player Prize Won:"+str(self.player_prize))

    def send_player_money(self):
        return self.player_money
    def send_player_name(self):
        return self.player_name
    def send_player_nprizes(self):
        return self.player_nprizes
    def send_player_prize(self):
        return self.player_prize




class lucky_number_generator(player):

    def generate_number(self):
        lucky_number = randint(1, 5)
        return lucky_number

class Game(player, lucky_number_generator):


    def gamy(self):
        while self.flag4:
         try:
           self.amount=raw_input("Enter The Amount For Which You Wanna Play in Range{1-5]:")
           self.flag4=False
         except:
           print("Enter a valid Amount")
           continue
         if self.amount > self.player_money:
           print("You Don't Have That Much Money")
         else:
           self.player_money=self.player_money-self.amount









playerobj = lucky_number_generator()


while True:
                frs = open('start', 'r')
                start = frs.read()
                print start
                frs.close()

                flag1=True
                flag2=True
                flag3=True
                flag4=True
                flag5=True

                try:
                    choice = int(input("Select an option : "))
                    flag6=False
                except:
                    print("Enter A Valid Choice")
                    continue

                if choice == 1:
                    print("Enter Player details")
                    while flag1:
                        player_name = raw_input("Enter player name :" )
                        if player_name=="":
                             print("Enter a valid name")
                        else:
                            flag1=False


                    PATH='./'+player_name

                    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
                        print "Welcome Back "+player_name+"..."
                        with open(player_name, 'r') as myfile:
                            data=myfile.readline()
                            data1=myfile.readline()

                        list=data.split(" ")

                        player_nprizes=int(list[1])
                        player_money=float(list[2])
                        player_prize=data1



                    else:
                        print "Hello "+player_name+"..."
                        player_prize=""
                        while flag2:
                          try:
                            player_nprizes = int(raw_input("Enter No. of Prizes : "))
                            flag2=False
                          except:
                            print("Enter a valid No. of Prizes")
                            continue
                        while flag3:
                          try:
                            player_money = float(raw_input("Enter Total money player has : "))
                            flag3=False
                          except:
                            print("Enter a valid Amount")
                            continue




                    playerobj.set_player_details(player_name, player_nprizes, player_money,player_prize)






                elif choice == 2:
                    guess=0
                    amount=0
                   # objgame.gamy()
                    pl=playerobj.send_player_money()
                    pz=playerobj.send_player_nprizes()
                    pn=playerobj.send_player_name()
                    p=playerobj.send_player_prize()
                    print ("You have: "+str(pl)+"Rs")
                    if (pl>0):
                        while flag4:
                            try:
                                amount=float(raw_input("Enter The Amount For Which You Wanna Play in Range[1-5]:"))
                                if amount > pl:

                                    print("You Don't Have That Much Money")
                                    continue
                                elif amount >5:
                                    print("Please Enter amount in range 1 to 5")
                                    continue

                                else:
                                    pl=pl-amount
                                    print pl

                                    playerobj.set_player_details(pn,pz,pl,p)
                                    flag4=False

                            except:
                                print("Enter a valid Amount")
                                continue




                        while flag5:
                            try:
                                guess=int(raw_input("Guess A Number in range [1-5] :"))
                                flag5=False
                            except:
                                print("Enter a valid Guess")
                                continue
                        lucky=playerobj.generate_number()
                        print "Lucky Number Was:"+str(lucky)

                        if guess==lucky:

                            if amount==1:
                                print("Congratulation You Won The Pen")
                                pl=pl+10
                                pz=pz+1
                                p= p + ' pen'
                            elif amount==2:
                                print("Congratulation You Won The Book")
                                pl=pl+20
                                pz=pz+1
                                p= p + ' book'
                            elif amount==3:
                                print("Congratulation You Won The DVD")
                                pl=pl+30
                                pz=pz+1
                                p= p + ' DVD'
                            elif amount==4:
                                print("Congratulation You Won The Mouse")
                                pl=pl+40
                                pz=pz+1
                                p= p + ' mouse'
                            elif amount==5:
                                print("Congratulation You Won The Keyboard")
                                pl=pl+50
                                pz=pz+1
                                p= p + ' keyboard'
                        else:
                            print("You Lost This Game Try Again..")
                        playerobj.set_player_details(pn,pz,pl,p)

                    else:
                        print("No balance")
                elif choice == 3:

                    playerobj.get_player_details()




                elif choice == 4:
                    print("Help center")
                    print("Price List: ")
                    fr = open('Game_help.txt', 'r')
                    text = fr.read()
                    print(text)
                    fr.close()
                    print("Game Rules: ")
                    print("1. Admin will set up a new player by setting his name, money, prizes, etc.")
                    print("2. Is the player exists he will get is previous data from the file otherwise a new player would be created.")
                    print("3. The player will than select the amount for which he/she wants to play.")
                    print("4. The player than has to guess a number and if the guess is correct, "
                          "he/she will a prize worth 10 times the amount he played for.")
                    print("5. If the guess is wrong player will loose that much amount.")
                elif choice == 5:

                        exit(0)


                else:
                    print("Enter a Valid Choice")
                    continue


