import time
import random
import pygame
import threading


pygame.init()

screen = pygame.display.set_mode((800,600))

done =  False

x = 30
y = 30

flag= 0
flag2=0
flag3=0

f = 1


clock = pygame.time.Clock()


def resize_part():
    global wdt
    while True:
        #wdd = random.randint(30, 42)  # vertical
        wdt = random.randint(5, 400)  # horizontal
        time.sleep(1)  # Adjust the delay to control the speed of resizing


# Start a thread to resize the part
resize_thread = threading.Thread(target=resize_part)
resize_thread.daemon = True  # Set the thread as a daemon so it will stop when the program exits
resize_thread.start()

def level1():
    global pressed
    global box
    global w1
    global w2
    global w3
    global w4
    global f1
    global flag
    global x
    global y
    global f






    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -= 3
    if pressed[pygame.K_s]: y += 3
    if pressed[pygame.K_a]: x -= 3
    if pressed[pygame.K_d]: x += 3

    screen.fill((0, 0, 0))

    imp2 = pygame.image.load("ferrai.png").convert()
    #screen.blit(imp2, (0, 0))

    box1 = imp2.get_rect()
    box1.topleft = (x,y)
    pygame.draw.rect(screen, (162, 0, 255), box1)
    screen.blit(imp2, box1)

    #box1 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 60, 60))
    w1 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(0, 155, 200, 1000))
    w2 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(200, 500, 1000, 1000))
    w3 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(350, 0, 500, 200))
    w4 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(350, 170, 100, 200))

    #f1 = pygame.draw.rect(screen, (217, 33, 33), pygame.Rect(700, 200, 100, 100))

    imp3 = pygame.image.load("Finish.png").convert()
    f1 = imp3.get_rect()
    f1.topleft = (670, 200)
    pygame.draw.rect(screen, (162, 0, 255), f1)
    screen.blit(imp3, f1)

    Font2 = pygame.font.SysFont("comicsansms", 30, True, True)
    Title2 = Font2.render("lvl: 1", True, (0,0,0))
    screen.blit(Title2, (700, 10))

    if box1.colliderect(w1) == True:
        x = 30
        y = 30

    if box1.colliderect(w2) == True:
        x = 30
        y = 30

    if box1.colliderect(w3) == True:
        x = 30
        y = 30

    if box1.colliderect(w4) == True:
        x = 30
        y = 30

    if box1.colliderect(f1) == True:
        x = 30
        y = 30

        flag = 1

    if flag == 1:
        Font = pygame.font.SysFont("comicsansms", 70, True, True)
        Title = Font.render("You Finished!", True, (255, 255, 255))
        screen.blit(Title, (190, 350))
        f = 2

def level2():
    global l2pressed
    global l2box
    global l2w1
    global l2w2
    global l2w3
    global l2w4, l2w5
    global l2f1
    global flag
    global x
    global y
    global f
    global flag2

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -= 3
    if pressed[pygame.K_s]: y += 3
    if pressed[pygame.K_a]: x -= 3
    if pressed[pygame.K_d]: x += 3

    screen.fill((0, 0, 0))

    imp2 = pygame.image.load("ferrai.png").convert()
    #screen.blit(imp2, (0, 0))

    box1 = imp2.get_rect()
    box1.topleft = (x, y)
    pygame.draw.rect(screen, (162, 0, 255), box1)
    screen.blit(imp2, box1)

    #box1 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 60, 60))
    l2w1 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(0, 100, 500, 100))
    l2w2 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(200, 500, 1000, 1000))
    l2w3 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(650, 0, 700, 600))
    l2w4 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(350, 170, 100, 200))
    l2w5 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(100, 300, 100, 500))

    #l2f1 = pygame.draw.rect(screen, (217, 33, 33), pygame.Rect(0, 500, 100, 100))

    imp3 = pygame.image.load("Finish2.png").convert()
    l2f1 = imp3.get_rect()
    l2f1.topleft = (0, 530)
    pygame.draw.rect(screen, (162, 0, 255), l2f1)
    screen.blit(imp3, l2f1)

    l2Font2 = pygame.font.SysFont("comicsansms", 30, True, True)
    l2Title2 = l2Font2.render("lvl: 2", True, (0,0,0))
    screen.blit(l2Title2, (700, 10))

    if box1.colliderect(l2w1) == True:
        x = 30
        y = 30

    if box1.colliderect(l2w2) == True:
        x = 30
        y = 30

    if box1.colliderect(l2w3) == True:
        x = 30
        y = 30

    if box1.colliderect(l2w4) == True:
        x = 30
        y = 30

    if box1.colliderect(l2w5) == True:
        x = 30
        y = 30

    if box1.colliderect(l2f1) == True:
        x = 30
        y = 30

        flag2 = 1

    if flag2 == 1:
        Font = pygame.font.SysFont("comicsansms", 70, True, True)
        Title = Font.render("You Finished!", True, (255, 255, 255))
        screen.blit(Title, (190, 350))
        f = 3


