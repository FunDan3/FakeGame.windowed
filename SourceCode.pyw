#I add comments but didnt 'recompile' exe file
#and I know pyinstaller puts interpretter in exe not compiling code!
import pygame
f=open("settings.pycon")#settings file. more about settings stuff at readme.md
config=f.read()
f.close()
config=eval(config)#make config readable
running = True
logo = pygame.image.load(config["Logo_path"])#Load logo (take logo path from settings)
screen = pygame.display.set_mode((1000, 1000))#create window
pygame.display.set_caption(config["Caption"])#Set window name (take name from settings)
pygame.display.set_icon(logo)#Set icon (already loaded)
while running:
    pygame.time.wait(100) #used to dont load cpu
    for event in pygame.event.get(): #check for events
      if event.type == pygame.QUIT: #on exit
        running = False #stop programm
