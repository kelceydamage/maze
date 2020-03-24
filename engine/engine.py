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
import time

# Helpers
import helpers

# Global state
from environment import World

# Simulation
from environment.simulation import EnvironmentalSimulation

# Rendering
from renderer.p3drenderer import Renderer
from renderer.p3drenderer import Picker

# Configuration
from utils.config import Config

# remote compute
from rtl.common.transform import Transform


# Const
# ------------------------------------------------------------------------ 79->
'''
FLAGS = {
    ord('k'): ('show_menu', True, 'toggle'),
    ord('l'): ('load', True),
    ord('s'): ('save', True),
    K_ESCAPE: ('quit', True),
    K_SPACE: ('paused', True, 'toggle')
}
EDITORS = {
    ord('d'): ['designate', 'mining'],
    ord('h'): ['designate', 'channel'],
    ord('i'): ['designate', 'drop'],
    ord('o'): ['designate', 'itemselect'],
    ord('x'): ['designate', 'remove'],
}
'''

# Classes
# ------------------------------------------------------------------------ 79->
class Engine:

    def __init__(self):
        super(Engine, self).__init__()
        self.renderer = Renderer() # disambiguate Scene
        self.transform = Transform()
        self.simulation = EnvironmentalSimulation()
        self.running = True # Possible pause use
        self.frame_limit = Config.frame_limit  # Figure out how to implement this in OGL

    def run_simulation(self, date):
        self.simulation.generate_precipitation(date)
        self.simulation.generate_precipitation_decay(date)
        self.simulation.generate_sun(date)
        self.simulation.generate_fertility(date)

    def update_world(self):
        t = time.perf_counter()
        date = helpers.chronologist.get_datetime()
        self.run_simulation(date)
        #print('SIM', time.perf_counter() - t)
        helpers.meteorologist.get_weather(self.simulation, date)
        # Run simulations
        if date[1] == 30 and date[2] == 12:
            self.simulation.roll_over_year()
        # Collect all asset updates
        return date

    def handle_events(self):
        pass

    def pause_game(self):
        pass

    def run(self):
        #self.mousePicker = Picker()
        #self.mousePicker.makePickable(self.renderer.GUI.mapView.mapView)
        while True:
            # Figure out logging
            
            # Implement pause
            if self.renderer.GUI.showPause:
                time.sleep(0.05)
            else:

                # Retrieve inputs and/or actions from renderer.window

                # Process actions
                #print(helpers.geographer.get_region_terrain((1, 1, 1)))
                if base.mouseWatcherNode.hasMouse():
                    x = base.mouseWatcherNode.getMouseX()
                    y = base.mouseWatcherNode.getMouseY()
                    self.renderer.updateCoordinates(x, y)
                # Update world
                date = self.update_world()

                maps = {
                    0: (World.terrain, 100, World.terrainColorSpace),
                    1: (World.rain, 1, World.terrainColorSpace),
                    2: (World.precipitation, 0.35, World.terrainColorSpace),
                    3: (World.sun, 0.5, World.terrainColorSpace),
                }
                self.renderer.updateMapView(maps[self.renderer.GUI.layer])
                self.renderer.updateTime(date)

                if self.renderer.GUI.regen:
                    World.regen()
                    self.renderer.GUI.regen = False

                # Update scene

                helpers.chronologist.increment_time()
            taskMgr.step()


    '''
    def handle_mouse_events(self, event):
        if event.type == VIDEORESIZE:
            VIEW.resize(event.w, event.h)
        elif event.type == MOUSEBUTTONDOWN:
            self.cartographer.set_region_location(event.pos)

    def handle_keyboard_events(self, event):
        if event.type == QUIT:
            STATE.quit = True
        elif event.type == KEYDOWN:
            self.stateful_keypress_events(event)
            self.update = self.navigation_events(event)
            print('UPDATE', self.update)

    def stateful_keypress_events(self, event):
        if event.key in EDITORS.keys():
            STATE.edit_mode = EDITORS[event.key]
            STATE.paused = True
        if event.key in FLAGS.keys():
            STATE.set_flag(FLAGS[event.key])
    '''
    
# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->


