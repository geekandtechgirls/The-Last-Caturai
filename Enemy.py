#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""enemy.py"""

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

"""It defines the general enemies of the game."""


import os
import config
import pygame
from Character import Character
from Shuriken import Shuriken

class Enemy(Character):
    def __init__(self, hp, position, sprite):
        super(Enemy, self).__init__(hp, position, sprite)
        self.movimientos = self._cortar_chara(fil=2)
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.direction = 'I'
        self.attacking = False
        # self.image = self.movimientos[self.direction][0]
        self.damage_umbral = 5
        self.shuriken = Shuriken(img_path=os.path.abspath(config.sprites + config.shuriken_sprite), position=(self.position[0]-25,self.position[1]))

    # def _cortar_chara(self, fil):
    #     # La idea de esta función es devolver una tupla con cuatro vectores:
    #     #       * sprites de movimiento hacia la izquierda
    #     #       * sprites de movimiento hacia la derecha
    #     #       * sprites de movimiento hacia arriba
    #     #       * sprites de movimiento hacia abajo
    #     abajo = []
    #     arriba = []
    #     dcha = []
    #     izq = []
    #
    #     for i in range(fil):
    #         abajo.append(self.image.subsurface((i * 35, 0, 32, 32)))
    #         izq.append(self.image.subsurface((i * 35, 35, 32, 32)))
    #         dcha.append(self.image.subsurface((i * 35, 75, 32, 32)))
    #         arriba.append(self.image.subsurface((i * 35, 105, 32, 32)))
    #
    #     return ({'A': abajo, 'U': arriba, 'D': dcha, 'I': izq})


    def attack(self, player, screen):
        self.attacking = True
        self.shuriken.draw(screen)
        diff = self.shuriken.position[0] - player.position[0]
        if  diff != self.damage_umbral or player.position[1] != self.position[1]:
            self.shuriken.move_left()
            self.shuriken.update()
            if self.shuriken.position[0] == 0:
                self.shuriken.stop_moving()
                pygame.sprite.Sprite.kill(self.shuriken)
                self.shuriken = Shuriken(img_path=os.path.abspath(config.sprites + config.shuriken_sprite),
                                         position=(self.position[0] - 25, self.position[1]))
        else:
            self.attacking = False
            self.shuriken.stop_moving()
            pygame.sprite.Sprite.kill(self.shuriken)
            self.shuriken = Shuriken(img_path=os.path.abspath(config.sprites + config.shuriken_sprite),
                                     position=(self.position[0] - 25, self.position[1]))

            player.hp -= 25
            shuriken_sound = pygame.mixer.Sound(
                os.path.abspath(config.sounds + config.shuriken_sound))
            shuriken_sound.play()


    def movement(self):
        pass
