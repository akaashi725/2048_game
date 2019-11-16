import random
import pygame
import maingame
gameBoard = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
inducerlist = [0,1,2,3]

pygame.init()
win = pygame.display.set_mode((559,817))
pygame.display.set_caption("2048 for 정보수행평가")

try:
    gameboardimage = pygame.image.load(r'C:\Users\soarh\Documents\2048\realgameboard.jpg')
    gameboardimage = pygame.transform.scale(gameboardimage, (559,817))

    image2 = pygame.image.load(r'C:\Users\soarh\Documents\2048\2pic2.jpg')
    image2 = pygame.transform.scale(image2, (115,115))
    image4 = pygame.image.load(r'C:\Users\soarh\Documents\2048\4pic2.jpg')
    image4 = pygame.transform.scale(image4, (115,115))
    image8 = pygame.image.load(r'C:\Users\soarh\Documents\2048\8pic.jpg')
    image8 = pygame.transform.scale(image8, (115,115))
    image16 = pygame.image.load(r'C:\Users\soarh\Documents\2048\16pic.jpg')
    image16 = pygame.transform.scale(image16, (115,115))
    image32 = pygame.image.load(r'C:\Users\soarh\Documents\2048\32pic.jpg')
    image32 = pygame.transform.scale(image32, (115,115))
    image64 = pygame.image.load(r'C:\Users\soarh\Documents\2048\64pic.jpg')
    image64 = pygame.transform.scale(image64, (115,115))
    image128 = pygame.image.load(r'C:\Users\soarh\Documents\2048\128pic2.jpg')
    image128 = pygame.transform.scale(image128, (115,115))
    image256 = pygame.image.load(r'C:\Users\soarh\Documents\2048\256pic2.jpg')
    image256 = pygame.transform.scale(image256, (115,115))
    image512 = pygame.image.load(r'C:\Users\soarh\Documents\2048\512pic2.jpg')
    image512 = pygame.transform.scale(image512, (115,115))
    image1024 = pygame.image.load(r'C:\Users\soarh\Documents\2048\1024pic2.jpg')
    image1024 = pygame.transform.scale(image1024, (115,115))
    gameover = pygame.image.load(r'C:\Users\soarh\Documents\2048\gameover.png')
    gameover = pygame.transform.scale(gameover,(559,817))
except:
    print("지정하신 이미지를 찾을 수 없습니다. 경로를 다시 한 번 확인해주세요.")



def drawBoard(gameBoard):
    for i in range (0,4,1):
        for j in range (0,4,1):
            a = gameBoard[i][j]
            
            where_x = 30 + j*130
            where_y = 290 + i * 130
            if a == 2:
                win.blit(image2,(where_x,where_y))
                pygame.display.update()
            elif a==4:
                win.blit(image4,(where_x,where_y))
                pygame.display.update()
            elif a==8:
                win.blit(image8,(where_x,where_y))
                pygame.display.update()
            elif a==16:
                win.blit(image16,(where_x,where_y))
            elif a==32:
                win.blit(image32,(where_x,where_y))
            elif a==64:
                win.blit(image64,(where_x,where_y))
            elif a==128:
                win.blit(image128,(where_x,where_y))
            elif a==256:
                win.blit(image256,(where_x,where_y))
            elif a==512:
                win.blit(image512,(where_x,where_y))
            elif a==1024:
                win.blit(image1024,(where_x,where_y))

#처음에 겹치지 않게 랜덤으로 위치 2개 잡아서 2 대입하는 반복문
def createBoard():
    gameBoard[random.choice(inducerlist)][random.choice(inducerlist)]=2
    x=random.choice(inducerlist)
    y=random.choice(inducerlist)
    if gameBoard[x][y]==0:
        gameBoard[x][y]=2
        win.blit(gameboardimage,(0,0))
        drawBoard(gameBoard)
        pygame.display.update()
    else:
        createBoard()




createBoard()

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        

        elif event.type == pygame.KEYUP:
            
            
            win.blit(gameboardimage,(0,0))
            if event.key == pygame.K_LEFT:
                user_input = 'a'
                maingame.users_choice(gameBoard,user_input)
                drawBoard(gameBoard)
            
            elif event.key == pygame.K_RIGHT:
                user_input='d'
                maingame.users_choice(gameBoard,user_input)
                drawBoard(gameBoard)
                
            elif event.key == pygame.K_UP:
                user_input = 'w'
                maingame.users_choice(gameBoard,user_input)
                drawBoard(gameBoard)
                
            elif event.key == pygame.K_DOWN:
                user_input = 's'
                maingame.users_choice(gameBoard,user_input)
                drawBoard(gameBoard)
            #이 밑으로는 그 빈 곳 중에서 랜덤으로 골라서 2를 넣는 코드인데 여긴 잘 됨
            listfori = []
            listforj = []
            count = 0
            for i in range(0,4):
                for j in range(0,4):
                    if gameBoard[i][j]==0:
                        count+=1
                        listfori.append(i)
                        listforj.append(j)
            if count > 0:
                if count > 1:
                    randomindex = listfori.index(random.choice(listfori))
                    gameBoard[listfori[randomindex]][listforj[randomindex]]=2
                    drawBoard(gameBoard)
                else:
                    gameBoard[listfori[0]][listforj[0]]=2
            else:
                win.fill((0,0,0))
                win.blit(gameover,(0,0))

                
                
            pygame.display.update()

       
        
