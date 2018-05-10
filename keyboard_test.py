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
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            bRunning = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:    print('yukarı')
            if event.key == pygame.K_DOWN:  print('aşağı')
            if event.key == pygame.K_LEFT:  print('sol')
            if event.key == pygame.K_RIGHT: print('sağ')