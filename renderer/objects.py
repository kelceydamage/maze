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
from renderer.colours import Colours
import pygame


# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->
class MenuObject:

    def __init__(self):
        self.text = ''
        self.header = ''
        self.is_list = False
        self.colour = Colours.white
        self.font = pygame.font.Font(None, 22)
        self.highlight = Colours.grey
        self.position = [0, 0]
        self.selected = False
        self.x_offset = 0
        self.y_offset = 0


class Menu:

    def __init__(self):
        self.width = 0
        self.height = 0
        self.position = [0, 0]
        self.background_colour = Colours.grey
        self.items = []


class BaseObject:

    def __init__(self): 
        self.menu_items = []

    def _new_menu_item(self, header, text, x_offset=0, y_offset=0):
        m = MenuObject()
        m.header = header
        m.text = text
        m.x_offset = x_offset
        m.y_offset = y_offset
        self.menu_items.append(m)


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
