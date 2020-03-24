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
from environment import World
import numpy as np

import time
# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->
class Weather:
    state = None

    # daily compound growth occurs until a random number falls under the value
    # at which point decay sets in until the weather changes again. Various
    # factors can impact growth and decay, such as seasonal trends, and land
    # variability.

    def check_state(self, simulation, date):
        # update precipitation in all regions
        growth = simulation.get_precipitation(date, 1)
        World.precipitation = np.multiply(
            World.precipitation,
            growth * 1
        )
        #World.precipitation[World.precipitation < 0.5]
        # determine if rain starts in a given region
        test = np.random.randint(100) / 100 + 0.02

        # update rain map to show which regions are raining
        World.rain[World.precipitation > test] = 1

        # Process decay conditions
        decay = simulation.get_precipitation_decay(date, 1)
        World.precipitation[(World.precipitation > 0.5) & (World.rain == 1)] = np.random.random(1) / 2
        World.precipitation[(World.precipitation > test) & (World.rain == 1)] /= (1 + (decay))
        World.precipitation[(World.precipitation < 0.3) & (World.rain == 0)] /= (1 + (decay / 4))
        World.rain[(World.precipitation < 0.35) & (World.rain == 1)] = 0


        


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
