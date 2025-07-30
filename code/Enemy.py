#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity

class Enemy(Entity):
  def __init__(self, name, position):
    super().__init__(name, position)

  def move(self, ):
    self.rect.centerx -= ENTITY_SPEED[self.name]
    if self.rect.right <= 0:
      self.rect.left = WIN_WIDTH