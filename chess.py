class chessBoard:
    def __init__(self,name):
        self.name=name
        self.board = [[x for x in range(8)] for y in range(8)]

        for x in range(8):
            for y in range(8):
                if (x==0 and (y==0 or y==7)):
                    self.board[x][y]=piece('rook','white',(x,y))
                elif (x==7 and (y==0 or y==7)):
                    self.board[x][y]=piece('rook','black',(x,y))
                elif x==1:
                    self.board[x][y]=piece('pawn','white',(x,y))
                elif x==6:
                    self.board[x][y]=piece('pawn','black',(x,y))
                elif (x==0 and (y==1 or y==6)):
                    self.board[x][y]=piece('knight','white',(x,y))
                elif (x==7 and (y==1 or y==6)):
                    self.board[x][y]=piece('knight','black',(x,y))
                elif (x==0 and (y==2 or y==5)):
                    self.board[x][y]=piece('bishop','white',(x,y))
                elif (x==7 and (y==2 or y==5)):
                    self.board[x][y]=piece('bishop','black',(x,y))
                elif (x==0 and y==3):
                    self.board[x][y]=piece('queen','white',(x,y))
                elif(x==7 and y==3):
                    self.board[x][y]=piece('queen','black',(x,y))
                elif (x==0 and y==4):
                    self.board[x][y]=piece('king','white',(x,y))
                elif (x==7 and y==4):
                    self.board[x][y]=piece('king','black',(x,y))
                else:
                    self.board[x][y]=piece(' ','green',(x,y))
    def printBoard(self):
        for x in range(8):
            row=''
            for y in range(8):
                row=row +'| '+self.board[x][y].name[0]+ ' |'
            print(row)


class piece:
    def __init__(self,name,color,position):
        self.name=name
        self.color=color
        self.position=position

    def canMove(position):
