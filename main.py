#---------------------------------------------------------
#문제1: (1-(x**2/a))**(1/2)의 허수화
#문제2: planet_x,y의 복소수화
#---------------------------------------------------------
import pygame
from sympy import Symbol,solve
import time
#---------------------------------------------------------
pygame.init()
BLACK=(0,0,0)
WHITE=(255,255,255)
BLUE=(0,0,255)
GREEN=(0,255,0)
RED=(255,0,0)
screen_w=800
screen_h=800
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption("P")
clock = pygame.time.Clock()
#---------------------------------------------------------
ellipse_w=1.496*10**2*5
ellipse_h=1.495*10**2*5

a=ellipse_w/2
b=ellipse_h/2
c=(a**2-b**2)**(1/2)

ellipse_x=screen_w/2-a
ellipse_y=screen_h/2-b

star_x=ellipse_x+a-c
star_y=ellipse_y+b

planet_x=screen_w/2
planet_y=screen_h/2-b

ds=500#단위면적
dt=0.1#단위시간
#---------------------------------------------------------
def draw_ellipse():
  pygame.draw.ellipse(screen, WHITE, [ellipse_x, ellipse_y, ellipse_w, ellipse_h], 1)
def draw_star():
  pygame.draw.circle(screen, RED, [star_x, star_y], 5)
def draw_planet():
  #print(planet_x,planet_y)
  pygame.draw.circle(screen, BLUE, [int(planet_x),int(planet_y)], 3)
def draw():
  screen.fill(BLACK)
  draw_ellipse()
  draw_star()
  draw_planet()
#---------------------------------------------------------
running=True
while running:
#---------------------------------------------------------
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
#---------------------------------------------------------
    st=time.time()
# ---------------------------------------------------------
    draw()
    draw_ellipse()
    draw_star()
    draw_planet()
#---------------------------------------------------------
    mpx = Symbol('mpx')
    mpy1=((b**2 * (1 - ((mpx - 400) ** 2 / a**2))) ** (1 / 2)) + 400
    mpy2=-1*((b**2 * (1 - ((mpx - 400) ** 2 / a**2))) ** (1 / 2)) + 400
    if planet_y<400:
      mpy=mpy2
      #print(mpy)
    elif planet_y>400:
      mpy=mpy1
      #print(mpy)
    k=((star_x * planet_y + planet_x * mpy + star_y * mpx) -(star_y * planet_x + planet_y * mpx + star_x * mpy))
    #print((1/2)*abs(k))
    eq =(k**2)-(4*(ds**2))

    re = solve(eq)
#---------------------------------------------------------
    if time.time()-st>0:
      #반시계 방향 회전/x값이 작아지는게 0/
      if planet_y<399:
        planet_x=re[0]
        #planet_y = re[0]
        planet_y=-1*((1-((planet_x-400)**2/a**2))*b**2)**(1/2)+400
        print("위",planet_x,planet_y)
      elif planet_y>399:
        planet_x=re[1]
        #planet_y = re[0]
        planet_y=((1-((planet_x-400)**2/a**2))*b**2)**(1/2)+400
        print("아래", planet_x, planet_y)
#---------------------------------------------------------
    pygame.display.update()
    clock.tick(60)
