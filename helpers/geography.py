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
from environment.regions import Region

# Import game world
from environment import World


# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->
class Geographer(BaseObject):

    def __init__(self):
        super(Geographer, self).__init__()
        #self.dimensions = dimensions
        self.current_region = Region()

    def add_content(self, location, content):
        """
        Args:
            location. z, x, y
        """
        if location not in self.entities[content[0]].keys():
            self.entities[content[0]][location] = {}
        index = len(self.entities[content[0]][location])
        self.entities[content[0]][location][index + 1] = content[1:]

    def del_content(self, location, _type, index):
        """
        Args:
            location. z, x, y
        """
        del self.entities[_type][location][index]

    def find_passable_terain(self, location):
        """
        Args:
            location. z, x, y
        """
        fil = np.add(location, CUBE_MASK)
        return [x for x in fil if World.passable[x[0], x[1], x[2]] == 1]

    def set_region_blocked(self, location, blocked=0):
        """
        Args:
            location. z, x, y
        """
        World.passable[location] = 0

    def is_region_blocked(self, location):
        """
        Args:
            location. z, x, y
        """
        return World.passable[location]

    def get_region_contents(self, location):
        """
        Args:
            location. z, x, y
        """
        if location not in self.entities['items'].keys():
            return {}
        return self.entities['items'][tuple(location)]

    def get_region_terrain(self, location):
        """
        Args:
            location. z, x, y
        """
        terrain = World.terrain[tuple(location)]
        return (World.region_types[terrain], terrain)

    def set_region_terrain(self, location, terrain):
        """
        Args:
            location. z, x, y
        """
        World.terrain[location] = terrain

    def get_region_resources(self, location):
        """
        Args:
            location. z, x, y
        """
        resources = World.resources[location]
        return [(x[1], y) for x, y in zip(World.resource_types.items(), resources.tolist())]

    def get_terrain_speed(self, c1, c2):
        return sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

    def valid_move(self, destination, cube_map):
        """
        Args:
            location. z, x, y
        """
        if destination in cube_map:
            return False
        return True

    def compile_selected_region(self):
        location = STATE.get_selected_region()
        print('GEO', location)
        self.current_region.terrain = self.get_region_terrain(location)
        self.current_region.items = self.get_region_contents(location)
        self.current_region.resources = self.get_region_resources(location)
        self.current_region.position = location

    def get_selected_region(self):
        return self.current_region


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
