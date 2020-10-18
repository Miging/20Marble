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


p1=Object("image/p1.png")
p1.locate(mainscene,0,90)
p2=Object("image/p2.png")
p2.locate(mainscene,0,180)
p3=Object("image/p3.png")
p3.locate(mainscene,0,270)
p4=Object("image/p4.png")
p4.locate(mainscene,0,360)
p5=Object("image/p5.png")
p5.locate(mainscene,0,450)
p6=Object("image/p6.png")
p6.locate(mainscene,0,540)
p7=Object("image/p7.png")
p7.locate(mainscene,160,660)
p8=Object("image/p8.png")
p8.locate(mainscene,320,660)
p9=Object("image/p9.png")
p9.locate(mainscene,480,660)
p10=Object("image/p10.png")
p10.locate(mainscene,640,660)
p11=Object("image/p11.png")
p11.locate(mainscene,800,660)
p12=Object("image/p12.png")
p12.locate(mainscene,960,660)
p13=Object("image/p13.png")
p13.locate(mainscene,1160,540)
p14=Object("image/p14.png")
p14.locate(mainscene,1160,450)
p15=Object("image/p15.png")
p15.locate(mainscene,1160,360)
p16=Object("image/p16.png")
p16.locate(mainscene,1160,270)
p17=Object("image/p17.png")
p17.locate(mainscene,1160,180)
p18=Object("image/p18.png")
p18.locate(mainscene,1160,90)
p19=Object("image/p19.png")
p19.locate(mainscene,960,0)
p20=Object("image/p20.png")
p20.locate(mainscene,800,0)
p21=Object("image/p21.png")
p21.locate(mainscene,640,0)
p22=Object("image/p22.png")
p22.locate(mainscene,480,0)
p23=Object("image/p23.png")
p23.locate(mainscene,320,0)
p24=Object("image/p24.png")
p24.locate(mainscene,160,0)

k1=Object("image/k1.png")
k1.locate(mainscene,0,90)
k2=Object("image/k2.png")
k2.locate(mainscene,0,180)
k3=Object("image/k3.png")
k3.locate(mainscene,0,270)
k4=Object("image/k4.png")
k4.locate(mainscene,0,360)
k5=Object("image/k5.png")
k5.locate(mainscene,0,450)
k6=Object("image/k6.png")
k6.locate(mainscene,0,540)
k7=Object("image/k7.png")
k7.locate(mainscene,160,660)
k8=Object("image/k8.png")
k8.locate(mainscene,320,660)
k9=Object("image/k9.png")
k9.locate(mainscene,480,660)
k10=Object("image/k10.png")
k10.locate(mainscene,640,660)
k11=Object("image/k11.png")
k11.locate(mainscene,800,660)
k12=Object("image/k12.png")
k12.locate(mainscene,960,660)
k13=Object("image/k13.png")
k13.locate(mainscene,1160,540)
k14=Object("image/k14.png")
k14.locate(mainscene,1160,450)
k15=Object("image/k15.png")
k15.locate(mainscene,1160,360)
k16=Object("image/k16.png")
k16.locate(mainscene,1160,270)
k17=Object("image/k17.png")
k17.locate(mainscene,1160,180)
k18=Object("image/k18.png")
k18.locate(mainscene,1160,90)
k19=Object("image/k19.png")
k19.locate(mainscene,960,0)
k20=Object("image/k20.png")
k20.locate(mainscene,800,0)
k21=Object("image/k21.png")
k21.locate(mainscene,640,0)
k22=Object("image/k22.png")
k22.locate(mainscene,480,0)
k23=Object("image/k23.png")
k23.locate(mainscene,320,0)
k24=Object("image/k24.png")
k24.locate(mainscene,160,0)

player1=Object("image/player1.png")
player1.locate(mainscene,0,50)
player1.setScale(0.3)
player1.show()

player2=Object("image/player2.png")
player2.locate(mainscene,70,50)
player2.setScale(0.3)
player2.show()


def on_startbtn(x,y,action):
    mainscene.enter()
startbtn.onMouseAction=on_startbtn

def on_explainbtn(x,y,action):
    explain.show()
explainbtn.onMouseAction=on_explainbtn

#맵 구현
#플레이어 위치 1로표기
gamemap=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
gamemap2=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
p1map=[0,p1,p2,p3,p4,p5,p6,0,p7,p8,p9,p10,p11,p12,0,p13,p14,p15,p16,p17,p18,0,p19,p20,p21,p22,p23,p24]
p2map=[0,k1,k2,k3,k4,k5,k6,0,k7,k8,k9,k10,k11,k12,0,k13,k14,k15,k16,k17,k18,0,k19,k20,k21,k22,k23,k24]

