# USER INTERFACE
# Author: Reuben George

import time # For pausing the program at intervals
import random # For the Random Number Generator
import datetime # To choose the initial greeting

def cls():
    print("\n"*65)

#this is the initial greeting. The greetings are chosen according to the time...
def greeting():
    cls()
    now=datetime.datetime.now()
    var=int(now.strftime("%H"))
    if(var<12):
        print("Good Morning Sir!")
    elif(var==12 or var==13 or var==14 or var==15 or var==16):
        print("Good afternoon sir!")
    elif(var>16):
        print("Good evening sir!")

def flow(var):
    i=0
    while(i<len(var)):
        print(var[i])
        time.sleep(0.15)
        i+=1

def virtual_fighter():
    
    from time import sleep as hold
    from random import randint as random_int


    def cls():
        print("\n"*100)
        
    def ques(ans):
        if(ans=='no' or ans=='nope' or ans=='nah' or ans=='n'):
            return 0
        elif(ans=='yes' or ans=='yep' or ans=='yeah' or ans=='y'):
            return 1
        else:
            return 2
        
    def status_bar(var):
        # This function displays a loading tab 
        cls()
        print(var,".")
        hold(1)
        cls()
        print(var,"..")
        hold(1)
        cls()
        print(var,"...")
        hold(1)
        cls()
        print(var,"....")
        hold(1)
        cls()
        hold(1)

    def game_logo():
        hold(3) 
        cls()
        print("                                                      xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","\n","                                                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","\n","                                                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","\n","                                                     xxxxxxx   xxxxx   xx          xx      xxx          xx  xxx  xxx      xxxx  xxxxxxxxxxxxxxx","\n","                                                     xxxxxxxx   xxx   xxxxxxx  xxxxxx  xxx  xxxxxx  xxxxxx  xxx  xx  xxxx  xxx  xxxxxxxxxxxxxxx","\n","                                                     xxxxxxxxx   x   xxxxxxxx  xxxxxx      xxxxxxx  xxxxxx  xxx  xx        xxx  xxxxxxxxxxxxxxx","\n","                                                     xxxxxxxxxx     xxxxxxxxx  xxxxxx  x  xxxxxxxx  xxxxxx  xxx  xx  xxxx  xxx  xxxxxxxxxxxxxxx","\n","                                                     xxxxxxxxxxx   xxxxxx          xx  xx  xxxxxxx  xxxxxxx     xxx  xxxx  xxx       xxxxxxxxxx","\n","                                                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","\n","                                                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","\n","                                                     xxxxxxx          xx          xxx        xx  xxxx  xx          xx         xx        xxxxxxx","\n","                                                     xxxxxxx  xxxxxxxxxxxxxx  xxxxxx  xxxxxxxxx  xxxx  xxxxxx  xxxxxx  xxxxxxxxx  xxxxx  xxxxxx","\n","                                                     xxxxxxx  xxxxxxxxxxxxxx  xxxxxx  xxxxxxxxx  xxxx  xxxxxx  xxxxxx  xxxxxxxxx  xxxxx  xxxxxx","\n","                                                     xxxxxxx       xxxxxxxxx  xxxxxx  xxxx   xx        xxxxxx  xxxxxx      xxxxx        xxxxxxx","\n","                                                     xxxxxxx  xxxxxxxxxxxxxx  xxxxxx  xxxxx  xx  xxxx  xxxxxx  xxxxxx  xxxxxxxxx  xx  xxxxxxxxx","\n","                                                     xxxxxxx  xxxxxxxxxxxxxx  xxxxxx  xxxxx  xx  xxxx  xxxxxx  xxxxxx  xxxxxxxxx  xxx  xxxxxxxx","\n","                                                     xxxxxxx  xxxxxxxxxx          xxx       xxx  xxxx  xxxxxx  xxxxxx         xx  xxxx  xxxxxxx","\n","                                                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","\n","                                                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","\n","                                                     xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n","\n")
        
    def health_display(health):
        print("|"*(int(health/10)), health)
                                                                     
    game_logo()
    hold(5)
    status_bar("loading")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    cls()
    hold(1)    
    cls()
    user=str(input("Enter username: "))
    cls()
    choice=input("What do you want to do:\n1.Play game\n2.View instructions\n3.view leaderboard\n")

    def random_opponent():
        num=random_int(1,5)
        if num==1:
            opponent=Iron_man
        elif num==2:
            opponent=Captain_America
        elif num==3:
            opponent=Hawkeye
        elif num==4:
            opponent=Thor
        elif num==5:
            opponent=Hulk
        return opponent

    def random_move():
        num=random_int(1,4)
        if num==1:
            action=slap
        elif num==2:
            action=punch
        elif num==3:
            action=kick
        elif num==4:
            action=flying_kick
        return action

    def input_move():
        try:
            num=input("Your move: ")
            if num=='slap':
                action=slap
            elif num=='punch':
                action=punch
            elif num=='kick':
                action=kick 
            elif num=='flying kick':
                action=flying_kick
            return action
        
        except UnboundLocalError:
            print("\nIllegal move. Try again\n")
            input_move()
            
    def random_chance():
        var=random_int(1,2)
        if var==1:
            return 1
        elif var==2:
            return 2

    def game():
        
        opponent=random_opponent()
        cls()
        hold(2)
        print("The audience cheers as {} enters the arena".format(user.name))
        hold(4)
        cls()
        print("{} waves at his fans as they cheer on".format(user.name))
        hold(3.5)
        cls()
        print("Suddenly the door on the other side bursts open. Who will be {}'s opponent?".format(user.name))
        hold(5)
        cls()
        print("It's none other than {}".format(opponent.name))
        hold(3)
        cls()

        def main():
            chance=random_chance()
            if chance==1:
                while(chance==1):
                    move=input_move()
                    cls()
                    if(move.num>0):
                        print(user.name,move.past,opponent.name,"\n")
                        opponent.health=(opponent.health)-(move.mag)
                        print(opponent.name,"'s health: ")
                        health_display(opponent.health)
                        print(user.name,"'s health: ")
                        health_display(user.health)
                        hold(3)
                                 
                        if opponent.health<=0:
                            cls()
                            print(user.name," defeated ",opponent.name)
                            hold(3)
                            var=input("Do you want to play again? : ")
                            ans=ques(var)
                            if ans==0:
                                cls()
                                x=str(input("\n\nDo you want to submit your score? : "))
                                ans=ques(x)
                                if ans==0:
                                    print("Thanks for playing Virtual Fighter")
                                    hold(250)
                                elif ans==1:
                                    try:
                                        file=open("game.leaderboard.txt",'a')
                                        file.write(user.name),file.write(" defeated "),file.write(opponent.name)
                                        file.close()
                                    except NameError:
                                        print("ERROR 458: A PROGRAM FILE HAS BEEN MOVED TO ANOTHER LOCATION")
                                    print("Thanks for playing Virtual Fighter")
                                    hold(250)
                                    break
                                elif ans==1:
                                    game()
                                elif ans==2:
                                    print("I take that as a yes")
                                    hold(2)
                                    game()
                                    
                        move.num=move.num-1 
                    else:
                        print("You can't use that move anymore")
                        hold(2.5)
                        cls()
                        main()
                    if(chance!=character):
                        break
                    
            elif chance==2:
                while(chance==2):
                    move=random_move()
                    cls()
                    print(opponent.name,move.past,user.name,"\n")
                    user.health=(user.health)-(move.mag)
                    print(opponent.name,"'s health: ")
                    health_display(opponent.health)
                    print(user.name,"'s health: ")
                    health_display(user.health)
                    hold(3)
                    
                    if user.health<=0:
                        cls()
                        print(opponent.name," defeated ",user.name)
                        hold(3)
                        var=input("Do you want to play again? : ")
                        ans=ques(var)
                        if ans==0:
                            cls()
                            x=str(input("\n\nDo you want to submit your score? : "))
                            ans=ques(x)
                            if ans==0:
                                print("Thanks for playing Virtual Fighter")
                                hold(250)

                            elif ans==1:
                                try:
                                    cls()
                                    file=open("game.leaderboard.txt",'a')
                                    file.write(user.name),file.write(" was defeated by "),file.write(opponent.name),file.write("\n")
                                    file.close()
                                    print("Your score has been submitted.\n\nThanks for playing Virtual Fighter")
                                    hold(250)
                                    break       
                                except NameError:
                                    print("ERROR 458: A PROGRAM FILE HAS BEEN MOVED TO ANOTHER LOCATION")                 
                        elif ans==1:
                             user.health=1000
                             game()
                        elif ans==2:
                            print("I take that as a yes")
                            hold(2)
                            user.health=1000
                            game()
                            
                    if(chance!=opponent):
                           break

        count=0
        while count<1000:
            if (count%5==0) and (count!=0):
                slap.mag=slap.mag *2
                punch.mag=punch.mag *2
                kick.mag=kick.mag *2
                flying_kick.mag=flying_kick.mag *2
                print("\n","POWER DOUBLED!!!","\n")
                hold(2)

            if count%5!=0:
                main()
            count+=1

    class character:

        def __init__(self,name,health,desc):
            self.name=name
            self.health=health
            self.desc=desc

    class opponent:

        def __init__(self,name,health,desc):
            self.name=name
            self.health=health
            self.desc=desc

    class verb:

        def __init__(self,name,mag,past,num):
            self.name=name
            self.mag=mag
            self.past=past
            self.num=num
            
    slap=verb("slap",5," slapped ",1500)
    punch=verb("punch",10," punched ",18)
    kick=verb("kick",20," kicked ",12)
    flying_kick=verb("flying kick",50," flying kicked ",6)
            
    user=character(user,1000,"")

    Iron_man=opponent("Iron man ",1000,"Has a suit of armour")
    Captain_America=opponent("Captain America ",1000,"Has a Vibranium shield")
    Hawkeye=opponent("Hawkeye ",700,"Fires arrows")
    Thor=opponent("Thor ",1000,"Has Mjolnir the hammer")
    Hulk=opponent("The Hulk ",2500,"Deadly when angry")

    if(choice=='2' or choice=="View instructions"):
        try:
            cls()
            guide=open("game_guide.txt")
            cont=guide.read()
            print(cont)
            hold(3)
            guide.close()
            x=str(input("\nHit Enter to play the game"))
            if x=="" or x==" ":
                cls()
                game()
        except NameError:
            print("ERROR 458: A PROGRAM FILE HAS BEEN MOVED TO ANOTHER LOCATION")

    elif(choice=='3' or choice=="View leaderboard"):
        cls()
        log=open("game.leaderboard.txt")
        cont=log.read()
        print(cont)
        log.close()
        if cont==None or cont=="" or cont==" ":
            print("There are no entries in the leaderboard yet")
        hold(3)
        x=str(input("\nHit Enter to play the game"))
        if x=="" or x==" ":
            cls()
            game()

    elif(choice=='1' or choice=="Play game"):
        game()
        
