#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

class Game:
  def __init__(self):
    print('Setup Start')
    pygame.init()
    self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT), flags=pygame.RESIZABLE)
    print('Setup End')

  def run(self, ):
    while True:
      menu = Menu(self.window)
      menu_return = menu.run()

      # Check for all events
      for event in pygame.event.get():
        if(event.type == pygame.QUIT):
          pygame.quit() # close window
          quit() # end pygame