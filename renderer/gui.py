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
import sys
from direct.showbase.ShowBase import DirectObject
from direct.gui.DirectGui import DirectFrame
from panda3d.core import *
from renderer.render_scaling import Scaling
from renderer.gui_objects import MenuBar
from renderer.gui_objects import MapView
from renderer.render_utils import findMethods
from environment import World


# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->
class MainGUI(DirectObject.DirectObject):

    def __init__(self):
        self.scaling = Scaling()
        self.layer = 0
        self.regen = False
        self.showMenu = True
        self.showPause = False
        self.showMap = False
        self.pauseBar = DirectFrame(
            frameColor=(0.22/2, 0.24/2, 0.32/2, 1),
            frameSize=(0, base.win.getXSize(), 0, self.scaling.getVerticalDisplayRatio(25)),
            pos=(0, -1, -self.scaling.getVerticalDisplayRatio(25)),
            parent=pixel2d
        )
        header = TextNode('paused')
        header.setText('Paused')
        header.setTextColor(1, 1, 1, 1)
        header.setAlign(TextNode.ACenter)
        header.setTextScale(30)
        self.pauseTextNodePath = self.pauseBar.attachNewNode(header)
        self.pauseTextNodePath.setPos(base.win.getXSize()/2, 0, -5)

        self.footer = DirectFrame(
            frameSize=(0, base.win.getXSize(), 0, 24),
            pos=(0, -1, -base.win.getYSize()),
            parent=pixel2d
        )
        #findMethods(self.footer, 'set')

        self.pauseBar.hide()

        self.coords = TextNode('coords')
        self.coords.setText('coords:    _x     _y     _z')
        self.coords.setTextColor(0, 0, 0, 1)
        self.coords.setAlign(TextNode.ARight)
        self.coords.setTextScale(15)
        self.coordsTextNodePath = self.footer.attachNewNode(self.coords)
        self.coordsTextNodePath.setPos(base.win.getXSize() - 10, 0, 5)

        self.time = TextNode('time')
        self.time.setText('time:    _x     _y     _z')
        self.time.setTextColor(0, 0, 0, 1)
        self.time.setAlign(TextNode.ALeft)
        self.time.setTextScale(15)
        self.timeTextNodePath = self.footer.attachNewNode(self.time)
        self.timeTextNodePath.setPos(10, 0, 5)

        pixel2d.setAntialias(AntialiasAttrib.MMultisample)
        self.menubar = MenuBar()
        self.mapView = MapView()
        self.registerEvents()
        self.registerMouseClickEvents()

    def registerEvents(self):
        self.accept('window-event', self.onWindowEvent)
        self.accept('escape', self.exitProgram)
        self.accept('q', self.toggleMenu)
        self.accept('m', self.toggleMap)
        self.accept('l', self.cycleLayers)
        self.accept('space', self.togglePause)
        self.accept('w', self.shiftMapUp)
        self.accept('s', self.shiftMapDown)
        self.accept('a', self.shiftMapLeft)
        self.accept('d', self.shiftMapRight)

    def registerMouseClickEvents(self):
        findMethods(self.menubar.btnQuit, 'func')
        self.menubar.btnQuit['command'] = self.exitProgram
        self.mapView.btnLayers['command'] = self.cycleLayers
        self.menubar.btnMaps['command'] = self.setRegen

    def shiftMapUp(self):
        if self.mapView.origin[1] > 0:
            self.mapView.origin[1] -= 1
        print(self.mapView.origin)

    def shiftMapDown(self):
        if self.mapView.origin[1] >= 0:
            self.mapView.origin[1] += 1
        print(self.mapView.origin)

    def shiftMapLeft(self):
        if self.mapView.origin[0] > 0:
            self.mapView.origin[0] -= 1
        print(self.mapView.origin)

    def shiftMapRight(self):
        if self.mapView.origin[0] >= 0:
            self.mapView.origin[0] += 1
        print(self.mapView.origin)

    def setRegen(self):
        self.regen = True
        
    def toggleMenu(self):
        self.showMenu = not self.showMenu
        if self.showMenu:
            self.menubar.menubar.show()
        else:
            self.menubar.menubar.hide()

    def togglePause(self):
        self.showPause = not self.showPause
        if self.showPause:
            self.pauseBar.show()
        else:
            self.pauseBar.hide()

    def toggleMap(self):
        self.showMap = not self.showMap
        if self.showMap:
            self.mapView.mapView.show()
        else:
            self.mapView.mapView.hide()

    def onWindowEvent(self, window):
        self.pauseBar['frameSize'] = (0, window.size[0], 0, self.scaling.getVerticalDisplayRatio(25))
        self.footer['frameSize'] = (0, window.size[0], 0, self.scaling.getVerticalDisplayRatio(25))
        self.footer.setZ(-window.size[1])
        self.pauseTextNodePath.setPos(base.win.getXSize()/2, 0, -5)
        self.coordsTextNodePath.setPos(base.win.getXSize() - 10, 0, 5)
        self.mapView.mapView.setPos(
            base.win.getXSize() - self.mapView.xDim - 1, -1, -base.win.getYSize() + self.mapView.vOffset
        )

    def exitProgram(self):
        sys.exit()

    def cycleLayers(self):
        self.layer += 1
        if self.layer >= 4:
            self.layer = 0

    def prepare_font(self):
        pass


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
