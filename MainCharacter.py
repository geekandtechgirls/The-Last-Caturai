#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""MainCharacter.py"""

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

"""Defines the main character of the game"""

from Character import Character

class MainCharacter(Character):
    def __init__(self, hp, position, sprite, is_girl):
        super(MainCharacter, self).__init__(hp, position, sprite)
        self.is_girl = is_girl
        self.sprite = sprite
        self.rect.x = position[0]
        self.rect.y = position[1]

    def attack(self):
        pass