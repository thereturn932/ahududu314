# -*- coding: utf-8 -*-
"""
Created on Thu May 10 23:01:11 2018

@author: User
"""
import pygame


pygame.init()

screen = pygame.display.set_mode((600,400))

while 1:
    pygame.event.get()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        print('sol')
    if keys[pygame.K_RIGHT]:
        print('sağ')