#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level

class Game:
  def __init__(self):
    print('Setup Start')
    pygame.init()
    self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT), flags=pygame.RESIZABLE, vsync=True)
    print('Setup End')

  def run(self, ):
    while True:
      menu = Menu(self.window)
      menu_return = menu.run()

      if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
        level = Level(self.window, 'Level1', menu_return)
        level_return = level.run()
      elif menu_return == MENU_OPTION[4]:
        pygame.quit() # close window
        quit() # end pygame
      else:
        pass

      # Check for all events
      for event in pygame.event.get():
        if(event.type == pygame.QUIT):
          pygame.quit() # close window
          quit() # end pygame