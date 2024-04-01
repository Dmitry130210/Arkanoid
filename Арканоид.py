import pygame
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)
fpsClock = pygame.time.Clock()
pygame.init()
font = pygame.font.SysFont(None, 30)

#Блок
class Block():
        
        def __init__(self, x, y, w, h, visible, color):
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.visible = visible
                self.color = color
        
        def draw(self):
                if self.visible:
                        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), 0)
            
#Игрок
class Platform():  
        def __init__(self, x, y, w, h, speed):   
                self.x = x
                self.y = y
                self.w = w
                self.h = h
                self.speed = speed
        
        def draw(self):
                pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.w, self.h), 0)
                
                
#Шарик
class Ball():  
        def __init__(self, x, y, r, vx, vy):   
                self.x = x
                self.y = y
                self.r = r
                self.vx = vx
                self.vy = vy
        
        
        def draw(self):
                pygame.draw.circle(screen, 'red', (self.x, self.y), self.r, 0)

def button(x_button, y_button, width_button, height_button, stroka):
        color = pygame.Color(50, 150, 150)
        pygame.draw.rect(screen, color, (x_button+3, y_button+3, width_button, height_button), 0)
        hsv = color.hsva
        color.hsva = (hsv[0], hsv[1], hsv[2]+30, hsv[3])
        pygame.draw.rect(screen, color, (x_button, y_button, width_button, height_button), 0)
        color.hsva = (hsv[0], hsv[1], hsv[2], hsv[3])
        pygame.draw.rect(screen, color, (x_button, y_button, width_button, height_button), 3)
        
        font = pygame.font.SysFont('timesnewroman', 30, bold = True, italic = False)
        text = font.render(stroka, 0, (255, 0, 0))
        dx = width_button//2 - text.get_width()//2
        dy = height_button//2 - text.get_height()//2
        screen.blit(text, (x_button + dx, y_button + dy)) 
        
width_button = 200
height_button = 50
x_button = width//2 - width_button//2
y_button = 200
    
PAGE = 'menu'
color_bg = 'white'

blocks_list = []

#Создание блоков  
def creatBlocks(level):
        font = pygame.font.SysFont('timesnewroman',10, bold = True, italic = False)
        text = font.render("Уровень" + str(level), 0, (255, 0, 0))
        dx = width//2 - text.get_width()//2
        screen.blit(text, (dx, 0))        
        color_list = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'violet', 'pink']       

        if level == 1:
                num_color = 0
                for x in range(50, 600, 70):        
                        blocks_list.append(Block(x, 20, 60, 30, True, color_list[num_color]))
                        num_color += 1
                    
                num_color = 0
                for x in range(80, 600-70, 70):
                        blocks_list.append(Block(x, 60, 60, 30, True, color_list[num_color]))
                        num_color += 1
                    
                num_color = 0
                for x in range(50, 600, 70):
                        blocks_list.append(Block(x, 100, 60, 30, True, color_list[num_color]))
                        num_color += 1
                    
                num_color = 0
                for x in range(80, 600-70, 70):
                        blocks_list.append(Block(x, 140, 60, 30, True, color_list[num_color]))
                        num_color += 1
                
        if level == 2:
                num_color = 0
                for x in range(50, 600, 70):        
                        blocks_list.append(Block(x, 20, 60, 30, True, color_list[num_color]))
                        num_color += 1
                    
                num_color = 0
                for x in range(80, 600-70, 70):
                        blocks_list.append(Block(x, 60, 60, 30, True, color_list[num_color]))
                        num_color += 1
                    
                num_color = 0
                for x in range(50, 600, 70):
                        blocks_list.append(Block(x, 100, 60, 30, True, color_list[num_color]))
                        num_color += 1
                    
                          


#Создание игрока
gamer = Platform(300, 450, 100, 10, 50)

#Рисование шарика
ball = Ball(350, 440, 10, 0, 0)

