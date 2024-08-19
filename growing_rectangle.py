import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill("white")
pygame.display.update()

class Rectangle():
    def __init__(self, color, dimensions):
        self.rect_color = color
        self.rect_dimesions = dimensions
        self.rect_surface = screen
    def draw(self):
        self.Draw_Rect = pygame.draw.rect(self.rect_surface, self.rect_color, self.rect_dimesions)
    def grow(self, r):
        self.rect_dimesions += r
        self.Draw_Rect = pygame.draw.rect(self.rect_surface, self.rect_color, self.rect_dimesions)
r = Rectangle("green", (50, 20, 100, 100))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            r.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            r.grow(20)
            pygame.display.update()
        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            r2 = Rectangle("red", (300, 400, 200, 200))
                           
            r2.draw()
            pygame.display.update()
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()