def status_bar(var):
    # This function displays a loading tab 
    cls()
    print(var,".")
    time.sleep(1)
    cls()
    print(var,"..")
    time.sleep(1)
    cls()
    print(var,"...")
    time.sleep(1)
    cls()
    print(var,"....")
    time.sleep(1)
    cls()
    time.sleep(1)

def count_char(char,text):
    count=0
    for c in text:
        if(c==char):
            count+=1
    return count

def ques(ans):
    if(ans=='no' or ans=='nope' or ans=='nah' or ans=='n'):
        return 0
    elif(ans=='yes' or ans=='yep' or ans=='yeah' or ans=='y'):
        return 1
    else:
        return 2

def calculator():
    
    def add(a,b):
        return(a+b)
    def sub(a,b):
        return(a-b)
    def mul(a,b):
        return(a*b)
    def div(a,b):
        return(a/b)
    def factorial(a):
        if a==1:
            print("The factorial of 1 is: 1")
        else:
            return a*factorial(a-1)
    def menu():
        
        choice=(input("What do you want to do?: "))

        # the use of the math module would make the code shorter as defining the operations would not be required....
        # but the developer of this code is currently too stupid to know how to use the math module....
        
        if choice=='1':
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
            print("The sum of ",a,"and",b,"is: ",add(a,b))

        elif choice=='2':
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
            print("The difference between ",a,"and",b,"is: ",sub(a,b))

        elif choice=='3':
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
            print("The product of ",a,"and",b,"is: ",mul(a,b))

        elif choice=='4':
            a=float(input("Enter the first number: "))
            b=float(input("Enter the second number: "))
            print("The quotient of ",a,"and",b,"is: ",div(a,b))
            
        elif choice=='5':
            var=int(input("Enter the number: "))
            num=factorial(var)
            print(var)
            
        elif choice=='6':
            c=str(input("Are you sure you want to quit Reuben's Calculator?"))
            if c=='Yes' or c=='yes' or c=='yeah' or c=='yep' or c=='oh yeah' or c=='definitely' or c=='yes please' or c=='y':
                print("Thank you for using Reuben's Calculator")
            elif c=='no' or c=='No' or c=='Nope' or c=='nope' or c=='nah' or c=='nada' or c=='n':
                print("")
                return menu()

        else:
            print("ERROR CODE 605: INVALID INPUT")

    print("Welcome to Reuben's Calculator")

    print("")
    print("Your options are:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Factorial")
    print("6.Quit")
    print("")

    menu()

