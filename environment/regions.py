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
from renderer.objects import BaseObject


# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->
class Region(BaseObject):

    __slots__ = [
        'terrain',
        'items',
        'resources',
        'position',
        'menu_items'
    ]

    def __init__(self):
        super(Region, self).__init__()
        self.terrain = 0
        self.items = {}
        self.resources = []
        self.position = [0, 0, 0]

    def get_menu_items(self):
        self.menu_items = []
        self._new_menu_item('Terrain: ', self.terrain[0])
        self._new_menu_item('Items: ', len(self.items))
        self._new_menu_item('', '')
        self._new_menu_item('Resources: ', '')
        self._new_menu_item('', '')
        for r in self.resources:
            self._new_menu_item(
                '{0}: '.format(r[0]),
                r[1],
                x_offset=32
            )
        self._new_menu_item('', '')
        self._new_menu_item('Position: ', '')
        self._new_menu_item('', '')
        self._new_menu_item(
            'z={0}, x={1}, y={2}'.format(*self.position),
            '',
            x_offset=32
        )
        return self.menu_items

class Coastal(Region):
    index = 0

    def __init__(self):
        super(Coastal, self).__init__()
        self.precipitation_threshold = 0.5
        self.precipitation_growth_rate = 0.04
        self.fertility_growth_rate = -2
        self.sun_growth_rate = 0.07
        self.color = (0.4, 0.72, 0.7, 0.9)


class Beach(Region):
    index = 1

    def __init__(self):
        super(Beach, self).__init__()
        self.precipitation_threshold = 0.5
        self.precipitation_growth_rate = 0.02
        self.fertility_growth_rate = -0.05
        self.sun_growth_rate = 0.05
        self.color = (0.2, 0.3, 0.5, 99)


class Forest(Region):
    index = 2

    def __init__(self):
        super(Forest, self).__init__()
        self.precipitation_threshold = 0.6
        self.precipitation_growth_rate = 0.01
        self.fertility_growth_rate = 0.04
        self.sun_growth_rate = -0.02
        self.color = (0.2, 0.7, 0.5, 0.95)


class Grasslands(Region):
    index = 3

    def __init__(self):
        super(Grasslands, self).__init__()
        self.precipitation_threshold = 0.5
        self.precipitation_growth_rate = 0.01
        self.fertility_growth_rate = 0.03
        self.sun_growth_rate = 0.03
        self.color = (0.4, 0.8, 0.5, 0.95)


class Barren(Region):
    index = 4

    def __init__(self):
        super(Barren, self).__init__()
        self.precipitation_threshold = 0.9
        self.precipitation_growth_rate = 0.01
        self.fertility_growth_rate = -0.05
        self.sun_growth_rate = 0.04
        self.color = (0.9, 0.3, 0.5, 99)


class Hill(Region):
    index = 5

    def __init__(self):
        super(Hill, self).__init__()
        self.precipitation_threshold = 0.5
        self.precipitation_growth_rate = 0.02
        self.fertility_growth_rate = 0.01
        self.sun_growth_rate = 0.05
        self.color = (0.9, 0.3, 0.5, 99)


class Mountain(Region):
    index = 6

    def __init__(self):
        super(Mountain, self).__init__()
        self.precipitation_threshold = 0.5
        self.precipitation_growth_rate = 0.03
        self.fertility_growth_rate = 0
        self.sun_growth_rate = 0.06
        self.color = (0.7, 0.7, 0.5, 0.8)


class Ocean(Region):
    index = 99

    def __init__(self):
        super(Ocean, self).__init__()
        self.precipitation_threshold = 0.5
        self.precipitation_growth_rate = 0.04
        self.fertility_growth_rate = 0
        self.sun_growth_rate = 0.08
        self.color = (0.2, 0.4, 0.5, 99)


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
