def print_board(lis):
    for i in range(0,3):
        for j in range(0,3):
            if (str(lis[i*3+j])).isnumeric() == False:
                print(lis[i*3+j], end=" ")
            else:
                print("-",end=" ")
        print('')
        
def getAndSetInput(lis,turn):
    pos = True
    while(pos== True):
        i = input("Enter position for {ch}: ".format(ch=turn))
        if str(lis[int(i)-1]).isnumeric()==True:
            lis[int(i)-1]=turn
            pos= False
        else:
            print("This position is already taken, please try again")
        print_board(lis)
        
def checkForWin(lis=[]):
    if(lis[0]==lis[1]==lis[2]) or (lis[3]==lis[4]==lis[5]) or (lis[6]==lis[7]==lis[8]) or (lis[0]==lis[4]==lis[8]) or (lis[2]==lis[4]==lis[6]) or (lis[0]==lis[3]==lis[6]) or (lis[1]==lis[4]==lis[7]) or (lis[2]==lis[5]==lis[8]):
        return True
    return False

alive = True
turn =True
ch = 'X'
lis =[1,2,3,4,5,6,7,8,9]
while(alive == True):
    if(turn==True):
        ch = 'X'
        turn = False
    else:
        ch = 'O'
        turn =True
    getAndSetInput(lis,ch)
    win = checkForWin(lis)
    if(win==True):
        alive =False
        print("Player {ch} won, Ending Game!!".format(ch=ch))
    else:
        a = input("want to play more? Enter 1, if Yes ")
        if int(a)==1:
            alive = True
        else: 
            alive = False
        if alive ==False:
            a = input("want to Start a new Game? Enter 1, if Yes ")
            if int(a)==1:
                alive = True
                turn =True
                ch = 'X'
                lis =[1,2,3,4,5,6,7,8,9]
            else:
                print("Ending Game... ended!")

checkForWin()