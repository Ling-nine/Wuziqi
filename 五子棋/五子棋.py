import pygame
import sys
from pygame.locals import *
import numpy as np

pygame.init()
size = width,height = 750,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('五子棋')
an = 0
lz=[]
rlzd=[]
qu = 0
jc = 0
col = 1
winner = 0

pb = pygame.image.load('.\旁版.png').convert()
zqb = pygame.image.load('.\置棋板.png').convert_alpha()
cwbutton = pygame.image.load('.\重玩.png').convert_alpha()
hqbutton = pygame.image.load('.\悔棋.png').convert_alpha()
hfwin = pygame.image.load('.\黑方胜利.png').convert_alpha()
bfwin = pygame.image.load('.\白方胜利.png').convert_alpha()

def color(col):
    global qp,hqz,bqz
    if col%2 == 0:
        qp = pygame.image.load('.\五子棋盘1.png').convert() 
        hqz = pygame.image.load('.\黑棋子1.png').convert_alpha()
        bqz = pygame.image.load('.\白棋子1.png').convert_alpha()
    if col%2 == 1:
        qp = pygame.image.load('.\五子棋盘.png').convert() 
        hqz = pygame.image.load('.\黑棋子.png').convert_alpha()
        bqz = pygame.image.load('.\白棋子.png').convert_alpha()
color(col)

def begin():
    global cwb,hqb,rzqb,rhqz,rbqz,xrhqz,xrbqz,hw,bw
    cwb = pygame.transform.scale(cwbutton,(120,60))
    hqb = pygame.transform.scale(hqbutton,(120,60))
    rzqb = pygame.transform.scale(zqb,(110,110))
    rhqz = pygame.transform.scale(hqz,(30,30))
    rbqz = pygame.transform.scale(bqz,(30,30))
    xrhqz = pygame.transform.scale(hqz,(60,60))
    xrbqz = pygame.transform.scale(bqz,(60,60))
    hw = pygame.transform.scale(hfwin,(100,25))
    bw = pygame.transform.scale(bfwin,(100,25))
    screen.blit(qp,(0,0))
    screen.blit(pb,(601,0))
    screen.blit(rzqb,(620,20))
    screen.blit(xrhqz,(646,44))
    screen.blit(cwb,(620,300))
    screen.blit(hqb,(620,400))

def run():
    global an,lz,qu,jc,rlzd,winner,qp,hqz,bqz,xrhqz,xrbqz,col,rhqz,rbqz
    while 1:
        for event in pygame.event.get():  # 循环获取事件
            if event.type == MOUSEBUTTONDOWN:
                if winner == 1:
                    if pygame.mouse.get_pressed()[0]:
                        an = 0
                        lz=[]
                        rlzd = []
                        qu = 0
                        jc = 0
                        begin()
                        winner = 0
                        run()

                if pygame.mouse.get_pos()[0] >= 620 and pygame.mouse.get_pos()[0] <= 740:
                    if pygame.mouse.get_pos()[1] >= 300 and pygame.mouse.get_pos()[1] <= 360: #重玩
                        if pygame.mouse.get_pressed()[0]:
                            an = 0
                            lz=[]
                            rlzd = []
                            qu = 0
                            jc = 0
                            begin()
                    if pygame.mouse.get_pos()[1] >= 400 and pygame.mouse.get_pos()[1] <= 460: #悔棋
                        if pygame.mouse.get_pressed()[0] and lz:
                            an-=1
                            lz.pop()
                            rlzd.pop()
                            black = lz[::2]
                            white = lz[1::2]
                            wzlz(rblack)
                            wzlz(rwhite)
                            begin()
                            for qzh in black:
                                screen.blit(rhqz,(qzh))
                            for qzb in white:
                                screen.blit(rbqz,(qzb))
                            if len(black) == len(white):
                                screen.blit(xrhqz,(646,44))
                            else:
                                screen.blit(xrbqz,(646,44))
                            #通过清除全屏去掉一组后跟据黑白两组复原棋盘

                if pygame.mouse.get_pos()[0] >= 646 and pygame.mouse.get_pos()[0] <= 706:
                    if pygame.mouse.get_pos()[1] >= 44 and pygame.mouse.get_pos()[1] <= 104: #换色
                        if pygame.mouse.get_pressed()[0]:
                            an = 0
                            lz=[]
                            rlzd = []
                            qu = 0
                            jc = 0
                            col +=1
                            color(col)
                            begin()
                            run()
                                
                if pygame.mouse.get_pressed()[0] and winner == 0: #落子
                    pos = pygame.mouse.get_pos()
                    posl = list(pos)
                    an+=1
                    def ld(l): #计算落子点
                        x =15
                        if (l[0]-20)%40<21:
                            l[0] = l[0]-(l[0]-20)%40-x
                        if (l[0]-20)%40>20:
                            l[0] = l[0]-(l[0]-20)%40-x+40
                        if (l[1]-20)%40<21:
                            l[1] = l[1]-(l[1]-20)%40-x
                        if (l[1]-20)%40>20:
                            l[1] = l[1]-(l[1]-20)%40-x+40
                        if l[0]<601:
                            if l[0]>560:
                                l[0] = 580-x
                            if l[1]>560:
                                l[1] = 580-x
                            if l[0]<20:
                                l[0] = 20-x
                            if l[1]<20:
                                l[1] = 20-x
                            
                            return l
                        else:
                            global an
                            an-=1
                            return [-10000,-10000]

                    posl = ld(posl)
                    if posl != [-10000,-10000]:
                        if qu == 0:
                            lz.append(posl)
                            black = lz[::2]
                            white = lz[1::2]
                            rlzd.append([int((posl[0]-5)/40),int((posl[1]-5)/40)])
                            rblack = rlzd[::2]
                            rwhite = rlzd[1::2]
                            screen.blit(rhqz,(posl))
                            screen.blit(xrbqz,(646,44))
                            qu += 1
                        else:
                            for si in lz:
                                if si == posl:
                                    jc +=1
                            if jc != 1: #显示棋子
                                lz.append(posl)
                                black = lz[::2]
                                white = lz[1::2]
                                rlzd.append([int((posl[0]-5)/40),int((posl[1]-5)/40)])
                                rblack = rlzd[::2]
                                rwhite = rlzd[1::2]
                                if an%2 == 0:
                                    screen.blit(rbqz,(posl))
                                    screen.blit(xrhqz,(646,44))
                                    if wzlz(rwhite): #白方胜利
                                        screen.blit(bw,(250,25))
                                        winner = 1
                                if an%2 == 1:
                                    screen.blit(rhqz,(posl))
                                    screen.blit(xrbqz,(646,44))
                                    if wzlz(rblack): #黑方胜利
                                        screen.blit(hw,(250,25))
                                        winner = 1
                            if jc == 1:
                                an-=1
                                jc = 0


            if event.type == QUIT:  # 若检测到事件类型为退出，则退出系统
                pygame.quit()
                sys.exit()
        pygame.display.update()  # 刷新屏幕内容

