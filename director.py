#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""director.py"""

"""
This file is part of The Last Caturai.

    The Last Caturai is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    The Last Caturai is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""

"""Class Director, it contains the game loop, and manages events."""

import pygame
import config
import Character
from pygame.locals import *

class Director:

    def __init__(self):
        infoScreen = pygame.display.Info()
        self.screen = pygame.display.set_mode((infoScreen.current_w, infoScreen.current_h), RESIZABLE)
        pygame.display.set_caption(config.name)
        self.scene = None
        self.quit_flag = False
        self.clock = pygame.time.Clock()

    def loop(self):
        """Starts the game"""

        seconds = 0

        while not self.quit_flag:
            self.time = self.clock.tick(60)

            # Exit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == VIDEORESIZE:
                    self.scene.on_resize(self.screen, event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        Character.jump()

            # Event detection
            self.scene.on_event()

            # Scene update
            self.scene.on_update()

            # Draws scene
            seconds += self.time
            self.scene.on_draw(self.screen, seconds)
            pygame.display.flip()

    def change_scene(self, scene):
        """Updates actual scene"""
        self.scene = scene

    def quit(self):
        self.quit_flag = True
