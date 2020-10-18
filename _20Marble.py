from bangtal import *
import random

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)


startscene=Scene("시작화면","image/startimage.png")
mainscene=Scene("게임화면","image/mainimage.png")

startbtn=Object("image/startbtn.png")
startbtn.locate(startscene,490,100)
startbtn.show()

explainbtn=Object("image/")

explain=Object("image/")
explain.hide()

player1=Object("image/player1.png")
player1.locate(mainscene,0,50)
player1.setScale(0.5)
player1.show()

player2=Object("image/player2.png")
player2.locate(mainscene,100,50)
player2.setScale(0.5)
player2.show()

def on_startbtn(x,y,action):
    mainscene.enter()
startbtn.onMouseAction=on_startbtn

def on_explainbtn(x,y,action):
    explain.show()
explainbtn.onMouseAction=on_explainbtn

#맵 구현
#플레이어 1 위치 1로표기
gamemap=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#플레이어가 온적이 있는지 없는지 확인
#1이 왔다갔으면 1
visitmap=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#주사위 구현
dicebtn=Object("")
move=0
def on_dicebtn(x,y,action):
    move=random.randrange(1,7)
    showMessage(str(move)+"이 나왔다!")
    gamemap[gamemap.index(1)]=0
    if gamemap.index(1)+move>32:
        gamemap[gamemap.index(1)+move-32]=1
        visitmap[gamemap.index(1)+move-32]=1
    else:
        gamemap[gamemap.index(1)+move]=1
        visitmap[gamemap.index(1)+move]=1   
dicebtn.onMouseAction=on_dicebtn

startGame(startscene)