def level3():
    global l3pressed
    global l3box
    global l3w1
    global l3w2
    global l3w3
    global l3w4, l3w5
    global l3f1
    global flag
    global x
    global y
    global f
    global flag3

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]: y -= 3
    if pressed[pygame.K_s]: y += 3
    if pressed[pygame.K_a]: x -= 3
    if pressed[pygame.K_d]: x += 3

    screen.fill((0, 0, 0))

    imp2 = pygame.image.load("ferrai.png").convert()
    #screen.blit(imp2, (0, 0))

    box1 = imp2.get_rect()
    box1.topleft = (x, y)
    pygame.draw.rect(screen, (162, 0, 255), box1)
    screen.blit(imp2, box1)


    #box1 = pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 60, 60))
    l3w1 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(0, 100, 600, 100))
    l3w2 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(200, 500, 1000, 1000))
    l3w3 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(100, 300, 700, 200))
    l3w4 = pygame.draw.rect(screen, (236, 0, 95), pygame.Rect(500, 85, wdt, 120))
    l3w5 = pygame.draw.rect(screen, (236, 238, 95), pygame.Rect(100, 300, 100, 500))

    #l3f1 = pygame.draw.rect(screen, (217, 33, 33), pygame.Rect(0, 500, 100, 100))

    imp3 = pygame.image.load("Finish2.png").convert()
    l3f1 = imp3.get_rect()
    l3f1.topleft = (0, 530)
    pygame.draw.rect(screen, (162, 0, 255), l3f1)
    screen.blit(imp3, l3f1)


    imp = pygame.image.load("mazeimg.png").convert()



    l3Font3 = pygame.font.SysFont("comicsansms", 30, True, True)
    l3Title3 = l3Font3.render("lvl: 3", True, (255, 255, 255))
    screen.blit(l3Title3, (700, 10))

    if box1.colliderect(l3w1) == True:
        x = 30
        y = 30

    if box1.colliderect(l3w2) == True:
        x = 30
        y = 30

    if box1.colliderect(l3w3) == True:
        x = 30
        y = 30

    if box1.colliderect(l3w4) == True:
        x = 30
        y = 30


    if box1.colliderect(l3w5) == True:
        x = 30
        y = 30


    if box1.colliderect(l3f1) == True:
        x = 30
        y = 30



        flag3 = 1

    if flag3 == 1:
        #Font = pygame.font.SysFont("comicsansms", 70, True, True)
        #Title = Font.render("You Finished!", True, (255, 255, 255))
        #screen.blit(Title, (190, 350))
        screen.blit(imp, (0, 0))
        f = 4


while done==False:
    for event in pygame.event.get():

        if event in pygame.event.get():
            done = True

    if f==1:
        level1()

    if f==2:
        level2()

    if f==3:
        level3()



    pygame.display.flip()
    clock.tick(60)









