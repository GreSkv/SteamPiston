import random 
import pygame
import time
pygame.init()


left = 50
top = 50
right =1700
bottom = 1500
n=50
maxv=50
pistony=150
pistonvy=0
pistonheight=301
xs = [random.randint(left, right) for i in range(n)]
ys = [random.randint(top, bottom) for i in range(n)]
vxs = [random.randint(-maxv, maxv) for i in range(n)]
vys = [random.randint(-maxv, maxv) for i in range(n)]
r = 10
colours= [random.randint (100, 200) for i in range(n)]
screen = pygame.display.set_mode((1800,1800))
running = True
while running:
    time.sleep(0.0001)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (20,20,20), pygame.Rect(left,top,right,bottom)) 
    pygame.draw.rect(screen, (150,100,0), pygame.Rect(left, pistony-pistonheight, right, pistonheight))
    pistony=pistony+pistonvy
    pistonvy=pistonvy+1
    if pistony>bottom:
        pistony=bottom
    for i, ( x, y, vx, vy, colour) in enumerate( zip(xs, ys, vxs, vys, colours)):
        pygame.draw.circle(screen,(2,colour,2), (x, y), r, r)
        x = x + vx
        y = y + vy +1/2
        vy = vy + 1
        if y<pistony and vy<0:
            vy=-vy
            pistonvy=pistonvy-vy/100
        if x > right and vx > 0:
            vx = -vx * 0.6
        if x < left and vx < 0:
            vx = -vx * 0.6
        if y > bottom and vy >= 0:
            if vy > 5:
                vy = -vy * 1.00
            else:
                vy = 0
            vx = vx * 1.00
        if y < 0 and vy < 0:
            vy = -vy
        xs[i]=x
        ys[i]=y
        vxs[i]=vx
        vys[i]=vy
    pygame.display.flip()

