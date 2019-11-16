def users_choice(gameBoard,user_input):
    if user_input == "w":
        i=0
        for j in range(0,4):
            if gameBoard[i][j]!=0 or gameBoard[i+1][j]!=0 or gameBoard[i+2][j]!=0 or gameBoard[i+3][j]!=0:
                if gameBoard[i][j]==0:
                    while gameBoard[i][j]==0:
                        gameBoard[i][j]=gameBoard[i+1][j]
                        gameBoard[i+1][j]=gameBoard[i+2][j]
                        gameBoard[i+2][j] = gameBoard[i+3][j]
                        gameBoard[i+3][j]=0
                if gameBoard[i+1][j]==0 and (gameBoard[i+2][j]!=0 or gameBoard[i+3][j]!=0):
                    while gameBoard[i+1][j]==0:                         
                        gameBoard[i+1][j]=gameBoard[i+2][j]
                        gameBoard[i+2][j]=gameBoard[i+3][j]
                        gameBoard[i+3][j]=0
                if gameBoard[i+2][j]==0 and (gameBoard[i+3][j]!=0):
                    while gameBoard[i+2][j]==0:
                        gameBoard[i+2][j]=gameBoard[i+3][j]
                        gameBoard[i+3][j]=0
        i=0
        for j in range(0,4):
            if gameBoard[i][j]==gameBoard[i+1][j]:
                gameBoard[i][j]=gameBoard[i][j]+gameBoard[i+1][j]
                gameBoard[i+1][j]=gameBoard[i+2][j]
                gameBoard[i+2][j]=gameBoard[i+3][j]
                gameBoard[i+3][j]=0
            if gameBoard[i+1][j]==gameBoard[i+2][j]:
                gameBoard[i+1][j]=gameBoard[i+1][j]+gameBoard[i+2][j]
                gameBoard[i+2][j]=gameBoard[i+3][j]
                gameBoard[i+3][j]=0
            if gameBoard[i+2][j]==gameBoard[i+3][j]:
                gameBoard[i+2][j]=gameBoard[i+2][j]+gameBoard[i+3][j]
                gameBoard[i+3][j]=0
                         
                         
           
    elif user_input == "s":
        i=0
        for j in range(0,4):
            if gameBoard[i][j]!=0 or gameBoard[i+1][j]!=0 or gameBoard[i+2][j]!=0 or gameBoard[i+3][j]!=0:
                if gameBoard[i+3][j]==0:
                    while gameBoard[i+3][j]==0:
                        gameBoard[i+3][j]=gameBoard[i+2][j]
                        gameBoard[i+2][j]=gameBoard[i+1][j]
                        gameBoard[i+1][j]=gameBoard[i][j]
                        gameBoard[i][j]=0
                if gameBoard[i+2][j]==0 and (gameBoard[i+1][j]!=0 or gameBoard[i][j]!=0):
                    while gameBoard[i+2][j]==0:
                        gameBoard[i+2][j]=gameBoard[i+1][j]
                        gameBoard[i+1][j]=gameBoard[i][j]
                        gameBoard[i][j]=0
 
                if gameBoard[i+1][j]==0 and gameBoard[i][j]!=0:
                    while gameBoard[i+1][j]==0:
                        gameBoard[i+1][j]=gameBoard[i][j]
                        gameBoard[i][j]=0
        i=0
        for j in range(0,4):
            if gameBoard[i+3][j]==gameBoard[i+2][j]:
                gameBoard[i+3][j]=gameBoard[i+3][j] + gameBoard[i+2][j]
                gameBoard[i+2][j]=gameBoard[i+1][j]
                gameBoard[i+1][j]=gameBoard[i][j]
                gameBoard[i][j]=0
            if gameBoard[i+2][j]==gameBoard[i+1][j]:
                gameBoard[i+2][j]=gameBoard[i+2][j]+gameBoard[i+1][j]
                gameBoard[i+1][j]=gameBoard[i][j]
                gameBoard[i][j]=0
            if gameBoard[i+1][j]==gameBoard[i][j]:
                gameBoard[i+1][j]=gameBoard[i+1][j]+gameBoard[i][j]
                gameBoard[i][j]=0
             
    elif user_input == "a":
        j=0
        for i in range(0,4):
 
            if gameBoard[i][j]!=0 or gameBoard[i][j+1]!=0 or gameBoard[i][j+2]!=0 or gameBoard[i][j+3]!=0:
                if gameBoard[i][j]==0:
                    while gameBoard[i][j]==0:
                        gameBoard[i][j]=gameBoard[i][j+1]
                        gameBoard[i][j+1]=gameBoard[i][j+2]
                        gameBoard[i][j+2] = gameBoard[i][j+3]
                        gameBoard[i][j+3]=0
                if gameBoard[i][j+1]==0 and (gameBoard[i][j+2]!=0 or gameBoard[i][j+3]!=0):
                    while gameBoard[i][j+1]==0:
                        gameBoard[i][j+1]=gameBoard[i][j+2]
                        gameBoard[i][j+2]=gameBoard[i][j+3]
                        gameBoard[i][j+3]=0
                if gameBoard[i][j+2]==0 and (gameBoard[i][j+3]!=0):
                    while gameBoard[i][j+2]==0:
                        gameBoard[i][j+2]=gameBoard[i][j+3]
                        gameBoard[i][j+3]=0
        j=0
        for i in range(0,4):
            if gameBoard[i][j]==gameBoard[i][j+1]:
                gameBoard[i][j]=gameBoard[i][j]+gameBoard[i][j+1]
                gameBoard[i][j+1]=gameBoard[i][j+2]
                gameBoard[i][j+2]=gameBoard[i][j+3]
                gameBoard[i][j+3]=0
            if gameBoard[i][j+1]==gameBoard[i][j+2]:
                gameBoard[i][j+1]=gameBoard[i][j+1]+gameBoard[i][j+2]
                gameBoard[i][j+2]=gameBoard[i][j+3]
                gameBoard[i][j+3]=0
            if gameBoard[i][j+2]==gameBoard[i][j+3]:
                gameBoard[i][j+2]=gameBoard[i][j+2]+gameBoard[i][j+3]
                gameBoard[i][j+3]=0
    elif user_input == "d":
        j=0
        for i in range(0,4):
            if gameBoard[i][j]!=0 or gameBoard[i][j+1]!=0 or gameBoard[i][j+2]!=0 or gameBoard[i][j+3]!=0:
                if gameBoard[i][j+3]==0:
                    while gameBoard[i][j+3]==0:
                        gameBoard[i][j+3]=gameBoard[i][j+2]
                        gameBoard[i][j+2]=gameBoard[i][j+1]
                        gameBoard[i][j+1]=gameBoard[i][j]
                        gameBoard[i][j]=0
                if gameBoard[i][j+2]==0 and (gameBoard[i][j+1]!=0 or gameBoard[i][j]!=0):
                    while gameBoard[i][j+2]==0:
                        gameBoard[i][j+2]=gameBoard[i][j+1]
                        gameBoard[i][j+1]=gameBoard[i][j]
                        gameBoard[i][j]=0
 
                if gameBoard[i][j+1]==0 and gameBoard[i][j]!=0:
                    while gameBoard[i][j+1]==0:
                        gameBoard[i][j+1]=gameBoard[i][j]
                        gameBoard[i][j]=0
        j=0
        for i in range(0,4):
            if gameBoard[i][j+3]==gameBoard[i][j+2]:
                gameBoard[i][j+3]=gameBoard[i][j+3] + gameBoard[i][j+2]
                gameBoard[i][j+2]=gameBoard[i][j+1]
                gameBoard[i][j+1]=gameBoard[i][j]
                gameBoard[i][j]=0
            if gameBoard[i][j+2]==gameBoard[i][j+1]:
                gameBoard[i][j+2]=gameBoard[i][j+2] + gameBoard[i][j+1]
                gameBoard[i][j+1]=gameBoard[i][j]
                gameBoard[i][j]=0
            if gameBoard[i][j+1]==gameBoard[i][j]:
                gameBoard[i][j+1]=gameBoard[i][j+1] + gameBoard[i][j]
                gameBoard[i][j]=0
