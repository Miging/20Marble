from bangtal import *
import random

startscene=Scene("","")
mainscene=Scene("","")

startbtn=Object()
explainbtn=Object()

explain=Object()
explain.hide()

def on_startbtn(x,y,action):
    mainscene.enter()
startbtn.onMouseAction=on_startbtn

def on_explainbtn(x,y,action):
    explain.show()
startbtn.onMouseAction=on_explainbtn

startGame(startscene)

#주사위 구현

dicebtn=Object()
move=0
def on_dicebtn(x,y,action):
    move=random.randrange(1,7)
dicebtn.onMouseAction=on_dicebtn

#맵 구현
#플레이어 1 위치 1로표기
gamemap=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#플레이어가 온적이 있는지 없는지 확인
#1이 왔다갔으면 1
visitmap=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#움직임 구현





