import random
import time

def USER_CHOICE():

    print(" ******* If you have another list write y ******* ")
    UserDecision = input("  Enter yor choise >>>>>  ")
    print("\n")
    if UserDecision == "y":
        ASK()
    else:
        print("\n\n")
        print(" <><><><><><><> Thank you for using this program :) <><><><><><><> ")
        time.sleep(5)
        quit()

def ASK():
    print("Categories >>> \n 1- movies\n 2- music\n 3- game(punishment)\n 4- fantasy\n 5- series\n 6- Food(meals)\n 7- Color")
    try:
        Cate = int(input("Enter the category( **By number** ) , please >>  "))
    except:
        print(" &&&&&&&&&&&&& YOU MUST ENTER A NUMBER NOT LETTERS &&&&&&&&&&&&& \n")
        ASK()
    else:
        def MoviesCH():
            print("*************** Loading ***************\n")
            time.sleep(4)
            GroupOfCandidates = []
            try:
                NumberOfCndidates = int(input(" Enter Number of Movies  :      "))
            except:
                print(" @@@@@@@@@ YOU MUST ENTER NUMBER/s NOT LETTERS @@@@@@@@@\n ")
                MoviesCH()
            else:
                for i in range(0, NumberOfCndidates):
                     Candidate = input(" Enter the movie's name >>>     ")
                     GroupOfCandidates.append(Candidate)
                RandomChoice = random.choices(GroupOfCandidates)
                print(" Movies are --->> ",GroupOfCandidates)
                ResOfChoice = random.choice(GroupOfCandidates)
                print("----------- Processing -----------\n")
                time.sleep(5)
                print(" Our choice to you is ---->  ",ResOfChoice)
                print("\n")
                USER_CHOICE()
            return

        def SongCH():
            print("*************** Loading ***************\n")
            time.sleep(4)
            GroupOfCandidates = []
            try:
                NumberOfCndidates = int(input(" Enter Number of Music  :      "))
            except:
                print(" @@@@@@@@@ YOU MUST ENTER NUMBER/s NOT LETTERS @@@@@@@@@\n ")
                SongCH()
            else:
                for i in range(0, NumberOfCndidates):
                    Candidate = (input(" Enter the Music's name >>>     "))
                    GroupOfCandidates.append(Candidate)
                RandomChoice = random.choice(GroupOfCandidates)
                print(" Songs are --->> ",GroupOfCandidates)
                ResOfChoice = random.choice(GroupOfCandidates)
                print("----------- Processing -----------\n")
                time.sleep(5)
                print(" Our choice to you is ---->  ",ResOfChoice)
                print("\n")
                USER_CHOICE()
            return

        def PunishCH():
            print("*************** Loading ***************\n")
            time.sleep(4)
            GroupOfCandidates = []
            try:
                NumberOfCndidates = int(input(" Enter Number of Punish  :      "))
            except:
                print(" @@@@@@@@@ YOU MUST ENTER NUMBER/s NOT LETTERS @@@@@@@@@\n ")
                SeriesCH()
            else:
                for i in range(0, NumberOfCndidates):
                    Candidate = (input(" Enter the Punish's name >>>     "))
                    GroupOfCandidates.append(Candidate)
                RandomChoice = random.choice(GroupOfCandidates)
                print(" Punishments  are --->> ",GroupOfCandidates)
                ResOfChoice = random.choice(GroupOfCandidates)
                print("----------- Processing -----------\n")
                time.sleep(5)
                print(" Our choice to you is ---->  ",ResOfChoice)
                print("\n")
                USER_CHOICE()
            return

        def FantasyCaptinCH():
            print("*************** Loading ***************\n")
            time.sleep(4)
            GroupOfCandidates = []
            try:
                NumberOfCndidates = int(input(" Enter Number of Players  :      "))
            except:
                print(" @@@@@@@@@ YOU MUST ENTER NUMBER/s NOT LETTERS @@@@@@@@@\n ")
                SeriesCH()
            else:
                for i in range(0, NumberOfCndidates):
                    Candidate = (input(" Enter the player's name >>>     "))
                    GroupOfCandidates.append(Candidate)
                RandomChoice = random.choice(GroupOfCandidates)
                print(" Players are --->> ",GroupOfCandidates)
                ResOfChoice = random.choice(GroupOfCandidates)
                print("----------- Processing -----------\n")
                time.sleep(5)
                print(" Our choice to Captin this player  ---->  ",ResOfChoice)
                print("\n")
                USER_CHOICE()
            return

        def SeriesCH():
            print("*************** Loading ***************\n")
            time.sleep(4)
            GroupOfCandidates = []
            try:
                NumberOfCndidates = int(input(" Enter Number of Series  :      "))
            except:
                print(" @@@@@@@@@ YOU MUST ENTER NUMBER/s NOT LETTERS @@@@@@@@@\n ")
                SeriesCH()
            else:
                for i in range(0, NumberOfCndidates):
                    Candidate = (input(" Enter the Series name >>>     "))
                    GroupOfCandidates.append(Candidate)
                RandomChoice = random.choice(GroupOfCandidates)
                print(" series are --->> ",GroupOfCandidates)
                ResOfChoice = random.choice(GroupOfCandidates)
                print("----------- Processing -----------\n")
                time.sleep(5)
                print(" Our choice to you is  ---->  ",ResOfChoice)
                print("\n")
                USER_CHOICE()
            return

        def FoodCH():
            print("*************** Loading ***************\n")
            time.sleep(4)
            GroupOfCandidates = []
            try:
                NumberOfCndidates = int(input(" Enter Number of Meals  :      "))
            except:
                print(" @@@@@@@@@ YOU MUST ENTER NUMBER/s NOT LETTERS @@@@@@@@@\n ")
                SongCH()
            else:
                for i in range(0, NumberOfCndidates):
                    Candidate = (input(" Enter the meal's name >>>     "))
                    GroupOfCandidates.append(Candidate)
                RandomChoice = random.choice(GroupOfCandidates)
                print(" Meals are --->> ",GroupOfCandidates)
                ResOfChoice = random.choice(GroupOfCandidates)
                print("----------- Processing -----------\n")
                time.sleep(5)
                print(" Our choice to you is ---->  ",ResOfChoice)
                print("\n")
                USER_CHOICE()
            return

        def ColorCH():
            print("*************** Loading ***************\n")
            time.sleep(4)
            GroupOfCandidates = []
            try:
                NumberOfCndidates = int(input(" Enter Number of Colors  :      "))
            except:
                print(" @@@@@@@@@ YOU MUST ENTER NUMBER/s NOT LETTERS @@@@@@@@@\n ")
                SongCH()
            else:
                for i in range(0, NumberOfCndidates):
                    Candidate = (input(" Enter the color's name >>>     "))
                    GroupOfCandidates.append(Candidate)
                RandomChoice = random.choice(GroupOfCandidates)
                print(" Colors are --->> ",GroupOfCandidates)
                ResOfChoice = random.choice(GroupOfCandidates)
                print("----------- Processing -----------\n")
                time.sleep(5)
                print(" Our choice to you is ---->  ",ResOfChoice)
                print("\n")
                USER_CHOICE()
            return
        if Cate == 1:
            MoviesCH()
        elif Cate == 2:
            SongCH()
        elif Cate == 3:
            PunishCH()
        elif Cate == 4:
            FantasyCaptinCH()
        elif Cate == 5:
            SeriesCH()
        elif Cate == 6:
            FoodCH()
        elif Cate == 7:
            ColorCH()
        else:
            time.sleep(4)
            print(" @@@@@@@@@@@@ This Category not found @@@@@@@@@@@@ ")
            time.sleep(10)
    return
ASK()