def wzlz(xf):
    lp=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

    for i in xf:
        qw = 0
        lp[i[1]][i[0]] = 1
        #横判定五子
        for ik in lp:
            for ti in ik:
                if ti == 1:
                    qw += 1
                if ti == 0:
                    qw = 0
                if qw == 5:
                    return True

        #竖判定五子
        ra = [a for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rb = [b for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rc = [c for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rd = [d for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        re = [e for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rf = [f for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rg = [g for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rh = [h for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        ri = [i for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rj = [j for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rk = [k for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rl = [l for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rm = [m for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rn = [n for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        ro = [o for [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o] in lp]
        rlp = [ra,rb,rc,rd,re,rf,rg,rh,ri,rj,rk,rl,rm,rn,ro]
        
        rqw = 0
        for rik in rlp:
            for rt in rik:
                if rt == 1:
                    rqw += 1
                if rt == 0:
                    rqw = 0
                if rqw == 5:
                    return True

        #斜判断五子
        def xjs(w,c):
            er = 0
            rer = 0
            
            el = 0
            lel = 0
            for df in range(0,w):
                #右
                if lp[df][df+c-1] == lp[df+1][df+c] == 1:
                    er += 1
                if er == 4:
                    return True
                
                if lp[-df-1][df+c-1] == lp[-df-2][df+c] == 1:
                    rer += 1
                if rer == 4:
                    return True
                
                if lp[df][df+c-1] == lp[df+1][df+c] == 0 or lp[df][df+c-1] != lp[df+1][df+c]:
                    er = 0
 
                if lp[-df-1][df+c-1] == lp[-df-2][df+c] == 0 or lp[-df-1][df+c-1] != lp[-df-2][df+c]:
                    rer = 0


                #左
                if lp[df+c-1][df] == lp[df+c][df+1] == 1:
                    el += 1
                if el == 4:
                    return True

                if lp[df][-df-c] == lp[df+1][-df-c-1] == 1:
                    lel += 1
                if lel == 4:
                    return True
                
                if lp[df+c-1][df] == lp[df+c][df+1] == 0 or lp[df+c-1][df] != lp[df+c][df+1]:
                    el = 0

                if lp[df][-df-c] == lp[df+1][-df-c-1] == 0 or lp[df][-df-c] != lp[df+1][-df-c-1]:
                    lel = 0

        co = 0
        for dr in range(0,15):
            co +=1
            if xjs(14-dr,co):
                return True
begin()
run()

    
