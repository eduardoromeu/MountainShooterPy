import pygame

# C
C_ORANGE = (255, 120, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_BLUE = (0, 0, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
  'Level1Bg0': 0,
  'Level1Bg1': 1,
  'Level1Bg2': 2,
  'Level1Bg3': 3,
  'Level1Bg4': 4,
  'Level1Bg5': 5,
  'Level1Bg6': 6,
}

# M
MENU_OPTION = ('NEW GAME 1P', 
              'NEW GAME 2P - COOPERATIVE',
              'NEW GAME 2P - COMPETITIVE',
              'SCORE',
              'EXIT')

# S
SPAWN_TIME = 4000

# T
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 20000  # 20s

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
