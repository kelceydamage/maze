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
class Fonts:

    def __init__(self):
        self.ppu = 192
        self.menlo = loader.loadFont("assets/fonts/OpenSans-Regular.ttf")
        self.menloBold = loader.loadFont("assets/fonts/OpenSans-Bold.ttf")
        self.menlo.setPixelsPerUnit(self.ppu)
        self.menlo.setPointSize(8)
        self.menlo.setScaleFactor(0.3189)
        self.menlo.setSpaceAdvance(2)
        self.menlo.setTextureMargin(2)
        self.menlo.setPageSize(x_size=512, y_size=512)
        self.menlo.setLineHeight(1)
        self.menlo.setRenderMode(TextFont.RMTexture)
        self.menlo.setMagfilter(Texture.FTLinearMipmapNearest)
        self.menlo.setNativeAntialias(0)
        self.menloBold.setPixelsPerUnit(256)
        self.menloBold.setPointSize(8)
        self.menloBold.setScaleFactor(0.3189)
        self.menloBold.setSpaceAdvance(2)
        self.menloBold.setTextureMargin(2)
        self.menloBold.setPageSize(x_size=512, y_size=512)
        self.menloBold.setLineHeight(1)
        self.menloBold.setRenderMode(TextFont.RMTexture)
        self.menloBold.setMagfilter(Texture.FTLinearMipmapNearest)
        self.menloBold.setNativeAntialias(0)


# Functions
# ------------------------------------------------------------------------ 79->


# Main
# ------------------------------------------------------------------------ 79->
