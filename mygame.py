from pygame import *

img_player1 = 'player1.png'
img_player2 = 'player2.png'
img_back = 'pole.jpg'
img_ball = 'ball.png'
img_goal = 'goal.png'

font.init()
font1 = font.SysFont("Arial", 80)
font2 = font.SysFont("Arial", 36)
player1score = 0
player2score = 0
bx = 4
by = 4
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("football")
background = transform.scale(image.load(img_back), (win_width, win_height))

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):

        sprite.Sprite.__init__(self)


        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 444:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 444:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed

goal1 = GameSprite(img_goal, 0, win_height - 312, 10, 120, 20)
goal2 = GameSprite(img_goal, 690, win_height - 312, 10, 120, 20)
ball = GameSprite(img_ball, 335, win_height - 270, 50, 50, 20)
player2 = Player(img_player1, 37, win_height - 267, 50, 50, 20)
player3 = Player(img_player1, 23, win_height - 253, 50, 50, 20)
player4 = Player(img_player1, 37, win_height - 253, 50, 50, 20)
player5 = Player(img_player1, 23, win_height - 267, 50, 50, 20)
player6 = Player1(img_player2, 637, win_height - 267, 50, 50, 20)
player7 = Player1(img_player2, 623, win_height - 267, 50, 50, 20)
player8 = Player1(img_player2, 637, win_height - 253, 50, 50, 20)
player9 = Player1(img_player2, 623, win_height - 253, 50, 50, 20)

