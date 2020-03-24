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
import configparser
import os


# Const
# ------------------------------------------------------------------------ 79->
CONFIG = configparser.ConfigParser()
CONFIG.readfp(open('{0}/config/main.cfg'.format(os.getcwd())))


# Classes
# ------------------------------------------------------------------------ 79->
class Config:
    fullscreen = CONFIG.getboolean('main', 'fullscreen')
    fullscreen_width = CONFIG.getint('main', 'fullscreen_width')
    fullscreen_height = CONFIG.getint('main', 'fullscreen_height')
    windowed_width = CONFIG.getint('main', 'windowed_width')
    windowed_height = CONFIG.getint('main', 'windowed_height')
    tile_width = CONFIG.getint('main', 'tile_width')
    map_width = CONFIG.getint('main', 'map_width')
    map_height = CONFIG.getint('main', 'map_height')
    frame_limit = CONFIG.getint('main', 'frame_limit')
    zlevels = CONFIG.getint('map', 'zlevels')
    images = str(CONFIG.get(
        'tiles', 'images{0}'.format(tile_width)
    )).split(', ')
    digimages = str(CONFIG.get(
        'tiles', 'digimages{0}'.format(tile_width)
    )).split(', ') 
    starting_coordinates = (
        CONFIG.getint('main', 'starting_z'),
        CONFIG.getint('main', 'starting_x'),
        CONFIG.getint('main', 'starting_y')
    )

# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
