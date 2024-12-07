import pygame
import math
import random
import colorsys
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
font = pygame.font.SysFont(None, 24)
k = 180/math.pi
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Rm = math.sqrt(SCREEN_HEIGHT**2 + SCREEN_WIDTH**2)/2
A = SCREEN_HEIGHT*SCREEN_WIDTH
no_of_extra_squares = A/900
screen_center = pygame.Vector2(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
screen_center2 = pygame.Vector2(SCREEN_WIDTH/2,-1*SCREEN_HEIGHT/2)

def arctan(y,x):
    t = math.atan2(y,x)
    if t<0:
        t = t + 2*math.pi
    else:
        pass
    return 2*math.pi -t

def colorlist(angle):
    color_tuple = colorsys.hsv_to_rgb(k*angle/360,1,1)
    color_list = []
    for i in color_tuple:
        color_list.append(i*255)
    return color_list




class hero(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center =(x,y)

    def update(self,enemy_pos):
        pos = pygame.Vector2(self.rect.center)
        B = enemy_pos-pos
        R = B.length()
        angle = math.atan2(B.y,B.x)
        angular_vel = 0.01
        x = 2*R*math.sin(angle + angular_vel)*math.sin(angular_vel)
        y = -2*R*math.sin(angular_vel)*math.cos(angle + angular_vel)
        
        if R <100:
            self.kill()
        else:
            #v = 30+((30*R)/Rm)
            v = 30
            self.rect.move_ip(v*math.cos(angle)+x,v*math.sin(angle)+y)
            
class hero2(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,20))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center =(x,y)

    def update(self,enemy_pos):
        pos = pygame.Vector2(self.rect.center)
        B = enemy_pos-pos
        R = B.length()
        angle = math.atan2(B.y,B.x)
        angular_vel = 0.01
        x = -2*R*math.sin(angle + angular_vel)*math.sin(angular_vel)
        y = 2*R*math.sin(angular_vel)*math.cos(angle + angular_vel)
        
        if R <50:
            self.kill()
        else:
            #v = 30+((30*R)/Rm)
            v = 30
            self.rect.move_ip(v*math.cos(angle)+x,v*math.sin(angle)+y)

class explosion_projectile(pygame.sprite.Sprite):
    def __init__(self, col, x, y,angle):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5,5))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle = angle

    def update(self,Sw,Sh):
        pos = pygame.Vector2(self.rect.center)
        relpos = pos - pygame.Vector2(Sw/2,Sh/2)
        Rs = relpos.length()
        angle = self.angle
        v = 20
        self.rect.move_ip(v*math.cos(angle),v*math.sin(angle))
        if Rs>Rm:
            self.kill()
            
running = True
#squares
squares1 = pygame.sprite.Group()
sqaures2 = pygame.sprite.Group()
evil_squares = pygame.sprite.Group()
Total_squares = 400
Total_explosion_squares = 100

w = math.pi/50
kills = 0
counter =0

while running:
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    mouse_pos2 = pygame.Vector2(mouse_pos.x,-1*mouse_pos.y)
    mouse_rel_center = mouse_pos2-screen_center2
    mouse_angle = arctan(mouse_rel_center.y,mouse_rel_center.x)
    colour_list = colorlist(mouse_angle)
    screen.fill((0,0,0))
    
    text = font.render(str(mouse_angle*k), True, (255,255,255))
    screen.blit(text, screen_center)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            angle2 =0
            for i in range(100):
                angle2 = angle2 + w
                evil_square = explosion_projectile(colour_list,mouse_pos.x,mouse_pos.y,angle2)
                evil_squares.add(evil_square)

            
    square_sprite_list = squares1.sprites()
    no_of_squares = len(square_sprite_list)
    for i in range(Total_squares-no_of_squares):
        angle= random.uniform(0,math.pi*2)
        if counter%2 ==0:
            square = hero(colour_list,Rm*math.cos(angle)+(SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+Rm*math.sin(angle))
            squares1.add(square)
        else:
            square = hero2(colour_list,Rm*math.cos(angle)+(SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+Rm*math.sin(angle))
            squares1.add(square)
        counter = counter +1
    if no_of_squares<no_of_extra_squares:
        for i in range(8):
            angle = random.uniform(0,math.pi*2)
            if counter%2 ==0:
                square = hero(colour_list,Rm*math.cos(angle)+(SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+Rm*math.sin(angle))
                squares1.add(square)
            else:
                square = hero2(colour_list,Rm*math.cos(angle)+(SCREEN_WIDTH/2),(SCREEN_HEIGHT/2)+Rm*math.sin(angle))
                squares1.add(square)
            counter = counter +1
    squares1.draw(screen)
    evil_squares.draw(screen)
    evil_squares.update(SCREEN_WIDTH,SCREEN_HEIGHT)
    squares1.update(mouse_pos)
    pygame.draw.line(screen,(255,255,255),(0,screen_center.y),(2*screen_center.x,screen_center.y))
    pygame.draw.line(screen,(255,255,255),(screen_center.x,0),(screen_center.x,screen_center.y*2))
    pygame.draw.line(screen,(255,255,255),screen_center,mouse_pos)
    t = pygame.sprite.groupcollide(squares1,evil_squares,True,False)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