n = 30
fall=False  
level=1
creatBlocks(level)
run = True
while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
            
                keyboard = pygame.key.get_pressed()
                buttons_mouse = pygame.mouse.get_pressed()
                pos_mouse = pygame.mouse.get_pos() 
                
                #Управление платформой
                if keyboard[pygame.K_LEFT]:
                        gamer.x -= gamer.speed
                if keyboard[pygame.K_RIGHT]:
                        gamer.x += gamer.speed
                #Запуск шарика
                if keyboard[pygame.K_SPACE]:
                        ball.vx=3
                        ball.vy=-3                         
                        fall=True                        
    
        screen.fill(color_bg)
            
        if PAGE == 'menu':
                button(x_button, y_button, width_button, height_button, 'Начать')
                button(x_button, y_button + 60, width_button, height_button, 'Помощь')
                button(x_button, y_button + 120, width_button,height_button, 'Выход') 
                    
                buttons_mouse = pygame.mouse.get_pressed()
                pos_mouse = pygame.mouse.get_pos()            
                    
                if pos_mouse[0]>x_button and pos_mouse[0]<x_button+width_button and pos_mouse[1]>y_button and pos_mouse[1]<y_button+height_button and buttons_mouse[0]:       
                        PAGE = 'game'
                        
                if pos_mouse[0]>x_button and pos_mouse[0]<x_button+width_button and pos_mouse[1]>y_button+60 and pos_mouse[1]<y_button+60+height_button and buttons_mouse[0]:       
                        PAGE = 'help'
                        
                if pos_mouse[0]>x_button and pos_mouse[0]<x_button+width_button and pos_mouse[1]>y_button+120 and pos_mouse[1]<y_button+120+height_button and buttons_mouse[0]:
                        PAGE = 'exit'                      
                        
        if PAGE == 'help':
                color_bg = 'white'
                    
                if keyboard[pygame.K_ESCAPE]:
                        PAGE = 'menu' 
                    
                font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
                text = font.render("                    ", 0, (255, 0, 0))
                dx = width_button//2 - text.get_width()//2
                screen.blit(text, (dx, 50)) 
                    
                font = pygame.font.SysFont('timesnewroman',20, bold = True, italic = False)
                text = font.render("Управление платформой:", 0, (255, 0, 0))
                dx = width//2 - text.get_width()//2
                screen.blit(text, (dx, 70))
                
                font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
                text = font.render("Чтобы запустить шарик, нужно нажать на ПРОБЕЛ", 0, (255, 0, 0))
                dx = width//2 - text.get_width()//2
                screen.blit(text, (dx, 90)) 
                
                font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
                text = font.render("Платформа управляется СТРЕЛКАМИ", 0, (255, 0, 0))
                dx = width//2 - text.get_width()//2
                screen.blit(text, (dx, 110))  
                
                font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
                text = font.render("Для победы нужно сбить все блоки", 0, (255, 0, 0))
                dx = width//2 - text.get_width()//2
                screen.blit(text, (dx, 130))  
                
                font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
                text = font.render("Если шарик платформой не отбить - то ты проиграл", 0, (255, 0, 0))
                dx = width//2 - text.get_width()//2
                screen.blit(text, (dx, 150)) 
                
                font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
                text = font.render("Удачи в игре!", 0, (255, 0, 0))
                dx = width//2 - text.get_width()//2
                screen.blit(text, (dx, 230))                      
                
        if PAGE == 'exit':
                run = False
                        
        if PAGE == 'game':
            
                if keyboard[pygame.K_ESCAPE]:
                        PAGE = 'menu'                       
        
                screen.fill('White') 
            
                for i in range(len(blocks_list)):
                        blocks_list[i].draw()
                
                gamer.draw()
                
                ball.draw()
                if fall:  
                        ball.x+=ball.vx
                        ball.y+=ball.vy
                else:   
                        ball.x = gamer.x+gamer.w/2
                if ball.y+ball.r>height:
                        ball.vy=0
                        ball.vx=0 
                
                if ball.y-ball.r<0:
                        ball.vy=-ball.vy              
                
                        
                if ball.x+ball.r>width or ball.x-ball.r<0:
                        ball.vx=-ball.vx           
                        
                if ball.x+ball.r>gamer.x and ball.x-ball.r<gamer.x+gamer.w and ball.y+ball.r>gamer.y and ball.y-ball.r<gamer.y+gamer.h:
                        ball.vy=-ball.vy
                        
                for i in range(len(blocks_list)):
                        if ball.x+ball.r>blocks_list[i].x and ball.x-ball.r<blocks_list[i].x+blocks_list[i].w and ball.y+ball.r>blocks_list[i].y and ball.y-ball.r<blocks_list[i].y+blocks_list[i].h and blocks_list[i].visible==True:
                                ball.vy=-ball.vy  
                                blocks_list[i].visible=False
                                n-=1
                if n==0:
                        n=8
                        ball.x = gamer.x+gamer.w/2
                        ball.y = 440
                        ball.vy=0
                        ball.vx=0
                        level=2
                        creatBlocks(level)
                
        
        pygame.display.flip()
        fpsClock.tick(60)
pygame.quit()            