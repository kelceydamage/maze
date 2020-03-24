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
from utils.config import Config
from environment import mob
from environment import noise
from environment.state import STATE
from environment.regions import *
import random


# Const
# ------------------------------------------------------------------------ 79->
RESOURCES = {
    0: 'Wood',
    1: 'Food',
    2: 'Coal', 
    3: 'Iron',
    4: 'Gold'
}
TERRAIN = {
    Ocean.index: Ocean(),
    Coastal.index: Coastal(),
    Beach.index: Beach(),
    Forest.index: Forest(),
    Grasslands.index: Grasslands(),
    Barren.index: Barren(),
    Hill.index: Hill(),
    Mountain.index: Mountain()
}
REGIONS = {
    0: 'Barren',
    1: 'Low Grass',
    2: 'Medium Grass', 
    3: 'Overgrown',
    4: 'Forest',
    5: 'Sky',
    7: 'Incline'
}
REGION_TEXTURES = {}
CUBE_MASK = np.array([
    [-1, -1, -1],
    [-1, 0, -1],
    [-1, 1, -1],
    [0, -1, -1],
    [0, 0, -1],
    [0, 1, -1],
    [1, -1, -1],
    [1, 0, -1],
    [1, 1, -1],
    [-1, -1, 0],
    [-1, 0, 0],
    [-1, 1, 0],
    [0, -1, 0],
    [0, 0, 0],
    [0, 1, 0],
    [1, -1, 0],
    [1, 0, 0],
    [1, 1, 0],
    [-1, -1, 1],
    [-1, 0, 1],
    [-1, 1, 1],
    [0, -1, 1],
    [0, 0, 1],
    [0, 1, 1],
    [1, -1, 1],
    [1, 0, 1],
    [1, 1, 1],
])

N_MASK = [
    np.array([-1, -1]),
    np.array([-1, 0]),
    np.array([-1, 1]),
    np.array([0, -1]),
    np.array([0, 1]),
    np.array([1, -1]),
    np.array([1, 0]),
    np.array([1, 1]),
]

T_MASK = [
    np.array([0, -1]), 
    np.array([-1, 0]),
    np.array([0, 1]),
    np.array([1, 0]),
]