#트리플 독점 승리 플랜을 위한 색깔별 변수
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
a2=0
b2=0
c2=0
d2=0
e2=0
f2=0
g2=0
h2=0


#플레이어가 온적이 있는지 없는지 확인
#1이 왔다갔으면 1 2가 왔다 갔으면 2
visitmap=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
visitmap2=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#주사위 구현
dicebtn=Object("image/dicebtn.png")
dicebtn.locate(mainscene,490,100)
dicebtn.show()
move=0
timer=Timer(1)
showTimer(timer)

endtimer=Timer(3)
def on_dicebtn(x,y,action):


    move=random.randrange(1,7)
    showMessage(str(move)+"이 나왔다!")
    temp=gamemap.index(1)
    if gamemap.index(1)+move>27:
        gamemap[gamemap.index(1)+move-28]=1
        visitmap[gamemap.index(1)+move-28]=1
        if p1map[gamemap.index(1)+move-28]!=0:
            p1map[gamemap.index(1)+move-28].show()
            p2map[gamemap.index(1)+move-28].hide()


    else:
        gamemap[gamemap.index(1)+move]=1
        visitmap[gamemap.index(1)+move]=1  
        if p1map[gamemap.index(1)+move]!=0:
            p1map[gamemap.index(1)+move].show()
            p2map[gamemap.index(1)+move].hide()

    global a,b,c,d,e,f,g,h

    if visitmap[1]+visitmap[2]+visitmap[3]==3:
        a=1
    if visitmap[4]+visitmap[5]+visitmap[6]==3:
        b=1
    if visitmap[8]+visitmap[9]+visitmap[10]==3:
        c=1
    if visitmap[11]+visitmap[12]+visitmap[13]==3:
        d=1
    if visitmap[15]+visitmap[16]+visitmap[17]==3:
        e=1
    if visitmap[18]+visitmap[19]+visitmap[20]==3:
        f=1
    if visitmap[22]+visitmap[23]+visitmap[24]==3:
        g=1
    if visitmap[25]+visitmap[26]+visitmap[27]==3:
        h=1
    if a+b+c+d+e+f+g+h==3:
        showMessage("트리플 독점, 승리!")
        endtimer.start()
    gamemap[temp]=0
    #상대방
    timer.start()
dicebtn.onMouseAction=on_dicebtn

def timer_onTimeout():
    global a2,b2,c2,d2,e2,f2,g2,h2
    move=random.randrange(1,7)
    showMessage("상대는"+str(move)+"이 나왔다!")
    temp=gamemap2.index(1)
    if gamemap2.index(1)+move>27:
        gamemap2[gamemap2.index(1)+move-28]=1
        visitmap2[gamemap2.index(1)+move-28]=1
        if p2map[gamemap2.index(1)+move-28]!=0:
            p2map[gamemap2.index(1)+move-28].show()
            p1map[gamemap2.index(1)+move-28].hide()
    else:
        gamemap2[gamemap2.index(1)+move]=1
        visitmap2[gamemap2.index(1)+move]=1
        if p2map[gamemap2.index(1)+move]!=0:
            p2map[gamemap2.index(1)+move].show()
            p1map[gamemap2.index(1)+move].hide()
    if visitmap2[1]+visitmap2[2]+visitmap2[3]==3:
        a2=1
    if visitmap2[4]+visitmap2[5]+visitmap2[6]==3:
        b2=1
    if visitmap2[8]+visitmap2[9]+visitmap2[10]==3:
        c2=1
    if visitmap2[11]+visitmap2[12]+visitmap2[13]==3:
        d2=1
    if visitmap2[15]+visitmap2[16]+visitmap2[17]==3:
        e2=1
    if visitmap2[18]+visitmap2[19]+visitmap2[20]==3:
        f2=1
    if visitmap2[22]+visitmap2[23]+visitmap2[24]==3:
        g2=1
    if visitmap2[25]+visitmap2[26]+visitmap2[27]==3:
        h2=1
    if a2+b2+c2+d2+e2+f2+g2+h2==3:
        showMessage("상대의 승리ㅜ")
        endtimer.start()
    gamemap2[temp]=0
    timer.set(1)
timer.onTimeout=timer_onTimeout

def on_Endtimeout():
    endGame()
endtimer.onTimeout=on_Endtimeout
startGame(startscene)








