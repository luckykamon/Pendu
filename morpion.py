import time
import sys
import pygame
from pygame.locals import *
from random import randint


pygame.init()
window = pygame.display.set_mode((648, 604), RESIZABLE)


def initialisation(): #choice beetween play or help
  window.blit(pygame.image.load("start.png").convert(), (0, 0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if 489 > event.pos[1]:
            morpion()
          if 488 < event.pos[1]:
            help()
      if event.type == KEYDOWN:
        morpion()

def help(): #display help
  window.blit(pygame.image.load("help.png").convert(), (0, 0))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        initialisation()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          initialisation()

def menu(): #choice beetween replay or go start
  window.blit(pygame.image.load("white.png").convert(), (580, 542)) #remove the next player
  pygame.display.flip()
  time.sleep(1.5)
  window.blit(pygame.image.load("menu.png").convert(), (230, 200))
  pygame.display.flip()
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if 200 < event.pos[1] < 239:
            if 230 < event.pos[0] < 364:
              initialisation()
            if 364 < event.pos[0] < 498:
              morpion()
      if event.type == KEYDOWN:
        if event.key == K_KP0:
          initialisation()
        if event.key == K_KP1:
          morpion()

def morpion():
  window.blit(pygame.image.load("tray.png").convert(), (0, 0))
  background = [0, 0, 0, 0, 0, 0, 0, 0, 0] #0=no pion, 1=dagger, 2=round
  player = randint(1, 2) #player who begining, 1=dagger, 2=round
  if player == 1:
    window.blit(pygame.image.load("tdagger.png").convert(), (580, 542))
  else:
    window.blit(pygame.image.load("tround.png").convert(), (580, 542))
  pygame.display.flip()
  n = 0
  while True:
    case = selectcase()
    if background[case] == 0: #if the case don't have pion
      n += 1
      background[case] = player
      case = (37 + (case % 3) * 199, 361 - (case / 3) * 178) #position of pion
      w = winner(background) #1=dagger win, 2=round win, 3=equality
      if player == 1: #display and change the player
        window.blit(pygame.image.load("dagger.png").convert(), case)
        player=2
        window.blit(pygame.image.load("tround.png").convert(), (580, 542))
      else: #display and change the player
        window.blit(pygame.image.load("round.png").convert(), case)
        player=1
        window.blit(pygame.image.load("tdagger.png").convert(), (580, 542))
      pygame.display.flip()
      if n > 4: #before we can't have a winner
        if w == 1:
          window.blit(pygame.image.load("gdagger.png").convert(), (200, 542))
          menu()
        if w == 2:
          window.blit(pygame.image.load("ground.png").convert(), (200, 542))
          menu()
        if w == 3:
          window.blit(pygame.image.load("equality.png").convert(), (230, 542))
          menu()

def selectcase(): #player select a case
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          if 355 < event.pos[1] < 540:
            if 9 < event.pos[0] < 220:
              return 0
            if 226 < event.pos[0] < 419:
              return 1
            if 425 < event.pos[0] < 636:
              return 2
          if 180 < event.pos[1] < 350:
            if 9 < event.pos[0] < 220:
              return 3
            if 226 < event.pos[0] < 419:
              return 4
            if 425 < event.pos[0] < 636:
              return 5
          if 7 < event.pos[1] < 175:
            if 9 < event.pos[0] < 220:
              return 6
            if 226 < event.pos[0] < 419:
              return 7
            if 425 < event.pos[0] < 636:
              return 8
      if event.type == KEYDOWN:
        if event.key == K_KP1:
          return 0
        if event.key == K_KP2:
          return 1
        if event.key == K_KP3:
          return 2
        if event.key == K_KP4:
          return 3
        if event.key == K_KP5:
          return 4
        if event.key == K_KP6:
          return 5
        if event.key == K_KP7:
          return 6
        if event.key == K_KP8:
          return 7
        if event.key == K_KP9:
          return 8

def winner(b): #return 1 or 2 if we have a winner else 0
  if b[0] == b[1] == b[2] and b[0] != 0:
    l = b[0]
    return l
  if b[3] == b[4] == b[5] and b[3] != 0:
    l = b[3]
    return l
  if b[6] == b[7] == b[8] and b[6] != 0:
    l = b[6]
    return l
  if b[0] == b[3] == b[6] and b[0] != 0:
    l = b[0]
    return l
  if b[1] == b[4] == b[7] and b[1] != 0:
    l = b[1]
    return l
  if b[2] == b[5] == b[8] and b[2] != 0:
    l = b[2]
    return l
  if b[0] == b[4] == b[8] and b[4] != 0:
    l = b[4]
    return l
  if b[2] == b[4] == b[6] and b[4] != 0:
    l = b[4]
    return l
  if b[0] != 0 and b[1] != 0 and b[2] != 0 and b[3] != 0 and b[4] != 0 and b[5] != 0 and b[6] != 0 and b[7] != 0 and b[8] != 0:
    return 3
  return 0

#To leave at the end
initialisation()
