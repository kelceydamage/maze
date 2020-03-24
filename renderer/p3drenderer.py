
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
from direct.showbase.ShowBase import ShowBase
from pandac.PandaModules import WindowProperties
from renderer.gui import MainGUI
from panda3d.core import *

#for the events
from direct.showbase import DirectObject
#for collision stuff
from pandac.PandaModules import *

# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->



class Renderer(ShowBase):

    def __init__(self):
        super(Renderer, self).__init__()
        self.props = WindowProperties()
        self.props.setTitle( 'Simulation Viewer' )
        self.GUI = MainGUI()
        base.win.requestProperties(self.props)

    def updateCoordinates(self, x, y):
        self.GUI.coords.setText('coords:  x= {0}  y= {1}'.format(x, y))

    def updateTime(self, date):
        self.GUI.time.setText('time:  {0[0]}, {0[1]}, {0[2]}, {0[3]}'.format(date))

    def updateMapView(self, source):
        shape = (2, self.GUI.mapView.xRange, self.GUI.mapView.yRange)
        for x in range(shape[1]):
            xM = x + self.GUI.mapView.origin[0]
            for y in range(shape[2]):
                yM = y + self.GUI.mapView.origin[1]
                if source[0][1][xM, yM] != 0 or source[0][1][xM, yM] != 0.:
                    self.GUI.mapView.panels[x][y].setText(str(source[0][1][xM, yM])[:4])
                else:
                    self.GUI.mapView.panels[x][y].setText(' ')
                if source[0][1][xM, yM] >= source[1]:
                    self.GUI.mapView.panels[x][y].setCardColor(0.22/2, 0.24/2, 0.32/2, 1)
                else:
                    if source[2] is not None:
                        self.GUI.mapView.panels[x][y].setCardColor(source[2][1, xM, yM])
                    else:
                        self.GUI.mapView.panels[x][y].setCardColor(self.GUI.mapView.colorSpace[x, y])


class Picker(DirectObject.DirectObject):

    def __init__(self):
        self.picker = CollisionTraverser()
        self.queue = CollisionHandlerQueue()
        self.pickerNode = CollisionNode('mouseRay')
        self.pickerNP = camera.attachNewNode(self.pickerNode)
        self.pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self.pickerRay = CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.picker.addCollider(self.pickerNode, self.queue)

        #this holds the object that has been picked
        self.pickedObj = None
        self.accept('mouse1', self.printMe)

    #this function is meant to flag an object as being somthing we can pick
    def makePickable(self,newObj):
        newObj.setTag('pickable','true')

    #this function finds the closest object to the camera that has been hit by our ray
    def getObjectHit(self, mpos): #mpos is the position of the mouse on the screen
        self.pickedObj = None #be sure to reset this
        self.pickerRay.setFromLens(base.camNode, mpos.getX(),mpos.getY())
        self.picker.traverse(render)
        if self.queue.getNumEntries() > 0:
            self.queue.sortEntries()
            self.pickedObj = self.queue.getEntry(0).getIntoNodePath()

            parent = self.pickedObj.getParent()
            self.pickedObj = None

            while parent != render:
                if parent.getTag('pickable')=='true':
                    self.pickedObj = parent
                    return parent
                else:
                    parent = parent.getParent()
        return None

    def getPickedObj(self):
        return self.pickedObj

    def printMe(self):
        self.getObjectHit( base.mouseWatcherNode.getMouse())
        print(self.pickedObj)


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->