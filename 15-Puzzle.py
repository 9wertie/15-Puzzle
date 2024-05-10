import pygame
import time
import random


w, h = 410, 410
win = pygame.display.set_mode((w, h))
pygame.font.init() 
my_font = pygame.font.SysFont('Comic Sans MS', 50)

loc = [[[10,10,90,90],[110,10,90,90],[210,10,90,90],[310,10,90,90]],
       [[10,110,90,90],[110,110,90,90],[210,110,90,90],[310,110,90,90]],
       [[10,210,90,90],[110,210,90,90],[210,210,90,90],[310,210,90,90]],
       [[10,310,90,90],[110,310,90,90],[210,310,90,90],[310,310,90,90]]]

nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,14]
random.shuffle(nums)
map = [[0,0,0,0],
       [0,0,0,0],
       [0,0,0,0],
       [0,0,0,0]]

c=0
for i in range(4):
    for j in range(4):
        map[i][j]=nums[c]
        c+=1


def block(i,j,n):
    if n!=15:
        moraba = pygame.Rect(loc[i][j][0],loc[i][j][1],loc[i][j][2],loc[i][j][3]) # [i][j][0] = x [i][j][1] = y
        pygame.draw.rect(win , "white" , moraba)

        text_surface = my_font.render(str(n+1), 1, (0, 0, 0))
        win.blit(text_surface, (loc[i][j][0]+30,loc[i][j][1]+10))


def main():
    run = True
    busy_UP = False
    busy_DOWN = False
    busy_LEFT = False
    busy_RIGHT = False 
    winner = False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        reset = pygame.Rect(0,0,w,h)
        pygame.draw.rect(win , "black" , reset)
        
        for i in range(4):
            for j in range(4):
                block(i,j,map[i][j])

        pygame.display.update()

        zero_i, zero_j = 0, 0
        for i in range(4):
            for j in range(4):
                if map[i][j]==15:
                    zero_i = i
                    zero_j = j
                    #print(i,j)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and zero_j != 0 and busy_RIGHT == False:
            busy_RIGHT=True
            map[zero_i][zero_j-1], map[zero_i][zero_j] = map[zero_i][zero_j], map[zero_i][zero_j-1]
                
        
        elif keys[pygame.K_LEFT] and zero_j != 3 and busy_LEFT == False:
            busy_LEFT=True
            map[zero_i][zero_j+1], map[zero_i][zero_j] = map[zero_i][zero_j], map[zero_i][zero_j+1]


        elif keys[pygame.K_UP] and zero_i != 3 and busy_UP == False:
            busy_UP=True
            map[zero_i+1][zero_j], map[zero_i][zero_j] = map[zero_i][zero_j], map[zero_i+1][zero_j]


        elif keys[pygame.K_DOWN] and zero_i != 0 and busy_DOWN == False:
            busy_DOWN=True
            map[zero_i-1][zero_j], map[zero_i][zero_j] = map[zero_i][zero_j], map[zero_i-1][zero_j]
        
        if not(keys[pygame.K_DOWN]):
            busy_DOWN=False
        if not(keys[pygame.K_UP]):
            busy_UP=False
        if not(keys[pygame.K_LEFT]):
            busy_LEFT=False
        if not(keys[pygame.K_RIGHT]):
            busy_RIGHT=False


        c=0
        f=0
        for i in range(4):
            for j in range(4):
                if map[i][j] != c:
                    f+=1
                c+=1
        if f == 0:
            print('HOLY SHIT YOU DID IT!')
            run = False
            winner = True

    pygame.quit()

    while winner:
        print('HOLY SHIT YOU DID IT!')

if __name__ == "__main__":
    main()