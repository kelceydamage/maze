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
from environment.assets import Assets
from environment.cursor import Cursor
from utils.config import Config
#from renderer.scaffolding import SCAFFOLDING


# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->
class WorldState:
    grow = True

    def __init__(self):
        self.sun = Sun()
        self.precipitation = Precipitation()

class State(Assets):

    def __init__(self):
        super(State, self).__init__()
        self.map_origin = [0, 0]
        self.starting_coordinates = (0, 0)
        self.selected_region = [0, 0, 0]
        self.viewport_origin = [0, 0, 0]
        self.viewport_z = 0
        self.viewport_x = 0
        self.viewport_y = 0
        self.select_mode = False
        self.show_menu = False
        self.paused = False
        self.quit = False
        self.save = False
        self.load = False
        self.edit_mode = [None, None]
        self.z = 5
        #self.cursor = Cursor(
        #    Config.tile_width, SCAFFOLDING.horizontal_tile_count // 2 * Config.tile_width,
        #    SCAFFOLDING.vertical_tile_count // 2 * Config.tile_width
        #)
        #self._set_intial_viewport()

    def _set_intial_viewport(self):
        """
        x = (Config.map_width - SCAFFOLDING.horizontal_tile_count) // 2
        y = (Config.map_width - SCAFFOLDING.vertical_tile_count) // 2
        self.shift_view([5, x, y])
        """
        pass

    def shift_view(self, origin):
        """
        # in terms of map indices
        if -1 not in origin:
            self.viewport_origin = origin
        self.viewport_z = origin[0]
        if 0 <= origin[1] <= Config.map_width - SCAFFOLDING.horizontal_tile_count:
            self.viewport_x = origin[1]
        if 0 <= origin[2] <= Config.map_height - SCAFFOLDING.vertical_tile_count:
            self.viewport_y = origin[2]
        """
        pass

    def idle_dwarves(self):
        counter = 0
        for mo in self.mobs:
            if mo.job == None:
                counter = counter + 1
        return counter

    def set_flag(self, flag):
        """
        if len(flag) == 3:
            toggle = not getattr(self, flag[0])
            setattr(self, flag[0], toggle)
        else:
            setattr(self, flag[0], flag[1])
        """
        pass

    def get_selected_region(self):
        #return tuple([int(x) for x in self.selected_region])
        return None


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
STATE = State()