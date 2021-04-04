import models
import sys
import settings
def play():
    breac_bool=True
    print("enter your name:",end="")
    name=input()
    print("hi",name)
    print("***********************************")
    while breac_bool:
        print("type start to start game or help to see all commands")
        command=input()
        if command=="exit":
            breac_bool=False
        elif command=="help":
            print(settings.comands)
        elif command=="scores":
            with open('scores.txt','r')as file:
                text=file.readlines()
            for i in text:
                print(i)
        if command=="start":
            break
    player=models.Player(name)
    enemy=models.Enemy(1)
    while breac_bool:
        player.attack(enemy)
        if player.protection(enemy)==False:
            breac_bool=False
if __name__=="__main__":
    play()
else:
    print("эта программа не может быть запущена из другой")
    sys.exit()