finish = False
run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
 
    if not finish:
        if sprite.collide_rect(ball, player2) and sprite.collide_rect(ball, player4) and ball.rect.x < 650:
            for i in range(40):
                ball.rect.x += 1
        if sprite.collide_rect(ball, player3) and sprite.collide_rect(ball, player5) and ball.rect.x > 0:
            for i in range(40):
                ball.rect.x -= 1
        if sprite.collide_rect(ball, player2) and sprite.collide_rect(ball, player5) and ball.rect.y > 0:
            for i in range(40):
                ball.rect.y -= 1
        if sprite.collide_rect(ball, player4) and sprite.collide_rect(ball, player3) and ball.rect.y < 440:
            for i in range(40):
                ball.rect.y += 1
        if sprite.collide_rect(ball, player2) and ball.rect.x < 650 and ball.rect.y > 0:
            for i in range(20):
                ball.rect.x += 1
                ball.rect.y -= 1
        if sprite.collide_rect(ball, player3) and ball.rect.x > 0 and ball.rect.y < 440:
            for i in range(20):
                ball.rect.x -= 1 
                ball.rect.y += 1
        if sprite.collide_rect(ball, player4) and ball.rect.x < 650 and ball.rect.y < 440:
            for i in range(20):
                ball.rect.x += 1
                ball.rect.y += 1
        if sprite.collide_rect(ball, player5) and ball.rect.x > 0 and ball.rect.y > 0:
            for i in range(20):
                ball.rect.x -= 1
                ball.rect.y -= 1

        if sprite.collide_rect(ball, player6) and sprite.collide_rect(ball, player8) and ball.rect.x < 650:
            for i in range(40):
                ball.rect.x += 1
        if sprite.collide_rect(ball, player9) and sprite.collide_rect(ball, player7) and ball.rect.x > 0:
            for i in range(40):
                ball.rect.x -= 1
        if sprite.collide_rect(ball, player6) and sprite.collide_rect(ball, player7) and ball.rect.y > 0:
            for i in range(40):
                ball.rect.y -= 1
        if sprite.collide_rect(ball, player8) and sprite.collide_rect(ball, player9) and ball.rect.y < 440:
            for i in range(40):
                ball.rect.y += 1
        if sprite.collide_rect(ball, player6) and ball.rect.x < 650 and ball.rect.y > 0:
            for i in range(20):
                ball.rect.x += 1
                ball.rect.y -= 1
        if sprite.collide_rect(ball, player9) and ball.rect.x > 0 and ball.rect.y < 440:
            for i in range(20):
                ball.rect.x -= 1 
                ball.rect.y += 1
        if sprite.collide_rect(ball, player8) and ball.rect.x < 650 and ball.rect.y < 440:
            for i in range(20):
                ball.rect.x += 1
                ball.rect.y += 1
        if sprite.collide_rect(ball, player7) and ball.rect.x > 0 and ball.rect.y > 0:
            for i in range(20):
                ball.rect.x -= 1
                ball.rect.y -= 1
        

        text = font2.render("Рахунок: " + str(player1score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text2 = font2.render("Рахунок: " + str(player2score), 1, (255, 255, 255))
        window.blit(text2, (520, 20)) 
        
        if ball.rect.x <= 5:
            ball.rect.x += 20
        if ball.rect.x >= 645:
            ball.rect.x -= 20 
        if ball.rect.y <= 5:
            ball.rect.y += 20
        if ball.rect.y >= 440:
            ball.rect.y -= 20 

        if player2.rect.x >= 650 or player4.rect.x >= 650:
            player2.rect.x -= 20
            player3.rect.x -= 20
            player4.rect.x -= 20
            player5.rect.x -= 20

        if player3.rect.x <= 5 or player5.rect.x <= 5:
            player2.rect.x += 20
            player3.rect.x += 20
            player4.rect.x += 20
            player5.rect.x += 20

        if player4.rect.y >= 435 or player3.rect.y >= 435:
            player2.rect.y -= 20
            player3.rect.y -= 20
            player4.rect.y -= 20
            player5.rect.y -= 20

        if player2.rect.y <= 5 or player5.rect.y <= 5:
            player2.rect.y += 20
            player3.rect.y += 20
            player4.rect.y += 20
            player5.rect.y += 20

        if player6.rect.x >= 650 or player8.rect.x >= 650:
            player6.rect.x -= 20
            player7.rect.x -= 20
            player8.rect.x -= 20
            player9.rect.x -= 20

        if player9.rect.x <= 5 or player5.rect.x <= 7:
            player9.rect.x += 20
            player8.rect.x += 20
            player7.rect.x += 20
            player6.rect.x += 20

        if player8.rect.y >= 435 or player9.rect.y >= 435:
            player6.rect.y -= 20
            player7.rect.y -= 20
            player9.rect.y -= 20
            player8.rect.y -= 20

        if player6.rect.y <= 5 or player5.rect.y <= 7:
            player6.rect.y += 20
            player7.rect.y += 20
            player8.rect.y += 20
            player9.rect.y += 20

        if sprite.collide_rect(ball, goal1):
            player2score += 1
            ball.rect.x = 335
            ball.rect.y = win_height - 270
            player2.rect.x =  37
            player3.rect.x =  23
            player4.rect.x =  37
            player5.rect.x =  23
            player6.rect.x =  637
            player7.rect.x =  623
            player8.rect.x =  637
            player9.rect.x = 623 
            player2.rect.y = win_height - 267
            player3.rect.y = win_height - 253
            player4.rect.y = win_height - 253
            player5.rect.y = win_height - 267
            player6.rect.y = win_height - 267
            player7.rect.y = win_height - 267
            player8.rect.y = win_height - 253
            player9.rect.y = win_height - 253

        if sprite.collide_rect(ball, goal2):
            player1score += 1
            ball.rect.x = 335
            ball.rect.y = win_height - 270
            player2.rect.x =  37
            player3.rect.x =  23
            player4.rect.x =  37
            player5.rect.x =  23
            player6.rect.x =  637
            player7.rect.x =  623
            player8.rect.x =  637
            player9.rect.x = 623 
            player2.rect.y = win_height - 267
            player3.rect.y = win_height - 253
            player4.rect.y = win_height - 253
            player5.rect.y = win_height - 267
            player6.rect.y = win_height - 267
            player7.rect.y = win_height - 267
            player8.rect.y = win_height - 253
            player9.rect.y = win_height - 253

        if player2score == 3:
            finish = True
            player1win = font1.render("Blue WIN " , 1, (0, 0, 255))
            window.blit(player1win, (210, 110))
        if player1score == 3:
            finish = True
            player1win = font1.render("Red WIN " , 1, (255, 0, 0))
            window.blit(player1win, (210, 110))


        goal1.update()
        goal1.reset()
        goal2.update()
        goal2.reset()
        ball.update()
        ball.reset()
        player7.update()
        player7.reset()
        player8.update()
        player8.reset()
        player9.update()
        player9.reset()
        player6.update()
        player6.reset()
        player5.update()
        player5.reset()
        player4.update()
        player4.reset()
        player3.update()
        player3.reset()
        player2.update()
        player2.reset()
        display.update()
        window.blit(background,(0,0))

    time.delay(30)