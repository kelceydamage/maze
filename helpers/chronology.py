#! /usr/bin/env python
# ------------------------------------------------------------------------ 79->
# Author: ${name=Kelcey Damage}
# Python: 3.5+
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Doc
# ------------------------------------------------------------------------ 79->
"""
This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::

        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:
    module_level_variable1 (int): Module level variables may be documented in
        either the ``Attributes`` section of the module docstring, or in an
        inline docstring immediately following the variable.

        Either form is acceptable, but the two should not be mixed. Choose
        one convention to document module level variables and be consistent
        with it.

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

"""


# Imports
# ------------------------------------------------------------------------ 79->
import pygame
from renderer.objects import BaseObject

# Import game world
from environment import World


# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->
class Chronologist(BaseObject):

    __slots__ = [
        'clock',
        'hours'
        'day',
        'month',
        'year',
        'y_offset',
        '_elapsed_time'
    ]

    def __init__(self):
        super(Chronologist, self).__init__()
        self.clock = pygame.time.Clock()
        self.hours = 0
        self.day = 1
        self.month = 12
        self.year = 1307
        self.y_offset = 840
        self._elapsed_time = 0

    def increment_time(self):
        self.hours += 1
        if self.hours > 23:
            self.day += 1
            self.hours = 0
            if self.day > 30:
                self.month += 1
                self.day = 1
                if self.month > 12:
                    self.year += 1
                    self.month = 1
            self._elapsed_time += 1

    @property
    def elapsed_time(self):
        return self._elapsed_time

    def get_datetime(self):
        return (self.hours, self.day, self.month, self.year)

    def get_menu_items(self):
        self.menu_items = []
        self._new_menu_item('Date: ', '', y_offset=self.y_offset)
        self._new_menu_item('', '', y_offset=self.y_offset)
        self._new_menu_item(
            '{0} / {1} / {2}'.format(*self.get_time()),
            '',
            x_offset=32,
            y_offset=self.y_offset
        )
        self._new_menu_item('', '', y_offset=self.y_offset)
        self._new_menu_item('FPS', self.clock.get_fps(), y_offset=self.y_offset)
        return self.menu_items


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
