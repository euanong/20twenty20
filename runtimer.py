import time
import random
import libs.ptext as ptext
import sys
import pygame

ptext.DEFAULT_FONT_NAME = "data/Roboto-Light.ttf"

def runTimer(time,quotefile,escapable,fontsize):
	pygame.init()
	try:
		pygame.mouse.set_visible(False)
		screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		w, h = screen.get_size()
		done = False
		timeMS = time*1000
		startTime = pygame.time.get_ticks()
		lines = open(quotefile).read().splitlines()
		quote = random.choice(lines)
		while not done:
			now = pygame.time.get_ticks()
			delta = now-startTime
			if delta>=timeMS:
				break
			for event in pygame.event.get():
				if escapable:
					if event.type == pygame.QUIT:
						done = True
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							done = True
			screen.fill((255, 255, 255))
			time = ""
			if 20-int(delta/1000)==1:
				time="1 second"
			else:
				time=str(20-int(delta/1000))+" seconds"
			#text_to_screen(screen,"Take a break to help prevent eye strain.",w/2,h/3,fontsize)
			ptext.draw("Take a break to help prevent eye strain.\nLook at something 20 feet away for "+time+".",midtop=(w/2,h/3),fontsize=fontsize,align="center",color="black")
			#text_to_screen(screen,quote,w/2,h/2,fontsize)
			ptext.draw(quote,midtop=(w/2,h/2),fontsize=fontsize,width=w*4/5,align="center",color="black")
			pygame.display.update()
	finally:
		pygame.quit()

if __name__ == '__main__':
	runTimer(int(sys.argv[1]),sys.argv[2],sys.argv[3]==True,int(sys.argv[4]))