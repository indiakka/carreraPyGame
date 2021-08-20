import turtle
import random

class Race():
    players = []
    players_color = ['red', 'green', 'blue', 'orange']
    players_initY = [-30,-10, 10, 30]
    
    def __ijnit__(self, width, height):
        self.players = []
        self.width = width
        self.height = height
        
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.bgcolor('lightgray')
        
        self.startline = -width / 2 + 20
        self.finishline = width / 2 - 20
        
        self.__iniPlayers()
        
    def __iniPlayers(self):
        for i in range (4):
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.pu()
            new_turtle.color(self.players_colors[i])
            new_turtle.setpos(self.startline, self.players_initY[i] * self.height/200)
            self.players.append(new_turtle)
            
    def comeptir(self):
        winner = False
        
        while winner == False:
            for i in range(4):
                player = self.players [i]
                advanec = random.randint(0,5)
                player.fd(advance)
                xcor = player.xcor()
                if xcor >= self.finishline:
                winner = True
                print("The winner is {} turtle".format(player.color()[0]))
                break
            
    if __name__ =='__main__':
        r = Race(640, 480)
        r.competir()