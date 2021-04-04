from random import randint
import exceptions
import settings
class Enemy:
    def __init__(self,level):
        self.lives=level
        self.level=level
    def select_attack(self):
        return randint(1,3)
    def reduce_decrais(self):
        self.lives-=1
        try:
            if self.lives==0:
                raise exceptions.EnemyDown()
        except exceptions.EnemyDown:
            self.level+=1
            self.lives=self.level
            return 1
        else:
            return 0
class Player:
    score=0
    lives=settings.lives
    atacs=[1,2,3]
    def __init__(self,name):
        self.name=name
    def static_battle(self,attack,protection):
        if attack==protection:
            return 0
        elif attack==1 and protection==3:
            return -1
        elif attack==1 and protection==2:
            return 1
        elif attack==2 and protection==1:
            return -1
        elif attack==2 and protection==3:
            return 1
        elif attack==3 and protection==2:
            return -1
        elif attack==3 and protection==1:
            return 1
    def reduce_lives(self):
        self.lives-=1
        try:
            if self.lives<1:
                raise exceptions.GameOver(self.score,self.name)
        except exceptions.GameOver as err:
            err.writer()
            print('Game Over!You score is ',self.score)
            print('good bye')
            return False
    def attack(self,enemy_obg):
        breac_bool=True
        while breac_bool:
            breac_bool=False
            try:
                print("Select attack to Use:1-WISARD,2-WARRIOR,3-ROGUE",end=":")
                attack=int(input())
                if attack<0 or attack>3:
                    print("incorect input")
                    breac_bool=True
            except ValueError:
                print("incorect input")
                breac_bool=True
        protection=enemy_obg.select_attack()
        result=self.static_battle(attack,protection)
        if result==0:
            print("it`s a draw!")
            print("Your lives:",self.lives,"|Enemy lives:",enemy_obg.lives)
        elif result==1:
            print("You attac successfully!")
            result=enemy_obg.reduce_decrais()
            if result==0:
                print("Your lives:",self.lives,"|Enemy lives:",enemy_obg.lives)
            elif result==1:
                self.score+=5
                print("__________________________________________________")
                print("You killed enemy.Your score:",self.score,".Level:",enemy_obg.level)
                print("__________________________________________________")
        elif result==-1:
            print("You missed!")
            print("Your lives:",self.lives,"|Enemy lives:",enemy_obg.lives)
    def protection(self,enemy_obg):
        breac_bool=True
        while breac_bool:
            breac_bool=False
            try:
                print("Select Defense to Use:1-WISARD,2-WARRIOR,3-ROGUE",end=":")
                protection=int(input())
                if protection<0 or protection>3:
                    print("incorect input")
                    breac_bool=True
            except ValueError:
                print("incorect input")
                breac_bool=True
        attack=enemy_obg.select_attack()
        result=self.static_battle(attack,protection)
        if result==0:
            print("it`s a draw!")
            print("Your lives:",self.lives,"|Enemy lives:",enemy_obg.lives)

        elif result==1:
            print("Enemy hit you!")
            print("Your lives:",self.lives-1,"|Enemy lives:",enemy_obg.lives)
            return self.reduce_lives()
        elif result==-1:
            print("You dodged the attack")
            print("Your lives:",self.lives,"|Enemy lives:",enemy_obg.lives)
