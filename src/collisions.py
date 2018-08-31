import pygame
class map:
	def __init__(self,WIDTH,HEIGHT):
		self.map = [[0 for i in range(HEIGHT+5)] for j in range(WIDTH+5)]
		for i in range (0,WIDTH):
			self.map[i][0] = 1

class imageArray:
	def __init__(self,colmap,imagename,width,height):
		self.width = width
		self.height = height

		self.image = pygame.image.load('examples/'+imagename)
		self.pixels = pygame.surfarray.array2d(self.image)
		self.colmap = colmap
		for i in range(0,self.width):
			for j in range(0,self.height):
				if self.pixels[i][j] == self.image.map_rgb(0,0,0) :
					self.colmap.map[i][j] = 1
				if self.pixels[i][j] == self.image.map_rgb(255,0,0):
					self.start = (i,j)
				if self.pixels[i][j] == self.image.map_rgb(0,255,0):
					self.end = (i,j)
