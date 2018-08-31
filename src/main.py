import pygame 
import collisions
import math


class point : 
	isClosed =  False
	isOpen = False
	def __init__(self,x,y,endx,endy) :
		self.position = (x,y)
		self.H = abs(endx-x)+abs(endy-y)
		self.G = 10000000
		self.isObst = colmap.map[x][y]



def addopenSet(grid,i,j):
	if (i>1 and j>1 and i<799 and j < 499):
		for k in range(-1,2):
			for n in range (-1,2):
	
					if(grid[i+k][j+n].isClosed == False and grid[i+k][j+n].isObst == 0 and grid[i+k][j+n].isOpen == False ):
	
						openSet.append(grid[i+k][j+n])
	
						grid[i+k][j+n].isOpen = True
	
					if(grid[i+k][j+n].isOpen == True and abs(n)==abs(k) and k!=0):
	
						if grid[i][j].G+1.4<grid[i+k][j+n].G:
	
							grid[i+k][j+n].G = grid[i][j].G+1.4
	
							grid[i+k][j+n].parent = grid[i][j]
	
					if(grid[i+k][j+n].isOpen == True and abs(n)!=abs(k)):
	
						if grid[i][j].G+1<grid[i+k][j+n].G:
	
							grid[i+k][j+n].G = grid[i][j].G+1
	
							grid[i+k][j+n].parent = grid[i][j]

def pickFromOs(openSet,current):
	lowF = openSet[0]
	for i in range(len(openSet)):
		if (openSet[i].G+openSet[i].H<lowF.G+lowF.H):
			lowF = openSet[i] 
	current = lowF
	openSet.remove(current)
	return current

def drawParent(object):
	if hasattr(object, 'parent'):
		pygame.draw.rect(screen,(0,255,0),(object.position[0],object.position[1],1,1))
		drawParent(object.parent)
	return

fileName = input("Enter Filename:")

image = pygame.image.load("examples/"+fileName)

WIDTH = image.get_rect().size[0]
HEIGHT = image.get_rect().size[1]

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('Gzamkvlevi')

colmap = collisions.map(WIDTH,HEIGHT)

imageProc = collisions.imageArray(colmap,fileName,WIDTH,HEIGHT)


colmap = imageProc.colmap

start = imageProc.start
end = imageProc.end

openSet = []*WIDTH*HEIGHT
closedSet = []*WIDTH*HEIGHT

grid = [[0 for i in range(HEIGHT+5)] for j in range(WIDTH+5)]

for i in range(0,WIDTH):
	for j in range(0,HEIGHT):
		grid[i][j] = point(i,j,end[0],end[1])

current = grid[start[0]][start[1]]
current.G = 0
closedSet.append(current)
current.isClosed = True
current.isOpen = False
addopenSet(grid,start[0],start[1])

searchCond = True


windowclose = False

screen.blit(image,(0,0))

while not windowclose:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				windowclose = True
	if searchCond:
		current = pickFromOs(openSet,current)	

		closedSet.append(current)
		pygame.draw.rect(screen,(28,107,160),(current.position[0],current.position[1],1,1))

		current.isClosed = True
		current.isOpen = False

		addopenSet(grid,current.position[0],current.position[1])

		for i in openSet:
			pygame.draw.rect(screen,(255,255,0),(i.position[0],i.position[1],1,1))

	if(current.position[0] == end[0] and current.position[1] == end[1]):
		screen.blit(image,(0,0))
		drawParent(grid[end[0]][end[1]])
		searchCond = False
		
	pygame.draw.rect(screen,(255,0,0),(start[0],start[1],10,10))
	pygame.draw.rect(screen,(0,255,0),(end[0],end[1],10,10))
	pygame.display.update()