def random_num_gen():
    from random import randint
    cls()
    min_value=int(input("Enter minimum value: "))
    max_value=int(input("Enter maximum value: "))
    random_number=random.randint(min_value,max_value)
    print(random_number)
    
def main():
    
    status_bar("Loading")
    greeting()

    time.sleep(2)
    cls()
    print("I am Droid, at your service")
 
    time.sleep(3)
    cls()
    print("Before I can help you, I will need to verify your identity")
    time.sleep(3)
    
    def user():
        time.sleep(3)
        cls()
        var=str(input("Do you have an account?: "))
        var=ques(var)
        cls() 

        """ The signup block takes a username, verifies its availability, takes a password,
        confirms the password, appends them to a file containing user info and stores
        the username and password in variables for future use...."""

        # The signup block
        if(var==0):
            choice=str(input("Do you want to sign up?: "))
            choice=ques(choice)
            if(choice==1):
                cls()
                username=str(input("Enter username: "))
                user_info=open('user_info.txt')
                cont=user_info.read()
                if username in cont:    
                    while(username in cont):
                        print("Sorry, the username is not available. Please try again with another username")
                        time.sleep(3)
                        cls()
                        username=str(input("Enter username: "))
                        if not username in cont:
                            break
                
                password=str(input("Enter access code: "))
                confirm_password=str(input("Confirm access code: "))
                cls()
                if(password==confirm_password):
                    print("Thank you for signing up")
                    time.sleep(2)
                elif(password!=confirm_password):
                    while(password!=confirm_password):
                        print("ERROR_CODE_223: PASSWORDS DO NOT MATCH")
                        time.sleep(3)
                        cls()
                        password=str(input("Enter access code: "))
                        confirm_password=str(input("Confirm access code: "))
                user_info.close()
                user_info=open('user_info.txt','a')
                user_info.write(username),user_info.write(' : '),user_info.write(password),user_info.write('\n')
                user_info.close()
            
                
        # The login block      
        elif(var==1):
            cls()
            username=str(input("Enter username: "))
            user_info=open('user_info.txt')
            cont=user_info.read()
            if(not username in cont or username=="" or username==" " or username=="  " or username=="   "):
                while(not username in cont or username=="" or username==" " or username=="  "):
                    cls()
                    print("Sorry, I don't know you. Please check and enter your username again")
                    time.sleep(3)
                    cls()
                    username=str(input("Enter username: "))
                    if username in cont:
                        break
            password=str(input("Enter access code: "))
            if(not password in cont or password=="" or password==" " or password=="  " or password=="   "):
                i=0
                while(not password in cont or password=="" or password==" " or password=="  " or password=="   "):
                    cls()
                    print("Incorrect password. Please try again")
                    time.sleep(2)
                    cls()
                    password=str(input("Enter your access code: "))
                    i+=1
                    if(i==5):
                        cls()
                        print("You have entered the wrong password 5 times. Try again after 10 seconds")
                        time.sleep(10)
                        cls()
                        password=str(input("Enter your access code: "))
                    if(password in cont):
                        break

        elif(var==2 or var==None):
            print("It's a yes or no question")
            time.sleep(2)
            user()
            
        cls()
        print("ACCESS GRANTED.....")
        time.sleep(2)

        # The timepass block
        i=0
        while(i<250):
            a=1100101011101000100110101001001001010010101101001100010001010101001010101010110010101010101010110110010100101010011010101010101010010101010100101000101010010101000101010010100101001010101010011001
            print(a)
            i+=1

        # The Welcome block
        cls()
        time.sleep(1)
        print("Welcome"),time.sleep(1),cls(),print(username),time.sleep(2),cls(),print("to"),time.sleep(1),cls(),print("the"),time.sleep(1),cls()
        flow('Augmented user interface')
        time.sleep(3),cls()
        print("I am going to be your guide")
        time.sleep(2)
        cls()

        # The interface defining block

        def interface():
            var=str(input("What would you like to do?: \n\n1.View guide\n2.Know about us\n3.View a document\n4.View a document with text analyzer\n5.Write a new document\n6.See the date and time\n7.Use the calculator\n8.Chat with others\n9.Random Number Generator\n10.Play Virtual Fighter\n11.Leave feedback\n12.Logout\n\n>>> ")) 
        
            if(var=='View guide' or var=='1'):
                guide=open('guide.txt')
                cls()
                print(guide.read())
                guide.close()
            
            elif(var=='Know about us' or var=='2'):
                about_us=open('about_us.txt')
                print(about_us.read())
        
            elif(var=='View a document' or var=='3'):
                src=input("Enter the exact path of the file: ")
                cls()
                try:
                    file=open(src)
                    print(file.read())
                    file.close()
                except FileNotFoundError:
                    print("ERROR 124: FILE NOT FOUND. PLEASE TRY AGAIN")
            
            elif(var=='View a document with text analyzer' or var=='4'):
                cls()
                src=input("Enter the exact path of the file: ")
                try:
                    file=open(src)
                    cont=file.read()
                    print(cont),("\n\n")
                    c=input("Which letter do you want to check?: ")
                    x=count_char(c,cont)
                    perc=(x*100)/len(cont)
                    print(x," i.e ",perc,"% of  the total characters in the file")
                except FileNotFoundError:
                    print("ERROR_CODE_124: FILE NOT FOUND. PLEASE TRY AGAIN")

            elif(var=='Write a new document' or var=='5'):
                file=open('new_document.txt','w')
                content=input("Write: ")
                file.write(content)
                file.close
                cls()
                print("The content has been written and saved as a .txt file as: 'new_document.txt'")
                time.sleep(4)
                cls()

            elif(var=='See the date and time' or var=='6'):
                cls()
                now=datetime.datetime.now()
                print("Current date and time: ")
                print(now.strftime("%y-%m-%d %H:%M"))

            elif(var=='Use the calculator' or var=='7'):
                cls()
                calculator()

            elif(var=='Chat with others' or var=='8'):
                i=0
                while(i<6):
                    cls()
                    print("CONNECTING.")
                    time.sleep(1)
                    cls()
                    print("CONNECTING..")
                    time.sleep(1)
                    cls()
                    print("CONNECTING...")
                    time.sleep(1)
                    i+=1
                cls()    
                print("ERROR CODE 178: https://www.github.com/users/reuben02/scripts TOOK TOO LONG TO RESPOND. PLEASE CHECK YOUR NETWORK CONNECTION AND TRY AGAIN")
                time.sleep(6)
                cls()

            elif(var=='Random Number Generator' or var=='9'):
                try:
                    random_num_gen()
                except ValueError:
                    print("Do you understand what is meant by 'MINIMUM' and 'MAXIMUM'???")
                    time.sleep(4.25)
                    random_num_gen()

            elif(var=='Play Virtual Fighter' or var=='10'):
                virtual_fighter()

            elif(var=='Leave feedback' or var=='11'):
                fback=input("Was this code helpful?: ")
                if('no' in fback or 'bad' in fback or 'long' in fback or 'messy' in fback):
                    cls()
                    print("Thanks a lot. I will try to improve your experience the next time")
                elif('yes' in fback or 'great' in fback or 'nice' in fback):
                    cls()
                    print("Thanks a lot. Your feedback means a lot to me")
                else:
                    print("I have no idea what that means, but thanks anyway")

            elif(var=='Logout' or var=='12'):
                cls()
                print("Glad I could help you",username)
                time.sleep(3)
                cls()
                return user()
                
        # The interface runner line    
        interface()

        # The interface repeater block
        var=str(input("Do you want to do anything else?"))
        var=ques(var)
        cls()

        if(var==0):
            cls()
            print("Glad I could help you",username)
        if(var==1):
            while(var==1):
                cls
                interface()
    user()
        
main()  
            
    
    
