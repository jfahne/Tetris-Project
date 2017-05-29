#import statements
import pygame

class TetrisMain:
  #Main Class where initializations occur
  
  def __init__(self)
  
    #Initialize pygame
    
    pygame.init()
    
    
    #Window dimensions
    
    self.width = 900
    
    self.height = 1800
    
    
    #Create Window
    
    self.screen = pygame.display.set_mode( ( self.width, self.height ) )
    
    
    
