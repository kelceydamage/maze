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
import numpy as np
from direct.gui.DirectGui import *
from panda3d.core import TextNode
from renderer.render_utils import removeFilters
from renderer.render_utils import findMethods



# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->
class MenuBar:
    '''
    Menubar objects. This class is to organize assets related to the menubar.
    '''
    def __init__(self):
        self.menubar = DirectFrame(
            pos=(0, -1, -24),
            parent=pixel2d
        )
        maps = loader.loadModel('assets/ui/exit_button.bam')
        maps = removeFilters(maps, 'btn_idle_exit')
        maps = removeFilters(maps, 'btn_over_exit')
        self.btnQuit = DirectButton(
            geom=(
                maps.find('**/btn_idle_exit'),
                maps.find('**/btn_idle_exit'),
                maps.find('**/btn_over_exit'),
                maps.find('**/btn_idle_exit')
            ),
            pressEffect=0,
            relief=None,
            scale=(20, 1, 5),
            pos=(60, 0, 12),
            parent=self.menubar,
        )

        maps = loader.loadModel('assets/ui/options_button.bam')
        maps = removeFilters(maps, 'btn_idle_options')
        maps = removeFilters(maps, 'btn_over_options')
        self.btnOptions = DirectButton(
            geom=(
                maps.find('**/btn_idle_options'),
                maps.find('**/btn_idle_options'),
                maps.find('**/btn_over_options'),
                maps.find('**/btn_idle_options')
            ),
            pressEffect=0,
            relief=None,
            scale=(20, 1, 5),
            pos=(165, 0, 12),
            parent=self.menubar,
        )

        maps = loader.loadModel('assets/ui/options_button.bam')
        maps = removeFilters(maps, 'btn_idle_options')
        maps = removeFilters(maps, 'btn_over_options')
        self.btnMaps = DirectButton(
            geom=(
                maps.find('**/btn_idle_options'),
                maps.find('**/btn_idle_options'),
                maps.find('**/btn_over_options'),
                maps.find('**/btn_idle_options')
            ),
            pressEffect=0,
            relief=None,
            scale=(20, 1, 5),
            pos=(270, 0, 12),
            parent=self.menubar,
        )

        def setMenubarOptions(self):
            self.btnQuit.setTexOffset(TextureStage.getDefault(), 0.35/256, -4/256)
            self.btnOptions.setTexOffset(TextureStage.getDefault(), 0.35/256, -4/256)

class MapView:

    def __init__(self):
        self.origin = [0, 0]
        self.yRange = 32
        self.xRange = 32
        self.colorSpace = np.zeros((self.xRange, self.yRange), dtype=tuple)
        self.panelDimension = 18
        self.xMulti = 1.8
        self.vOffset = 26
        self.xDim = (self.panelDimension * self.xMulti + 1) * self.xRange
        self.yDim = (self.panelDimension + 1) * self.yRange
        self.xPos = base.win.getXSize() - self.xDim - 1
        self.yPos = -base.win.getYSize() + self.vOffset
        self.mapView = DirectFrame(
            pos=(self.xPos - 1, -1, self.yPos),
            frameSize=(self.xDim - 1, 0, self.yDim - 1, 0),
            parent=pixel2d,
            frameColor=(0, 0, 0, 0.8)
        )
        self.panels = {}
        #self.panels = np.zeros((self.xRange, self.yRange), dtype=object)
        self.generatePanels(self.xRange, self.yRange)
        #self.mapView.flattenStrong()
        self.mapView.hide()

        maps = loader.loadModel('assets/ui/options_button.bam')
        maps = removeFilters(maps, 'btn_idle_options')
        maps = removeFilters(maps, 'btn_over_options')
        self.btnLayers = DirectButton(
            geom=(
                maps.find('**/btn_idle_options'),
                maps.find('**/btn_idle_options'),
                maps.find('**/btn_over_options'),
                maps.find('**/btn_idle_options')
            ),
            pressEffect=0,
            relief=None,
            scale=(20, 1, 4.5),
            pos=(49, 0, -14),
            parent=self.mapView
        )

    def generatePanels(self, xRange, yRange):
        xI = 0
        yI = 0
        xMod = self.panelDimension * self.xMulti + 1
        yMod = self.panelDimension + 1
        colorXI = 1 / xRange
        colorYI = 1 / yRange
        for x in range(xRange):
            if x not in self.panels.keys():
                self.panels[x] = {}
            xI += xMod
            for y in range(yRange):
                key = '{0}-{1}'.format(x, yI)
                yI = yMod * y
                xDim = - (self.panelDimension * 1.9) / 2
                yDim = 0
                self.panels[x][y] = TextNode(key)
                self.panels[x][y].setText(key)
                self.panels[x][y].setTextColor(1, 1, 1, 0.99)
                self.panels[x][y].setAlign(TextNode.ACenter)
                self.panels[x][y].setTextScale(14)
                self.panels[x][y].setCardColor(colorXI * x, colorYI * y, 0.5, 0.99)
                self.panels[x][y].setCardDecal(True)
                self.panels[x][y].setCardActual( - xMod / 2, xMod / 2 - 1, yMod * 0.75 - 1, -(yMod / 4))
                textnode = self.mapView.attachNewNode(self.panels[x][y])
                textnode.setPos(xI - xMod / 2, 0, yI + 5)
                self.colorSpace[x, y] = (colorXI * x, colorYI * y, 0.5, 0.99)


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
        '''
        header = TextNode('paused')
        header.setText('Paused')
        header.setTextColor(1, 1, 1, 1)
        header.setAlign(TextNode.ACenter)
        header.setTextScale(30)
        self.pauseTextNodePath = self.pauseBar.attachNewNode(header)

        self.pauseTextNodePath.setPos(base.win.getXSize()/2, 0, -5)

        # Set card color
        text.setCardColor(0, 0, 0, 0.3)
        # Set card margin relative to text rect.
        text.setCardAsMargin(0.2, 0.2, 0.2, 0.2)
        # Necessary for rendering in 3d space
        text.setCardDecal(True)
        '''