# Classes
# ------------------------------------------------------------------------ 79->
class GeneratedMap:
    starting_coordinates = [0, 0]
    width = 100 #Config.map_width
    height = 100 #Config.map_height

    def __init__(self):
        self.tile_width = Config.tile_width
        self.zlevels = Config.zlevels
        self.tiledBG = None
        self.terrain_map = np.zeros(
            (self.zlevels, self.width, self.height), 
            dtype=int
        )
        self.passable_map = np.ones(
            (self.zlevels, self.width, self.height), 
            dtype=int
        )
        # wood, coal, iron, gold, food
        self.resource_map = np.zeros(
            (self.zlevels, self.width, self.height, 6),
            dtype=(object)
        )
        self.precipitation_map = np.zeros(
            (self.zlevels, self.width, self.height), 
            dtype=(object)
        )
        self.rain_map = np.zeros(
            (self.zlevels, self.width, self.height), 
            dtype=(object)
        )
        self.sun_map = np.zeros(
            (self.zlevels, self.width, self.height), 
            dtype=(object)
        )
        self.fertility_map = np.zeros(
            (self.zlevels, self.width, self.height), 
            dtype=(object)
        )
        self.entities = {'mobs': {}, 'items': {}}
        self.images = Config.images
        self.digimages = Config.digimages

    def firstnum(self, num):
        return num // 10

    def secondnum(self, num):
        return num % 10

    def create_resources(self, test, _range, location):
        selector = random.randint(0, _range)
        resources = np.zeros(6)
        if selector in test:
            resources[selector] = random.randint(1,5)
            self.resource_map[location] = resources
        else:
            self.resource_map[location] = resources

    def getNeighbors(self, index, mask=N_MASK):
        return np.array([
            np.add(index, mask[i]) for i in range(len(mask)) 
            if self.width not in np.add(index, mask[i])
        ])

    def paintOceanLayer(self):
        self.terrain_map[self.terrain_map < 9] = 99
        self.terrainColorSpace[self.terrain_map < 9] = 0

    def paintLandSeeds(self, threshold=0.05):
        # Paint some initial random starting points to expand. A higher threshold 
        # will result in more land and less water
        shape = self.terrain_map.shape
        for x in range(shape[1]):
            for y in range(shape[2]):
                if np.random.random(1) < threshold:
                    self.terrain_map[1][x, y] = 3

    def paintMountainSeeds(self, threshold=0.05):
        # Paint some initial random starting points to expand. A higher threshold 
        # will result in more land and less water
        shape = self.terrain_map.shape
        for x in range(shape[1]):
            for y in range(shape[2]):
                if np.random.random(1) < threshold:
                    if self.terrain_map[1][x, y] == 3:
                        self.terrain_map[1][x, y] = 6

    def paintForestSeeds(self, threshold=0.05):
        # Paint some initial random starting points to expand. A higher threshold 
        # will result in more land and less water
        shape = self.terrain_map.shape
        for x in range(shape[1]):
            for y in range(shape[2]):
                if np.random.random(1) < threshold:
                    if self.terrain_map[1][x, y] == 3:
                        self.terrain_map[1][x, y] = 2

    def expandRegion(self, drawType, target, r=0):
        z = np.nonzero(self.terrain_map[1] == drawType)
        shape = self.terrain_map.shape
        for i in range(z[0].shape[0]):
            # get all 8 neighbors
            p = self.getNeighbors((z[0][i], z[1][i]))
            # filter out an indices that are already painted
            valid = [x for x in p if self.terrain_map[1][tuple(x)] == target]
            # if there are any valid indices to pain....
            if valid:
                # select 3 for this iteration
                select = random.choices(valid, k=1)
                # reorder indices
                p1 = np.stack(select, axis=1)
                # paint map
                self.terrain_map[1][tuple(p1)] = drawType
        if r > 0:
            r -= 1
            self.expandRegion(drawType, target, r)

    def printMap(self, _map):
        for row in _map:
            print(row)

    def drawCoastline(self, drawType, target, r=0):
        z = np.nonzero(self.terrain_map[1] == target)
        for i in range(z[0].shape[0]):
            # get all 8 neighbors
            p = self.getNeighbors((z[0][i], z[1][i]), T_MASK)
            # filter out an indices that are already painted
            valid = [
                x for x in p if self.terrain_map[1][x[0], x[1]] != target
                and self.terrain_map[1][x[0], x[1]] != drawType
            ]
            # if there are any valid indices to pain....
            if valid:
                
                if len(valid)  <= 3:
                    # select 3 for this iteration
                    select = random.choices(valid, k=1)
                    # reorder indices
                    p1 = np.stack(select, axis=1)
                    # paint map
                    self.terrain_map[1][tuple(p1)] = drawType
        if r >= 0:
            r -= 1
            self.drawCoastline(drawType, target, r)

    def populate_terrain(self):
        self.terrainColorSpace = np.zeros((2, self.width, self.height), dtype=tuple)
        self.paintOceanLayer()
        self.paintLandSeeds()
        self.expandRegion(3, 99, 4)
        self.paintMountainSeeds()
        self.expandRegion(6, 3, 1)
        self.paintForestSeeds()
        self.expandRegion(2, 3, 2)
        self.drawCoastline(0, 99, 3)
        for z in range(self.zlevels):
            for x in range(self.width):
                for y in range(self.height):
                    location = (z, x ,y)
                    t = TERRAIN[self.terrain_map[location]]
                    self.precipitation_map[location] = random.randint(1, 5) * t.precipitation_growth_rate
                    self.sun_map[location] = random.randint(0, 5) * t.sun_growth_rate
                    self.fertility_map[location] = random.randint(0, 5) * t.fertility_growth_rate
                    self.terrainColorSpace[location] = t.color
                    self.create_resources((0, 1), 2, location)


        '''
        #print(self.resource_map)
        print('Passable Map')
        print('-'*79)
        print(self.passable_map[1])
        print('Terrain Map')
        print('-'*79)
        print(self.terrain_map[1])
        print('Precipitation Map')
        print('-'*79)
        print(self.precipitation_map[1])
        print('Sun Map')
        print('-'*79)
        print(self.sun_map[1])
        print('Fertility Map')
        print('-'*79)
        print(self.fertility_map[1])
        '''

    def initialize_world(self):
        #self.paintOceanLayer()
        self.populate_terrain()
        return {
            "terrain": self.terrain_map,
            "passable": self.passable_map,
            "resources": self.resource_map,
            "entities": self.entities,
            "precipitation": self.precipitation_map,
            "sun": self.sun_map,
            "fertility": self.fertility_map,
            "rain": self.rain_map,
            "terrainColorSpace": self.terrainColorSpace
        }
        print(self.terrain_map)


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->