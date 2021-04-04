import time
class GameOver(Exception):
    """Game over"""
    def __init__(self,score,name):
        """init"""
        self.score=score
        self.name=name
    def writer(self):
        """запись результата в текстовый файл"""
        with open('scores.txt','r') as file:
            text=file.readlines()
        with open('scores.txt','w') as file:
            ind=len(text)
            if len(text)<1:
                file.writelines(text+
                                [str(self.name)+
                                 ' : '+str(self.score)+
                                 ' | '+time.strftime("%d.%m.%Y %H:%M")+'\n'])
            else:
                for i in text:
                    if self.score>int(i.split(' ')[2]):
                        ind=text.index(i)
                        break
                file.writelines(text[0:ind]+
                                [str(self.name)+
                                 ' : '+str(self.score)+
                                 ' | '+time.strftime("%d.%m.%Y %H:%M")+
                                 '\n']+text[ind:len(text)])
class EnemyDown(Exception):
    pass
