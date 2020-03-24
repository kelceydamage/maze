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


# Const
# ------------------------------------------------------------------------ 79->


# Classes
# ------------------------------------------------------------------------ 79->
class Mobs:

    def mob_logic(self):
        for mob in self.mobs:
            if mob.job != None:
                if mob.position == mob.job.move:
                    if mob.job.name == "Channeling":
                        #print "Channeling..."
                        digtype = 7 # create an up ramp
                        diglevel = mob.job.dest[2] - 1 #the z level below
                        self.renderer.map.writeMap(mob.job.dest[0], mob.job.dest[1], diglevel, digtype) # default to a green tile for now.
                        self.renderer.map.setBlocked(mob.job.dest[0], mob.job.dest[1], diglevel, False) # unblock the tile
                        digtype = 5 # put an empty tile on top
                        self.renderer.map.writeMap(mob.job.dest[0], mob.job.dest[1], mob.job.dest[2], digtype) # default to a green tile for now.
                        self.renderer.map.writeEMap(mob.job.dest[0], mob.job.dest[1], mob.job.dest[2], 1) # default to a empty tile for now.
                        self.renderer.map.writeEMapQueue(mob.job.dest[0], mob.job.dest[1], mob.job.dest[2], False)
                        self.renderer.map.setBlocked(mob.job.dest[0], mob.job.dest[1], mob.job.dest[2], True) # unblock the tile
                        mob.job = None
                    elif mob.job.name == "Mining":
                        #print "Mining..."
                        digtype = 1
                        self.renderer.map.writeMap(mob.job.dest[0], mob.job.dest[1], mob.job.dest[2], digtype) # default to a green tile for now.
                        self.renderer.map.writeEMap(mob.job.dest[0], mob.job.dest[1], mob.job.dest[2], 1) # default to a empty tile for now.
                        self.renderer.map.writeEMapQueue(mob.job.dest[0], mob.job.dest[1], mob.job.dest[2], False)
                        self.renderer.map.setBlocked(mob.job.dest[0], mob.job.dest[1], mob.job.dest[2], False) # unblock the tile
                        mob.job = None
                    elif mob.job.name == "MoveItem":
                        #print "Picking up Item"
                        if self.renderer.map.get_items_in_queue(mob.position[0], mob.position[1], mob.position[2]) != None:
                            val = self.renderer.map.mapdata[mob.position[2]][mob.position[0]][mob.position[1]].pickup()
                            mob.carrying = val
                            mob.job = Job('DropItem', mob.job.dest[0], mob.job.dest[0])
                            mob.pathlines = self._recompute_path(self.renderer.map, mob.position, mob.dest)
                        else:
                            print("Job Canceled, no items left")
                            print("SHOULD NOT GET HERE")
                            #mob.job = None #.clearjob()
                    elif mo.job.name == "DropItem":
                        #print "Dropping Item"
                        #print "Item"
                        #pprint(mo.carrying)
                        mob.carrying.selected = False # set the item to false before dropping it.
                        mob.carrying.inqueue = False # set the item to false before dropping it.
                        self.renderer.map.mapdata[mob.job.dest[2]][mob.job.dest[0]][mob.job.dest[1]].add(mob.carrying)
                        mob.carrying = None
                        mob.job = None #.clearjob()
         
                             
            else:
                #print "no Job" # get one
                if len(self.queued_jobs) > 0:
                    mob.job = self.queued_jobs.pop(0)

    def moveMob(self, x, y, zlevel, mob):
        # x, y, z
        oldx, oldy, oldz = mob.position[0], mob.position[1], mob.position[2]
        self.addTileMob(x, y, zlevel, mob) #this will need to be adjusted
        self.delTileMob(oldx, oldy, oldz, mob) #this also will need to be adjusted
        mob.position = (x, y, zlevel)
    
    
    
    def move_mobs(self):
        for mob in self.mobs:
            if len(mob.pathlines) > 0:
                #print "Has a path, walking 1 step of the path"
                move = mob.pathlines.pop(0)
                self.moveMob(move[0], move[1], move[2], mob)
            else:
                if mob.job:
                    print("No pathlines, attempting to snag some")
                    path = self._recompute_path(self.renderer.map, mob.position, mob.job.move)
                    #pprint(path)
                    if path != []:
                        #print "path found"
                        mob.pathlines = path
                    else:
                        mob.job = None

# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
